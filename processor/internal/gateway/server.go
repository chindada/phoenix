package gateway

import (
	"context"
	"net/http"
	"time"

	"phoenix/processor/internal/client"
)

type Server struct {
	httpServer *http.Server
}

func New(client client.ShioajiClient, secret string, port string) *Server {
	router := NewRouter(client, secret)
	return &Server{
		httpServer: &http.Server{
			Addr:    ":" + port,
			Handler: router,
			ReadTimeout:  5 * time.Second,
			WriteTimeout: 10 * time.Second,
		},
	}
}

func (s *Server) Run() error {
	return s.httpServer.ListenAndServe()
}

func (s *Server) Shutdown(ctx context.Context) error {
	return s.httpServer.Shutdown(ctx)
}