package gateway

import (
	"github.com/gin-gonic/gin"
	"phoenix/processor/internal/client"
	"phoenix/processor/internal/gateway/handler"
	"phoenix/processor/internal/gateway/middleware"
)

func NewRouter(client client.ShioajiClient, secret string) *gin.Engine {
	r := gin.Default()
	h := handler.New(client, secret)

	v1 := r.Group("/api/v1")
	{
		v1.POST("/login", h.Login)
		
		// Protected routes
		protected := v1.Group("/")
		protected.Use(middleware.Auth(secret))
		{
			// Add trade routes later
		}
	}
	return r
}
