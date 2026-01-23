package main

import (
	"context"
	"os"
	"os/signal"
	"syscall"
	"time"

	"go.uber.org/zap"

	"phoenix/processor/internal/client"
	"phoenix/processor/internal/gateway"
	"phoenix/processor/pkg/log"
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

	// Initialize REST Gateway
	srv := gateway.New(grpcClient, jwtSecret, port)

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

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	if errShutdown := srv.Shutdown(ctx); errShutdown != nil {
		log.L().Fatal("Server forced to shutdown", zap.Error(errShutdown))
	}

	log.L().Info("Server exiting")
}
