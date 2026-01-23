package handler

import (
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/golang-jwt/jwt/v5"
	"phoenix/processor/internal/client"
	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/pkg/pb"
)

type Handler struct {
	client client.ShioajiClient
	secret string
}

func New(client client.ShioajiClient, secret string) *Handler {
	return &Handler{
		client: client,
		secret: secret,
	}
}

func (h *Handler) Login(c *gin.Context) {
	var req pb.LoginRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	resp, err := h.client.Login(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	// Generate JWT
	token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
		"sub": "user", 
		"exp": time.Now().Add(24 * time.Hour).Unix(),
	})
	
	tokenString, err := token.SignedString([]byte(h.secret))
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": "Failed to generate token"})
		return
	}

	// Add token to header
	c.Header("X-Auth-Token", tokenString)
	
	middleware.Render(c, http.StatusOK, resp)
}
