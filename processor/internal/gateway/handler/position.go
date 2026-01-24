package handler

import (
	"net/http"

	"github.com/gin-gonic/gin"

	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/pkg/pb"
)

// ListPositions godoc
//
//	@Summary		List Positions
//	@Description	List all positions
//	@Tags			Position
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.ListPositionsRequest	true	"Positions Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.ListPositionsResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/positions [post]
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

// ListPositionDetail godoc
//
//	@Summary		List Position Detail
//	@Description	Get detailed position information
//	@Tags			Position
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.ListPositionDetailRequest	true	"Position Detail Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.ListPositionDetailResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/positions/detail [post]
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

// ListProfitLoss godoc
//
//	@Summary		List Profit Loss
//	@Description	Get profit and loss information
//	@Tags			Position
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.ListProfitLossRequest	true	"P/L Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.ListProfitLossResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/positions/pnl [post]
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

// ListProfitLossDetail godoc
//
//	@Summary		List Profit Loss Detail
//	@Description	Get detailed profit and loss information
//	@Tags			Position
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.ListProfitLossDetailRequest	true	"P/L Detail Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.ListProfitLossDetailResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/positions/pnl/detail [post]
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

// ListProfitLossSummary godoc
//
//	@Summary		List Profit Loss Summary
//	@Description	Get profit and loss summary
//	@Tags			Position
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.ListProfitLossSummaryRequest	true	"P/L Summary Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.ListProfitLossSummaryResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/positions/pnl/summary [post]
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
