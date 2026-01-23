// Package httpserver implements HTTP server.
package httpserver

import (
	"context"
	"errors"
	"net"
	"net/http"
	"time"

	"go.uber.org/zap"

	"phoenix/processor/pkg/log"
	"phoenix/processor/pkg/portscan"
)

const (
	_defaultHost              = ""
	_defaultPort              = "80"
	_defaultReadTimeout       = 5 * time.Second
	_defaultReadHeaderTimeout = 5 * time.Second
	_defaultWriteTimeout      = 5 * time.Minute
	_defaultShutdownTimeout   = 3 * time.Second
)

// Server -.
type Server struct {
	srv *http.Server

	host string
	port string

	logger   *zap.Logger
	keyPath  string
	certPath string

	notify chan error
}

// New -.
func New(handler http.Handler, opts ...Option) *Server {
	s := &Server{
		srv: &http.Server{
			Handler:           handler,
			ReadHeaderTimeout: _defaultReadHeaderTimeout,
			ReadTimeout:       _defaultReadTimeout,
			WriteTimeout:      _defaultWriteTimeout,
		},
		notify: make(chan error, 1),
	}

	for _, opt := range opts {
		opt(s)
	}

	if s.logger == nil {
		s.logger = log.L()
	}
	s.srv.ErrorLog = zap.NewStdLog(s.logger)
	if s.host == "" {
		s.host = _defaultHost
	}
	if s.port == "" {
		s.port = _defaultPort
	}
	s.srv.Addr = net.JoinHostPort(s.host, s.port)
	return s
}

// Start starts the server.
func (s *Server) Start() error {
	lc := net.ListenConfig{}
	l, err := lc.Listen(context.Background(), "tcp", s.srv.Addr)
	if err != nil {
		return err
	}
	s.srv.Addr = l.Addr().String()
	go func() {
		var srvErr error
		if s.certPath == "" || s.keyPath == "" {
			srvErr = s.srv.Serve(l)
		} else {
			srvErr = s.srv.ServeTLS(l, s.certPath, s.keyPath)
		}
		if srvErr != nil && srvErr != http.ErrServerClosed {
			s.notify <- srvErr
		}
	}()
	s.logger.Info("HTTP server started", zap.String("addr", s.srv.Addr))
	return nil
}

// StartWithRandomPort starts the server on a random port.
func (s *Server) StartWithRandomPort() error {
	scanner := portscan.NewPortScan()
	s.port = scanner.GetRandomPort()
	if s.port == "" {
		return errors.New("failed to find free port")
	}
	s.srv.Addr = net.JoinHostPort(s.host, s.port)
	return s.Start()
}

// Notify returns a channel that will receive any server error.
func (s *Server) Notify() <-chan error {
	return s.notify
}

// Shutdown gracefully shuts down the server.
func (s *Server) Shutdown() error {
	ctx, cancel := context.WithTimeout(context.Background(), _defaultShutdownTimeout)
	defer cancel()
	return s.srv.Shutdown(ctx)
}

// GetListenPort returns the port the server is listening on.
func (s *Server) GetListenPort() string {
	_, port, err := net.SplitHostPort(s.srv.Addr)
	if err != nil {
		return s.port
	}
	return port
}
