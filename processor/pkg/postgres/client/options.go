package client

import "go.uber.org/zap"

// Option -.
type Option func(*postgresClient)

// MaxPoolSize -.
func MaxPoolSize(size int) Option {
	return func(c *postgresClient) {
		c.maxPoolSize = size
	}
}

// AddLogger -.
func AddLogger(base *zap.Logger) Option {
	return func(c *postgresClient) {
		c.logger = base
	}
}
