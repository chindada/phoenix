package handler

import (
	"net/http"

	"github.com/gin-gonic/gin"

	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/pkg/pb"
)

// ListTrades godoc
//
//	@Summary		List Trades
//	@Description	List all trades
//	@Tags			Trade
//	@Produce		json
//	@Security		Bearer
//	@Success		200	{object}	pb.ListTradesResponse
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/trades [get]
func (h *Handler) ListTrades(c *gin.Context) {
	resp, err := h.client.ListTrades(c.Request.Context(), &pb.Empty{})
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// ListComboTrades godoc
//
//	@Summary		List Combo Trades
//	@Description	List all combo trades
//	@Tags			Trade
//	@Produce		json
//	@Security		Bearer
//	@Success		200	{object}	pb.ListComboTradesResponse
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/trades/combo [get]
func (h *Handler) ListComboTrades(c *gin.Context) {
	resp, err := h.client.ListComboTrades(c.Request.Context(), &pb.Empty{})
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetOrderDealRecords godoc
//
//	@Summary		Get Order Deal Records
//	@Description	Get deal records for orders
//	@Tags			Trade
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetOrderDealRecordsRequest	true	"Deal Records Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.GetOrderDealRecordsResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/trades/deals [get]
func (h *Handler) GetOrderDealRecords(c *gin.Context) {
	var req pb.GetOrderDealRecordsRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetOrderDealRecords(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// SubscribeTrade godoc
//
//	@Summary		Subscribe Trade
//	@Description	Subscribe to trade updates
//	@Tags			Trade
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.SubscribeTradeRequest	true	"Subscribe Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.SubscribeTradeResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/trades/subscribe [post]
func (h *Handler) SubscribeTrade(c *gin.Context) {
	var req pb.SubscribeTradeRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.SubscribeTrade(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// UnsubscribeTrade godoc
//
//	@Summary		Unsubscribe Trade
//	@Description	Unsubscribe from trade updates
//	@Tags			Trade
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.UnsubscribeTradeRequest	true	"Unsubscribe Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.UnsubscribeTradeResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/trades/unsubscribe [post]
func (h *Handler) UnsubscribeTrade(c *gin.Context) {
	var req pb.UnsubscribeTradeRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.UnsubscribeTrade(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}
