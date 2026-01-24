package handler

import (
	"net/http"

	"github.com/gin-gonic/gin"

	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/pkg/pb"
)

// GetStockReserveSummary godoc
//
//	@Summary		Get Stock Reserve Summary
//	@Description	Get summary of stock reserves
//	@Tags			Reserve
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetStockReserveSummaryRequest	true	"Reserve Summary Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.ReserveStocksSummaryResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/reserve/stocks/summary [post]
func (h *Handler) GetStockReserveSummary(c *gin.Context) {
	var req pb.GetStockReserveSummaryRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetStockReserveSummary(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetStockReserveDetail godoc
//
//	@Summary		Get Stock Reserve Detail
//	@Description	Get detailed stock reserve info
//	@Tags			Reserve
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetStockReserveDetailRequest	true	"Reserve Detail Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.ReserveStocksDetailResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/reserve/stocks/detail [post]
func (h *Handler) GetStockReserveDetail(c *gin.Context) {
	var req pb.GetStockReserveDetailRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetStockReserveDetail(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// ReserveStock godoc
//
//	@Summary		Reserve Stock
//	@Description	Reserve stock for trading
//	@Tags			Reserve
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.ReserveStockRequest	true	"Reserve Stock Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.ReserveStockResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/reserve/stocks [post]
func (h *Handler) ReserveStock(c *gin.Context) {
	var req pb.ReserveStockRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.ReserveStock(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetEarmarkingDetail godoc
//
//	@Summary		Get Earmarking Detail
//	@Description	Get earmarking details
//	@Tags			Reserve
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetEarmarkingDetailRequest	true	"Earmarking Detail Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.EarmarkStocksDetailResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/reserve/earmarking/detail [post]
func (h *Handler) GetEarmarkingDetail(c *gin.Context) {
	var req pb.GetEarmarkingDetailRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetEarmarkingDetail(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// ReserveEarmarking godoc
//
//	@Summary		Reserve Earmarking
//	@Description	Reserve funds for earmarking
//	@Tags			Reserve
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.ReserveEarmarkingRequest	true	"Reserve Earmarking Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.ReserveEarmarkingResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/reserve/earmarking [post]
func (h *Handler) ReserveEarmarking(c *gin.Context) {
	var req pb.ReserveEarmarkingRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.ReserveEarmarking(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// CreditEnquires godoc
//
//	@Summary		Credit Enquiries
//	@Description	Enquire about credit
//	@Tags			Reserve
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.CreditEnquiresRequest	true	"Credit Enquiries Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.CreditEnquiresResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/reserve/credit-enquires [post]
func (h *Handler) CreditEnquires(c *gin.Context) {
	var req pb.CreditEnquiresRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.CreditEnquires(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetShortStockSources godoc
//
//	@Summary		Get Short Stock Sources
//	@Description	Get sources for short selling
//	@Tags			Reserve
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetShortStockSourcesRequest	true	"Short Stock Sources Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.GetShortStockSourcesResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/reserve/short-stock-sources [post]
func (h *Handler) GetShortStockSources(c *gin.Context) {
	var req pb.GetShortStockSourcesRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetShortStockSources(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}
