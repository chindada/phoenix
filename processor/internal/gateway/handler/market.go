package handler

import (
	"net/http"

	"github.com/gin-gonic/gin"

	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/pkg/pb"
)

// GetSnapshots godoc
//
//	@Summary		Get Snapshots
//	@Description	Get market snapshots
//	@Tags			Market
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetSnapshotsRequest	true	"Snapshots Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.GetSnapshotsResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/market/snapshots [post]
func (h *Handler) GetSnapshots(c *gin.Context) {
	var req pb.GetSnapshotsRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetSnapshots(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetTicks godoc
//
//	@Summary		Get Ticks
//	@Description	Get market ticks
//	@Tags			Market
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetTicksRequest	true	"Ticks Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.Ticks
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/market/ticks [post]
func (h *Handler) GetTicks(c *gin.Context) {
	var req pb.GetTicksRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetTicks(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetKbars godoc
//
//	@Summary		Get Kbars
//	@Description	Get market kbars
//	@Tags			Market
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetKbarsRequest	true	"Kbars Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.Kbars
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/market/kbars [post]
func (h *Handler) GetKbars(c *gin.Context) {
	var req pb.GetKbarsRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetKbars(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetDailyQuotes godoc
//
//	@Summary		Get Daily Quotes
//	@Description	Get daily quotes
//	@Tags			Market
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetDailyQuotesRequest	true	"Daily Quotes Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.DailyQuotes
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/market/daily-quotes [post]
func (h *Handler) GetDailyQuotes(c *gin.Context) {
	var req pb.GetDailyQuotesRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetDailyQuotes(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetScanners godoc
//
//	@Summary		Get Scanners
//	@Description	Get market scanners
//	@Tags			Market
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetScannersRequest	true	"Scanners Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.GetScannersResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/market/scanners [post]
func (h *Handler) GetScanners(c *gin.Context) {
	var req pb.GetScannersRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetScanners(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetPunish godoc
//
//	@Summary		Get Punish Info
//	@Description	Get stock punishment information
//	@Tags			Market
//	@Produce		json
//	@Security		Bearer
//	@Success		200	{object}	pb.Punish
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/market/punish [get]
func (h *Handler) GetPunish(c *gin.Context) {
	resp, err := h.client.GetPunish(c.Request.Context(), &pb.Empty{})
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetNotice godoc
//
//	@Summary		Get Market Notices
//	@Description	Get market notices
//	@Tags			Market
//	@Produce		json
//	@Security		Bearer
//	@Success		200	{object}	pb.Notice
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/market/notice [get]
func (h *Handler) GetNotice(c *gin.Context) {
	resp, err := h.client.GetNotice(c.Request.Context(), &pb.Empty{})
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// FetchContracts godoc
//
//	@Summary		Fetch Contracts
//	@Description	Fetch contract definitions
//	@Tags			Market
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.FetchContractsRequest	true	"Fetch Contracts Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.Empty
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/market/contracts/fetch [post]
func (h *Handler) FetchContracts(c *gin.Context) {
	var req pb.FetchContractsRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.FetchContracts(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}
