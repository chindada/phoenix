package httpserver

import (
	"net"

	"go.uber.org/zap"
)

// Option -.
type Option func(*Server)

func Host(host string) Option {
	return func(s *Server) {
		if net.ParseIP(host) == nil {
			return
		}
		s.host = host
	}
}

// Port -.
func Port(port string) Option {
	return func(s *Server) {
		s.port = port
	}
}

func AddLogger(logger *zap.Logger) Option {
	return func(c *Server) {
		c.logger = logger
	}
}

func KeyPath(keyPath string) Option {
	return func(s *Server) {
		s.keyPath = keyPath
	}
}

func CertPath(certPath string) Option {
	return func(s *Server) {
		s.certPath = certPath
	}
}
