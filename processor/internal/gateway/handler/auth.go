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
		// Even if fetching accounts fails, we might still want to return the token
		// but for now, let's treat it as an error or return empty accounts
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

// ActivateCA godoc
//
//	@Summary		Activate CA
//	@Description	Activate the Certificate Authority for the user
//	@Tags			Auth
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.ActivateCARequest	true	"CA Activation Details"
//	@Security		Bearer
//	@Success		200	{object}	pb.ActivateCAResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/ca/activate [post]
func (h *Handler) ActivateCA(c *gin.Context) {
	var req pb.ActivateCARequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.ActivateCA(c.Request.Context(), &req)
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
//	@Router			/api/v1/ca/expire [get]
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
