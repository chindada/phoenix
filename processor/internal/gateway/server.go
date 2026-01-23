package gateway

import (
	"context"
	"net/http"
	"time"

	"phoenix/processor/internal/client"
	"phoenix/processor/internal/repository"
)

type Server struct {
	httpServer *http.Server
}

func New(client client.ShioajiClient, userRepo repository.UserRepository, secret string, port string) *Server {
	router := NewRouter(client, userRepo, secret)
	return &Server{
		httpServer: &http.Server{
			Addr:         ":" + port,
			Handler:      router,
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
