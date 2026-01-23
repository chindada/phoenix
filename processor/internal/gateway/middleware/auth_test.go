package middleware_test

import (
	"net/http"
	"net/http/httptest"
	"testing"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/golang-jwt/jwt/v5"

	"phoenix/processor/internal/gateway/middleware"
)

func TestAuthMiddleware(t *testing.T) {
	// Setup
	gin.SetMode(gin.TestMode)
	secret := "test-secret"
	
	tests := []struct {
		name       string
		token      string
		setupToken func() string
		wantStatus int
	}{
		{
			name:       "No Header",
			token:      "",
			wantStatus: http.StatusUnauthorized,
		},
		{
			name:       "Invalid Token",
			token:      "Bearer invalid",
			wantStatus: http.StatusUnauthorized,
		},
		{
			name: "Valid Token",
			setupToken: func() string {
				token := jwt.NewWithClaims(jwt.SigningMethodHS256, jwt.MapClaims{
					"sub": "user123",
					"exp": time.Now().Add(time.Hour).Unix(),
				})
				s, _ := token.SignedString([]byte(secret))
				return "Bearer " + s
			},
			wantStatus: http.StatusOK,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			w := httptest.NewRecorder()
			c, _ := gin.CreateTestContext(w)
			
			req, _ := http.NewRequest("GET", "/", nil)
			if tt.setupToken != nil {
				req.Header.Set("Authorization", tt.setupToken())
			} else if tt.token != "" {
				req.Header.Set("Authorization", tt.token)
			}
			c.Request = req

			// Call middleware
			handler := middleware.Auth(secret)
			handler(c)

			if w.Code != tt.wantStatus {
				t.Errorf("Auth() status = %v, want %v", w.Code, tt.wantStatus)
			}
		})
	}
}
