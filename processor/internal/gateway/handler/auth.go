package handler

import (
	"errors"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/golang-jwt/jwt/v5"
	"golang.org/x/crypto/bcrypt"

	"phoenix/processor/internal/client"
	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/internal/repository"
	"phoenix/processor/pkg/pb"
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

type LoginRequest struct {
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
}

func (h *Handler) Login(c *gin.Context) {
	var req LoginRequest
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	user, err := h.userRepo.GetByUsername(c.Request.Context(), req.Username)
	if err != nil {
		if errors.Is(err, repository.ErrNotFound) {
			c.JSON(http.StatusUnauthorized, gin.H{"error": "Invalid username or password"})
			return
		}
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Internal server error"})
		return
	}

	if errCompare := bcrypt.CompareHashAndPassword([]byte(user.PasswordHash), []byte(req.Password)); errCompare != nil {
		c.JSON(http.StatusUnauthorized, gin.H{"error": "Invalid username or password"})
		return
	}

	// Generate JWT
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
		"sub": user.Username,
		"exp": time.Now().Add(24 * time.Hour).Unix(),
	})

	tokenString, err := token.SignedString([]byte(h.secret))
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to generate token"})
		return
	}

	// Add token to header
	c.Header("X-Auth-Token", tokenString)

	// Fetch accounts from provider using global session
	resp, err := h.client.ListAccounts(c.Request.Context(), &pb.Empty{})
	if err != nil {
		// Even if fetching accounts fails, we might still want to return the token
		// but for now, let's treat it as an error or return empty accounts
		c.JSON(http.StatusOK, gin.H{"token": tokenString, "accounts": []any{}})
		return
	}

	middleware.Render(c, http.StatusOK, resp)
}
