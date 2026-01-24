package gateway

import (
	"github.com/gin-gonic/gin"

	"phoenix/processor/internal/client"
	_ "phoenix/processor/internal/gateway/docs"
	"phoenix/processor/internal/gateway/handler"
	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/internal/repository"

	swaggerFiles "github.com/swaggo/files"
	ginSwagger "github.com/swaggo/gin-swagger"
)

// NewRouter -.
//
//	@title						Phoenix API
//	@version					1.0
//	@description				REST API Gateway for Shioaji Trading Provider.
//	@termsOfService				http://swagger.io/terms/
//	@contact.name				API Support
//	@contact.url				http://www.swagger.io/support
//	@contact.email				support@swagger.io
//	@license.name				Apache 2.0
//	@license.url				http://www.apache.org/licenses/LICENSE-2.0.html
//	@host						localhost:8080
//	@BasePath					/
//	@securityDefinitions.apikey	Bearer
//	@in							header
//	@name						Authorization
//	@description				Type "Bearer" followed by a space and then your token.
func NewRouter(client client.ShioajiClient, userRepo repository.UserRepository, secret string) *gin.Engine {
	r := gin.Default()

	// Swagger UI
	r.GET("/api/doc/*any", ginSwagger.WrapHandler(swaggerFiles.Handler))

	h := handler.New(client, userRepo, secret)

	v1 := r.Group("/api/v1")
	{
		v1.POST("/login", h.Login)

		// Protected routes
		protected := v1.Group("/")
		protected.Use(middleware.Auth(secret))
		{
			// Auth
			protected.POST("/logout", h.Logout)
			protected.POST("/ca/activate", h.ActivateCA)
			protected.GET("/ca/expire", h.GetCAExpireTime)

			// Account
			protected.GET("/accounts", h.ListAccounts)
			protected.GET("/usage", h.GetUsage)
			protected.GET("/accounts/balance", h.GetAccountBalance)
			protected.GET("/accounts/settlements", h.GetSettlements)
			protected.GET("/accounts/margin", h.GetMargin)
			protected.GET("/accounts/limits", h.GetTradingLimits)

			// Order
			protected.POST("/orders", h.PlaceOrder)
			protected.POST("/orders/combo", h.PlaceComboOrder)
			protected.PUT("/orders", h.UpdateOrder)
			protected.POST("/orders/cancel", h.CancelOrder)
			protected.POST("/orders/combo/cancel", h.CancelComboOrder)
			protected.POST("/orders/status", h.UpdateStatus)
			protected.POST("/orders/combo/status", h.UpdateComboStatus)

			// Trade
			protected.GET("/trades", h.ListTrades)
			protected.GET("/trades/combo", h.ListComboTrades)
			protected.GET("/trades/deals", h.GetOrderDealRecords)
			protected.POST("/trades/subscribe", h.SubscribeTrade)
			protected.POST("/trades/unsubscribe", h.UnsubscribeTrade)

			// Position
			protected.POST("/positions", h.ListPositions)
			protected.POST("/positions/detail", h.ListPositionDetail)
			protected.POST("/positions/pnl", h.ListProfitLoss)
			protected.POST("/positions/pnl/detail", h.ListProfitLossDetail)
			protected.POST("/positions/pnl/summary", h.ListProfitLossSummary)

			// Market Data
			protected.POST("/market/snapshots", h.GetSnapshots)
			protected.POST("/market/ticks", h.GetTicks)
			protected.POST("/market/kbars", h.GetKbars)
			protected.POST("/market/daily-quotes", h.GetDailyQuotes)
			protected.POST("/market/scanners", h.GetScanners)
			protected.GET("/market/punish", h.GetPunish)
			protected.GET("/market/notice", h.GetNotice)
			protected.POST("/market/contracts/fetch", h.FetchContracts)

			// Reserve
			protected.POST("/reserve/stocks/summary", h.GetStockReserveSummary)
			protected.POST("/reserve/stocks/detail", h.GetStockReserveDetail)
			protected.POST("/reserve/stocks", h.ReserveStock)
			protected.POST("/reserve/earmarking/detail", h.GetEarmarkingDetail)
			protected.POST("/reserve/earmarking", h.ReserveEarmarking)
			protected.POST("/reserve/credit-enquires", h.CreditEnquires)
			protected.POST("/reserve/short-stock-sources", h.GetShortStockSources)
		}
	}
	return r
}
