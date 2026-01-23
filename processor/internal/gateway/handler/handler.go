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

func New(client client.ShioajiClient, userRepo repository.UserRepository, secret string) *Handler {
	return &Handler{
		client:   client,
		userRepo: userRepo,
		secret:   secret,
	}
}
