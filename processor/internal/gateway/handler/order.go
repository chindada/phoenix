package handler

import (
	"net/http"

	"github.com/gin-gonic/gin"

	"phoenix/processor/internal/gateway/middleware"
	"phoenix/processor/pkg/pb"
)

// PlaceOrder godoc
// @Summary      Place a new order
// @Description  Submit a buy or sell order to the provider
// @Tags         Order
// @Accept       json
// @Produce      json
// @Param        request body pb.PlaceOrderRequest true "Order Details"
// @Security     Bearer
// @Success      200  {object}  pb.OrderResponse
// @Failure      400  {object}  APIError
// @Failure      401  {object}  APIError
// @Failure      500  {object}  APIError
// @Router       /api/v1/orders [post]
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

// PlaceComboOrder godoc
// @Summary      Place a new combo order
// @Description  Submit a multi-leg combo order to the provider
// @Tags         Order
// @Accept       json
// @Produce      json
// @Param        request body pb.PlaceComboOrderRequest true "Combo Order Details"
// @Security     Bearer
// @Success      200  {object}  pb.OrderResponse
// @Failure      400  {object}  APIError
// @Failure      401  {object}  APIError
// @Failure      500  {object}  APIError
// @Router       /api/v1/orders/combo [post]
func (h *Handler) PlaceComboOrder(c *gin.Context) {
	var req pb.PlaceComboOrderRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.PlaceComboOrder(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// UpdateOrder godoc
// @Summary      Update an existing order
// @Description  Modify the price or quantity of an open order
// @Tags         Order
// @Accept       json
// @Produce      json
// @Param        request body pb.UpdateOrderRequest true "Update Order Details"
// @Security     Bearer
// @Success      200  {object}  pb.OrderResponse
// @Failure      400  {object}  APIError
// @Failure      401  {object}  APIError
// @Failure      500  {object}  APIError
// @Router       /api/v1/orders [put]
func (h *Handler) UpdateOrder(c *gin.Context) {
	var req pb.UpdateOrderRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.UpdateOrder(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// CancelOrder godoc
// @Summary      Cancel an existing order
// @Description  Cancel a single open order
// @Tags         Order
// @Accept       json
// @Produce      json
// @Param        request body pb.CancelOrderRequest true "Cancel Order Details"
// @Security     Bearer
// @Success      200  {object}  pb.OrderResponse
// @Failure      400  {object}  APIError
// @Failure      401  {object}  APIError
// @Failure      500  {object}  APIError
// @Router       /api/v1/orders/cancel [post]
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

// CancelComboOrder godoc
// @Summary      Cancel an existing combo order
// @Description  Cancel a multi-leg combo order
// @Tags         Order
// @Accept       json
// @Produce      json
// @Param        request body pb.CancelComboOrderRequest true "Cancel Combo Order Details"
// @Security     Bearer
// @Success      200  {object}  pb.OrderResponse
// @Failure      400  {object}  APIError
// @Failure      401  {object}  APIError
// @Failure      500  {object}  APIError
// @Router       /api/v1/orders/combo/cancel [post]
func (h *Handler) CancelComboOrder(c *gin.Context) {
	var req pb.CancelComboOrderRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.CancelComboOrder(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// UpdateStatus godoc
// @Summary      Update order status
// @Description  Manually trigger a status update for an order
// @Tags         Order
// @Accept       json
// @Produce      json
// @Param        request body pb.UpdateStatusRequest true "Status Update Details"
// @Security     Bearer
// @Success      200  {object}  pb.OrderResponse
// @Failure      400  {object}  APIError
// @Failure      401  {object}  APIError
// @Failure      500  {object}  APIError
// @Router       /api/v1/orders/status [post]
func (h *Handler) UpdateStatus(c *gin.Context) {
	var req pb.UpdateStatusRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.UpdateStatus(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}

// UpdateComboStatus godoc
// @Summary      Update combo order status
// @Description  Manually trigger a status update for a combo order
// @Tags         Order
// @Accept       json
// @Produce      json
// @Param        request body pb.UpdateStatusRequest true "Combo Status Update Details"
// @Security     Bearer
// @Success      200  {object}  pb.OrderResponse
// @Failure      400  {object}  APIError
// @Failure      401  {object}  APIError
// @Failure      500  {object}  APIError
// @Router       /api/v1/orders/combo/status [post]
func (h *Handler) UpdateComboStatus(c *gin.Context) {
	var req pb.UpdateStatusRequest
	if err := middleware.Bind(c, &req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	resp, err := h.client.UpdateComboStatus(c.Request.Context(), &req)
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	middleware.Render(c, http.StatusOK, resp)
}
