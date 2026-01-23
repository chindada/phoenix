package client

import (
	"crypto/tls"

	"go.uber.org/zap"
)

type Option func(*client)

func UID(username string) Option {
	return func(s *client) {
		s.uid = username
	}
}

func Password(password string) Option {
	return func(s *client) {
		s.password = password
	}
}

func Host(host string) Option {
	return func(s *client) {
		s.host = host
	}
}

func Port(port string) Option {
	return func(s *client) {
		s.port = port
	}
}

func AddLogger(base *zap.Logger) Option {
	return func(c *client) {
		c.logger = base
	}
}

func WithTLSConfig(config *tls.Config) Option {
	return func(c *client) {
		c.tlsConfig = config
	}
}

func WithScheme(scheme string) Option {
	return func(c *client) {
		c.scheme = scheme
	}
}
