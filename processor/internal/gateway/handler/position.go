package handler

import (
	"net/http"

	"github.com/gin-gonic/gin"

	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/pkg/pb"
)

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

func (h *Handler) ListPositionDetail(c *gin.Context) {
	var req pb.ListPositionDetailRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.ListPositionDetail(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

func (h *Handler) ListProfitLoss(c *gin.Context) {
	var req pb.ListProfitLossRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.ListProfitLoss(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

func (h *Handler) ListProfitLossDetail(c *gin.Context) {
	var req pb.ListProfitLossDetailRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.ListProfitLossDetail(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

func (h *Handler) ListProfitLossSummary(c *gin.Context) {
	var req pb.ListProfitLossSummaryRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.ListProfitLossSummary(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}
