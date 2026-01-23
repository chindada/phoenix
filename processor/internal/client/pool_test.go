package client

import (
	"testing"
)

func TestNewClient(t *testing.T) {
	cfg := Config{
		Target:   "localhost:50051",
		PoolSize: 2,
	}
	
	c, err := New(cfg)
	if err != nil {
		t.Fatalf("New() failed: %v", err)
	}
	defer c.Close()

	if c == nil {
		t.Fatal("New() returned nil client")
	}
}
