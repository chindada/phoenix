package handler

import (
	"net/http"

	"github.com/gin-gonic/gin"
	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/pkg/pb"
)

func (h *Handler) ListAccounts(c *gin.Context) {
	resp, err := h.client.ListAccounts(c.Request.Context(), &pb.Empty{})
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

func (h *Handler) PlaceOrder(c *gin.Context) {
	var req pb.PlaceOrderRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.PlaceOrder(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

func (h *Handler) CancelOrder(c *gin.Context) {
	var req pb.CancelOrderRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.CancelOrder(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

func (h *Handler) ListTrades(c *gin.Context) {
	resp, err := h.client.ListTrades(c.Request.Context(), &pb.Empty{})
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

func (h *Handler) ListPositions(c *gin.Context) {
	var req pb.ListPositionsRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.ListPositions(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}
