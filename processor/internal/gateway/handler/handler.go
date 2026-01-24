package handler

import (
	"phoenix/processor/internal/client"
	"phoenix/processor/internal/repository"
)

type Handler struct {
	client   client.ShioajiClient
	userRepo repository.UserRepository
	secret   string
}

// APIError represents a standard error response
type APIError struct {
	Error string `json:"error" example:"error message"`
}

func New(client client.ShioajiClient, userRepo repository.UserRepository, secret string) *Handler {
	return &Handler{
		client:   client,
		userRepo: userRepo,
		secret:   secret,
	}
}
