package client

import (
	"fmt"
	"sync/atomic"

	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
	"phoenix/processor/pkg/pb"
)

type Config struct {
	Target   string
	PoolSize int
}

type Client struct {
	conns    []*grpc.ClientConn
	clients  []pb.ShioajiProviderClient
	poolSize uint64
	next     uint64
}

func New(cfg Config) (*Client, error) {
	if cfg.PoolSize <= 0 {
		cfg.PoolSize = 1
	}

	conns := make([]*grpc.ClientConn, cfg.PoolSize)
	clients := make([]pb.ShioajiProviderClient, cfg.PoolSize)

	// Service config for retries
	serviceConfig := `{"methodConfig": [{
		"name": [{"service": "v1.ShioajiProvider"}],
		"retryPolicy": {
			"MaxAttempts": 3,
			"InitialBackoff": "0.1s",
			"MaxBackoff": "1s",
			"BackoffMultiplier": 2,
			"RetryableStatusCodes": ["UNAVAILABLE"]
		}
	}]}`

	opts := []grpc.DialOption{
		grpc.WithTransportCredentials(insecure.NewCredentials()),
		grpc.WithDefaultServiceConfig(serviceConfig),
	}

	for i := range cfg.PoolSize {
		conn, err := grpc.NewClient(cfg.Target, opts...)
		if err != nil {
			// Clean up already opened connections
			for j := range i {
				_ = conns[j].Close()
			}
			return nil, fmt.Errorf("failed to dial %s: %w", cfg.Target, err)
		}
		conns[i] = conn
		clients[i] = pb.NewShioajiProviderClient(conn)
	}

	return &Client{
		conns:    conns,
		clients:  clients,
		poolSize: uint64(cfg.PoolSize),
	}, nil
}

func (c *Client) Close() error {
	var firstErr error
	for _, conn := range c.conns {
		if err := conn.Close(); err != nil && firstErr == nil {
			firstErr = err
		}
	}
	return firstErr
}

func (c *Client) getNextClient() pb.ShioajiProviderClient {
	idx := atomic.AddUint64(&c.next, 1) % c.poolSize
	return c.clients[idx]
}
