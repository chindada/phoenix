package main

import (
	"context"
	"fmt"
	"os"
	"os/signal"
	"syscall"
	"time"

	"go.uber.org/zap"
	"golang.org/x/crypto/bcrypt"

	"phoenix/processor/internal/client"
	"phoenix/processor/internal/gateway"
	"phoenix/processor/internal/repository"
	"phoenix/processor/pkg/log"
	"phoenix/processor/pkg/pb"
	pgClient "phoenix/processor/pkg/postgres/client"
	"phoenix/processor/pkg/postgres/launcher"
)

func main() {
	// Configuration
	providerAddr := os.Getenv("PROVIDER_ADDR")
	if providerAddr == "" {
		providerAddr = "localhost:50051"
	}
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	jwtSecret := os.Getenv("JWT_SECRET")
	if jwtSecret == "" {
		jwtSecret = "default-secret-do-not-use-in-prod"
	}
	shioajiKey := os.Getenv("SHIOAJI_API_KEY")
	shioajiSecret := os.Getenv("SHIOAJI_SECRET_KEY")

	// Initialize Database
	dbLauncher, err := launcher.New(
		launcher.DBName("mojave"),
		launcher.AddLogger(log.L()),
	)
	if err != nil {
		log.L().Fatal("Failed to create db launcher", zap.Error(err))
	}

	if !dbLauncher.DatabaseAlreadyExists() {
		if err = dbLauncher.InitDB(true); err != nil {
			log.L().Fatal("Failed to initialize database", zap.Error(err))
		}
	} else {
		if err = dbLauncher.StartDB(); err != nil {
			log.L().Fatal("Failed to start database", zap.Error(err))
		}
	}
	defer func() {
		if errStop := dbLauncher.StopDB(); errStop != nil {
			log.L().Error("Failed to stop database", zap.Error(errStop))
		}
	}()

	if err = dbLauncher.MigrateScheme(nil); err != nil {
		log.L().Fatal("Failed to run migrations", zap.Error(err))
	}

	// Initialize PG Client
	pgUrl := fmt.Sprintf("postgres://postgres:password@localhost:5432/mojave?sslmode=disable")
	pg, err := pgClient.New(pgUrl, pgClient.AddLogger(log.L()))
	if err != nil {
		log.L().Fatal("Failed to connect to postgres", zap.Error(err))
	}
	defer pg.Close()

	userRepo := repository.NewUserRepository(pg)

	// Seed Admin User
	ctx := context.Background()
	count, err := userRepo.Count(ctx)
	if err != nil {
		log.L().Fatal("Failed to count users", zap.Error(err))
	}
	if count == 0 {
		hash, _ := bcrypt.GenerateFromPassword([]byte("admin"), bcrypt.DefaultCost)
		err = userRepo.Create(ctx, &repository.User{
			Username:     "admin",
			PasswordHash: string(hash),
			CreatedAt:    time.Now(),
			UpdatedAt:    time.Now(),
		})
		if err != nil {
			log.L().Fatal("Failed to seed admin user", zap.Error(err))
		}
		log.L().Info("Seeded default admin user")
	}

	// Initialize gRPC Client
	log.L().Info("Connecting to provider", zap.String("address", providerAddr))
	grpcClient, err := client.New(client.Config{
		Target:   providerAddr,
		PoolSize: 5,
	})
	if err != nil {
		log.L().Fatal("Failed to create grpc client", zap.Error(err))
	}
	defer grpcClient.Close()

	// System Login to Provider
	if shioajiKey != "" && shioajiSecret != "" {
		log.L().Info("Performing system login to provider")
		_, err = grpcClient.Login(ctx, &pb.LoginRequest{
			ApiKey:    shioajiKey,
			SecretKey: shioajiSecret,
		})
		if err != nil {
			log.L().Error("System login failed", zap.Error(err))
		} else {
			log.L().Info("System login successful")
		}
	} else {
		log.L().Warn("SHIOAJI_API_KEY or SHIOAJI_SECRET_KEY not set, skipping system login")
	}

	// Initialize REST Gateway
	srv := gateway.New(grpcClient, userRepo, jwtSecret, port)

	// Run Server in Goroutine
	go func() {
		log.L().Info("Starting REST Gateway", zap.String("port", port))
		if errRun := srv.Run(); errRun != nil {
			log.L().Fatal("Server failed", zap.Error(errRun))
		}
	}()

	// Graceful Shutdown
	quit := make(chan os.Signal, 1)
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
	<-quit
	log.L().Info("Shutting down server...")

	ctxShutdown, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	if errShutdown := srv.Shutdown(ctxShutdown); errShutdown != nil {
		log.L().Fatal("Server forced to shutdown", zap.Error(errShutdown))
	}

	log.L().Info("Server exiting")
}
