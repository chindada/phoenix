package handler

import (
	"errors"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/golang-jwt/jwt/v5"
	"golang.org/x/crypto/bcrypt"

	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/internal/repository"
	"phoenix/processor/pkg/pb"
)

type LoginRequest struct {
	Username string `json:"username" binding:"required"`
	Password string `json:"password" binding:"required"`
}

// Login godoc
//
//	@Summary		System/User Login
//	@Description	Authenticate with username and password to get a JWT token
//	@Tags			Auth
//	@Accept			json
//	@Produce		json
//	@Param			request	body		LoginRequest	true	"Login Credentials"
//	@Success		200		{object}	pb.ListAccountsResponse
//	@Failure		400		{object}	APIError
//	@Failure		401		{object}	APIError
//	@Failure		500		{object}	APIError
//	@Router			/api/v1/login [post]
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
		c.JSON(http.StatusOK, gin.H{"token": tokenString, "accounts": []any{}})
		return
	}

	middleware.Render(c, http.StatusOK, resp)
}

// Logout godoc
//
//	@Summary		User Logout
//	@Description	Invalidate the session (placeholder for now)
//	@Tags			Auth
//	@Produce		json
//	@Security		Bearer
//	@Success		200	{object}	pb.LogoutResponse
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/logout [post]
func (h *Handler) Logout(c *gin.Context) {
	resp, err := h.client.Logout(c.Request.Context(), &pb.Empty{})
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetCAExpireTime godoc
//
//	@Summary		Get CA Expire Time
//	@Description	Retrieve the expiration time of the user's Certificate Authority
//	@Tags			Auth
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetCAExpireTimeRequest	true	"CA Details"
//	@Security		Bearer
//	@Success		200	{object}	pb.GetCAExpireTimeResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/ca/expire [post]
func (h *Handler) GetCAExpireTime(c *gin.Context) {
	var req pb.GetCAExpireTimeRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetCAExpireTime(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}
