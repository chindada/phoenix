package gateway

import (
	"github.com/gin-gonic/gin"

	"phoenix/processor/internal/client"
	"phoenix/processor/internal/gateway/handler"
	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/internal/repository"
)

func NewRouter(client client.ShioajiClient, userRepo repository.UserRepository, secret string) *gin.Engine {
	r := gin.Default()
	h := handler.New(client, userRepo, secret)

	v1 := r.Group("/api/v1")
	{
		v1.POST("/login", h.Login)

		// Protected routes
		protected := v1.Group("/")
		protected.Use(middleware.Auth(secret))
		{
			protected.GET("/accounts", h.ListAccounts)
			protected.POST("/orders", h.PlaceOrder)
			protected.POST("/orders/cancel", h.CancelOrder)
			protected.GET("/trades", h.ListTrades)
			protected.POST("/positions", h.ListPositions)
		}
	}
	return r
}
