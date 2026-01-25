package handler

import (
	"net/http"

	"github.com/gin-gonic/gin"

	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/pkg/pb"
)

// ListAccounts godoc
//
//	@Summary		List Accounts
//	@Description	List all accounts available for the user
//	@Tags			Account
//	@Produce		json
//	@Security		Bearer
//	@Success		200	{object}	pb.ListAccountsResponse
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/accounts [get]
func (h *Handler) ListAccounts(c *gin.Context) {
	resp, err := h.client.ListAccounts(c.Request.Context(), &pb.Empty{})
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetUsage godoc
//
//	@Summary		Get Usage
//	@Description	Get usage information
//	@Tags			Account
//	@Produce		json
//	@Security		Bearer
//	@Success		200	{object}	pb.UsageStatus
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/usage [get]
func (h *Handler) GetUsage(c *gin.Context) {
	resp, err := h.client.GetUsage(c.Request.Context(), &pb.Empty{})
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetAccountBalance godoc
//
//	@Summary		Get Account Balance
//	@Description	Get balance for the account
//	@Tags			Account
//	@Produce		json
//	@Security		Bearer
//	@Success		200	{object}	pb.AccountBalance
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/accounts/balance [get]
func (h *Handler) GetAccountBalance(c *gin.Context) {
	resp, err := h.client.GetAccountBalance(c.Request.Context(), &pb.Empty{})
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetSettlements godoc
//
//	@Summary		Get Settlements
//	@Description	Get settlement information
//	@Tags			Account
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetSettlementsRequest	true	"Settlement Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.GetSettlementsResponse
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/accounts/settlements [post]
func (h *Handler) GetSettlements(c *gin.Context) {
	var req pb.GetSettlementsRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetSettlements(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetMargin godoc
//
//	@Summary		Get Margin
//	@Description	Get margin information
//	@Tags			Account
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetMarginRequest	true	"Margin Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.Margin
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/accounts/margin [post]
func (h *Handler) GetMargin(c *gin.Context) {
	var req pb.GetMarginRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetMargin(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// GetTradingLimits godoc
//
//	@Summary		Get Trading Limits
//	@Description	Get trading limits information
//	@Tags			Account
//	@Accept			json
//	@Produce		json
//	@Param			request	body	pb.GetTradingLimitsRequest	true	"Trading Limits Request"
//	@Security		Bearer
//	@Success		200	{object}	pb.TradingLimits
//	@Failure		400	{object}	APIError
//	@Failure		500	{object}	APIError
//	@Router			/api/v1/accounts/limits [post]
func (h *Handler) GetTradingLimits(c *gin.Context) {
	var req pb.GetTradingLimitsRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.GetTradingLimits(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}
