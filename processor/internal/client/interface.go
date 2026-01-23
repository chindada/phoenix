package client

import (
	"phoenix/processor/pkg/pb"
)

// ShioajiClient defines the interface for the Shioaji Provider gRPC client.
// It includes all methods from pb.ShioajiProviderClient plus lifecycle management.
type ShioajiClient interface {
	pb.ShioajiProviderClient
	Close() error
}
