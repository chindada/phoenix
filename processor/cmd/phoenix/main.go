package main

import (
	"context"
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

type config struct {
	providerAddr  string
	port          string
	jwtSecret     string
	shioajiKey    string
	shioajiSecret string
}

func loadConfig() config {
	return config{
		providerAddr:  getEnv("PROVIDER_ADDR", "localhost:50051"),
		port:          getEnv("PORT", "8080"),
		jwtSecret:     getEnv("JWT_SECRET", "default-secret-do-not-use-in-prod"),
		shioajiKey:    os.Getenv("SHIOAJI_API_KEY"),
		shioajiSecret: os.Getenv("SHIOAJI_SECRET_KEY"),
	}
}

func getEnv(key, fallback string) string {
	if value, ok := os.LookupEnv(key); ok {
		return value
	}
	return fallback
}

func setupDB() (launcher.Launcher, pgClient.PGClient, error) {
	dbLauncher, err := launcher.New(
		launcher.DBName("phoenix"),
		launcher.AddLogger(log.L()),
		launcher.EnableLog(),
	)
	if err != nil {
		return nil, nil, err
	}

	if !dbLauncher.DatabaseAlreadyExists() {
		if err = dbLauncher.InitDB(true); err != nil {
			return nil, nil, err
		}
	} else {
		if err = dbLauncher.StartDB(); err != nil {
			return nil, nil, err
		}
	}

	if err = dbLauncher.MigrateScheme(nil); err != nil {
		return dbLauncher, nil, err
	}

	pgURL := "postgres://postgres:password@localhost:5432/phoenix?sslmode=disable"
	if socket := dbLauncher.GetSocketPath(); socket != "" {
		pgURL = "postgres://postgres:password@?host=localhost&port=5432&dbname=phoenix&sslmode=disable"
		log.L().Info("Connecting to postgres socket", zap.String("path", socket))
	}
	pg, err := pgClient.New(pgURL, pgClient.AddLogger(log.L()))
	if err != nil {
		return dbLauncher, nil, err
	}

	return dbLauncher, pg, nil
}

func seedAdminUser(ctx context.Context, repo repository.UserRepository) error {
	count, err := repo.Count(ctx)
	if err != nil {
		return err
	}

	if count == 0 {
		hash, errHash := bcrypt.GenerateFromPassword([]byte("admin"), bcrypt.DefaultCost)
		if errHash != nil {
			return errHash
		}
		err = repo.Create(ctx, &repository.User{
			Username:     "admin",
			PasswordHash: string(hash),
			CreatedAt:    time.Now(),
			UpdatedAt:    time.Now(),
		})
		if err != nil {
			return err
		}
		log.L().Info("Seeded default admin user")
	}
	return nil
}

func initGRPCClient(ctx context.Context, addr, key, secret string) (*client.Client, error) {
	log.L().Info("Connecting to provider", zap.String("address", addr))
	grpcClient, err := client.New(client.Config{
		Target:   addr,
		PoolSize: 5,
	})
	if err != nil {
		return nil, err
	}

	if key != "" && secret != "" {
		log.L().Info("Performing system login to provider")
		_, err = grpcClient.Login(ctx, &pb.LoginRequest{
			ApiKey:    key,
			SecretKey: secret,
		})
		if err != nil {
			log.L().Error("System login failed", zap.Error(err))
		} else {
			log.L().Info("System login successful")
		}
	} else {
		log.L().Warn("SHIOAJI_API_KEY or SHIOAJI_SECRET_KEY not set, skipping system login")
	}

	return grpcClient, nil
}

func main() {
	cfg := loadConfig()
	ctx := context.Background()

	// Initialize Database
	dbLauncher, pg, err := setupDB()
	if err != nil {
		log.L().Fatal("Failed to setup database", zap.Error(err))
	}
	defer func() {
		if dbLauncher != nil {
			_ = dbLauncher.StopDB()
		}
	}()
	defer pg.Close()

	userRepo := repository.NewUserRepository(pg)
	if err = seedAdminUser(ctx, userRepo); err != nil {
		log.L().Fatal("Failed to seed admin user", zap.Error(err))
	}

	// Initialize gRPC Client
	grpcClient, err := initGRPCClient(ctx, cfg.providerAddr, cfg.shioajiKey, cfg.shioajiSecret)
	if err != nil {
		log.L().Fatal("Failed to create grpc client", zap.Error(err))
	}
	defer grpcClient.Close()

	// Initialize REST Gateway
	srv := gateway.New(grpcClient, userRepo, cfg.jwtSecret, cfg.port)

	// Run Server
	go func() {
		log.L().Info("Starting REST Gateway", zap.String("port", cfg.port))
		if errRun := srv.Run(); errRun != nil {
			log.L().Error("REST Gateway stopped", zap.Error(errRun))
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
