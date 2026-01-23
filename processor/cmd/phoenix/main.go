package main

import (
	"context"
	"log"
	"os"
	"os/signal"
	"syscall"
	"time"

	"phoenix/processor/internal/client"
	"phoenix/processor/internal/gateway"
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
	log.Printf("Connecting to provider at %s...", providerAddr)
	grpcClient, err := client.New(client.Config{
		Target:   providerAddr,
		PoolSize: 5,
	})
	if err != nil {
		log.Fatalf("Failed to create grpc client: %v", err)
	}
	defer grpcClient.Close()

	// Initialize REST Gateway
	srv := gateway.New(grpcClient, jwtSecret, port)

	// Run Server in Goroutine
	go func() {
		log.Printf("Starting REST Gateway on port %s...", port)
		if err := srv.Run(); err != nil {
			log.Fatalf("Server failed: %v", err)
		}
	}()

	// Graceful Shutdown
	quit := make(chan os.Signal, 1)
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
	<-quit
	log.Println("Shutting down server...")

	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Second)
	defer cancel()
	if err := srv.Shutdown(ctx); err != nil {
		log.Fatalf("Server forced to shutdown: %v", err)
	}

	log.Println("Server exiting")
}