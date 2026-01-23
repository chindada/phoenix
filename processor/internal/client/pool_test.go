package client_test

import (
	"testing"

	"phoenix/processor/internal/client"
)

func TestNewClient(t *testing.T) {
	cfg := client.Config{
		Target:   "localhost:50051",
		PoolSize: 2,
	}

	c, err := client.New(cfg)
	if err != nil {
		t.Fatalf("New() failed: %v", err)
	}
	defer c.Close()

	if c == nil {
		t.Fatal("New() returned nil client")
	}
}
