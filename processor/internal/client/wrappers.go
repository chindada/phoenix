package client

import (
	"context"

	"google.golang.org/grpc"

	"phoenix/processor/pkg/pb"
)

func (c *Client) Login(ctx context.Context, in *pb.LoginRequest, opts ...grpc.CallOption) (*pb.LoginResponse, error) {
	return c.getNextClient().Login(ctx, in, opts...)
}

func (c *Client) Logout(ctx context.Context, in *pb.Empty, opts ...grpc.CallOption) (*pb.LogoutResponse, error) {
	return c.getNextClient().Logout(ctx, in, opts...)
}

func (c *Client) GetUsage(ctx context.Context, in *pb.Empty, opts ...grpc.CallOption) (*pb.UsageStatus, error) {
	return c.getNextClient().GetUsage(ctx, in, opts...)
}

func (c *Client) ListAccounts(
	ctx context.Context,
	in *pb.Empty,
	opts ...grpc.CallOption,
) (*pb.ListAccountsResponse, error) {
	return c.getNextClient().ListAccounts(ctx, in, opts...)
}

func (c *Client) GetAccountBalance(
	ctx context.Context,
	in *pb.Empty,
	opts ...grpc.CallOption,
) (*pb.AccountBalance, error) {
	return c.getNextClient().GetAccountBalance(ctx, in, opts...)
}

func (c *Client) PlaceOrder(ctx context.Context, in *pb.PlaceOrderRequest, opts ...grpc.CallOption) (*pb.Trade, error) {
	return c.getNextClient().PlaceOrder(ctx, in, opts...)
}

func (c *Client) PlaceComboOrder(
	ctx context.Context,
	in *pb.PlaceComboOrderRequest,
	opts ...grpc.CallOption,
) (*pb.ComboTrade, error) {
	return c.getNextClient().PlaceComboOrder(ctx, in, opts...)
}

func (c *Client) UpdateOrder(
	ctx context.Context,
	in *pb.UpdateOrderRequest,
	opts ...grpc.CallOption,
) (*pb.Trade, error) {
	return c.getNextClient().UpdateOrder(ctx, in, opts...)
}

func (c *Client) CancelOrder(
	ctx context.Context,
	in *pb.CancelOrderRequest,
	opts ...grpc.CallOption,
) (*pb.Trade, error) {
	return c.getNextClient().CancelOrder(ctx, in, opts...)
}

func (c *Client) CancelComboOrder(
	ctx context.Context,
	in *pb.CancelComboOrderRequest,
	opts ...grpc.CallOption,
) (*pb.ComboTrade, error) {
	return c.getNextClient().CancelComboOrder(ctx, in, opts...)
}

func (c *Client) UpdateStatus(
	ctx context.Context,
	in *pb.UpdateStatusRequest,
	opts ...grpc.CallOption,
) (*pb.Empty, error) {
	return c.getNextClient().UpdateStatus(ctx, in, opts...)
}

func (c *Client) UpdateComboStatus(
	ctx context.Context,
	in *pb.UpdateStatusRequest,
	opts ...grpc.CallOption,
) (*pb.Empty, error) {
	return c.getNextClient().UpdateComboStatus(ctx, in, opts...)
}

func (c *Client) ListTrades(
	ctx context.Context,
	in *pb.Empty,
	opts ...grpc.CallOption,
) (*pb.ListTradesResponse, error) {
	return c.getNextClient().ListTrades(ctx, in, opts...)
}

func (c *Client) ListComboTrades(
	ctx context.Context,
	in *pb.Empty,
	opts ...grpc.CallOption,
) (*pb.ListComboTradesResponse, error) {
	return c.getNextClient().ListComboTrades(ctx, in, opts...)
}

func (c *Client) GetOrderDealRecords(
	ctx context.Context,
	in *pb.GetOrderDealRecordsRequest,
	opts ...grpc.CallOption,
) (*pb.GetOrderDealRecordsResponse, error) {
	return c.getNextClient().GetOrderDealRecords(ctx, in, opts...)
}

func (c *Client) ListPositions(
	ctx context.Context,
	in *pb.ListPositionsRequest,
	opts ...grpc.CallOption,
) (*pb.ListPositionsResponse, error) {
	return c.getNextClient().ListPositions(ctx, in, opts...)
}

func (c *Client) ListPositionDetail(
	ctx context.Context,
	in *pb.ListPositionDetailRequest,
	opts ...grpc.CallOption,
) (*pb.ListPositionDetailResponse, error) {
	return c.getNextClient().ListPositionDetail(ctx, in, opts...)
}

func (c *Client) ListProfitLoss(
	ctx context.Context,
	in *pb.ListProfitLossRequest,
	opts ...grpc.CallOption,
) (*pb.ListProfitLossResponse, error) {
	return c.getNextClient().ListProfitLoss(ctx, in, opts...)
}

func (c *Client) ListProfitLossDetail(
	ctx context.Context,
	in *pb.ListProfitLossDetailRequest,
	opts ...grpc.CallOption,
) (*pb.ListProfitLossDetailResponse, error) {
	return c.getNextClient().ListProfitLossDetail(ctx, in, opts...)
}

func (c *Client) ListProfitLossSummary(
	ctx context.Context,
	in *pb.ListProfitLossSummaryRequest,
	opts ...grpc.CallOption,
) (*pb.ListProfitLossSummaryResponse, error) {
	return c.getNextClient().ListProfitLossSummary(ctx, in, opts...)
}

func (c *Client) GetSettlements(
	ctx context.Context,
	in *pb.GetSettlementsRequest,
	opts ...grpc.CallOption,
) (*pb.GetSettlementsResponse, error) {
	return c.getNextClient().GetSettlements(ctx, in, opts...)
}

func (c *Client) ListSettlements(
	ctx context.Context,
	in *pb.GetSettlementsRequest,
	opts ...grpc.CallOption,
) (*pb.GetSettlementsResponse, error) {
	return c.getNextClient().ListSettlements(ctx, in, opts...)
}

func (c *Client) GetMargin(ctx context.Context, in *pb.GetMarginRequest, opts ...grpc.CallOption) (*pb.Margin, error) {
	return c.getNextClient().GetMargin(ctx, in, opts...)
}

func (c *Client) GetTradingLimits(
	ctx context.Context,
	in *pb.GetTradingLimitsRequest,
	opts ...grpc.CallOption,
) (*pb.TradingLimits, error) {
	return c.getNextClient().GetTradingLimits(ctx, in, opts...)
}

func (c *Client) GetStockReserveSummary(
	ctx context.Context,
	in *pb.GetStockReserveSummaryRequest,
	opts ...grpc.CallOption,
) (*pb.ReserveStocksSummaryResponse, error) {
	return c.getNextClient().GetStockReserveSummary(ctx, in, opts...)
}

func (c *Client) GetStockReserveDetail(
	ctx context.Context,
	in *pb.GetStockReserveDetailRequest,
	opts ...grpc.CallOption,
) (*pb.ReserveStocksDetailResponse, error) {
	return c.getNextClient().GetStockReserveDetail(ctx, in, opts...)
}

func (c *Client) ReserveStock(
	ctx context.Context,
	in *pb.ReserveStockRequest,
	opts ...grpc.CallOption,
) (*pb.ReserveStockResponse, error) {
	return c.getNextClient().ReserveStock(ctx, in, opts...)
}

func (c *Client) GetEarmarkingDetail(
	ctx context.Context,
	in *pb.GetEarmarkingDetailRequest,
	opts ...grpc.CallOption,
) (*pb.EarmarkStocksDetailResponse, error) {
	return c.getNextClient().GetEarmarkingDetail(ctx, in, opts...)
}

func (c *Client) ReserveEarmarking(
	ctx context.Context,
	in *pb.ReserveEarmarkingRequest,
	opts ...grpc.CallOption,
) (*pb.ReserveEarmarkingResponse, error) {
	return c.getNextClient().ReserveEarmarking(ctx, in, opts...)
}

func (c *Client) GetSnapshots(
	ctx context.Context,
	in *pb.GetSnapshotsRequest,
	opts ...grpc.CallOption,
) (*pb.GetSnapshotsResponse, error) {
	return c.getNextClient().GetSnapshots(ctx, in, opts...)
}

func (c *Client) GetTicks(ctx context.Context, in *pb.GetTicksRequest, opts ...grpc.CallOption) (*pb.Ticks, error) {
	return c.getNextClient().GetTicks(ctx, in, opts...)
}

func (c *Client) GetKbars(ctx context.Context, in *pb.GetKbarsRequest, opts ...grpc.CallOption) (*pb.Kbars, error) {
	return c.getNextClient().GetKbars(ctx, in, opts...)
}

func (c *Client) GetDailyQuotes(
	ctx context.Context,
	in *pb.GetDailyQuotesRequest,
	opts ...grpc.CallOption,
) (*pb.DailyQuotes, error) {
	return c.getNextClient().GetDailyQuotes(ctx, in, opts...)
}

func (c *Client) CreditEnquires(
	ctx context.Context,
	in *pb.CreditEnquiresRequest,
	opts ...grpc.CallOption,
) (*pb.CreditEnquiresResponse, error) {
	return c.getNextClient().CreditEnquires(ctx, in, opts...)
}

func (c *Client) GetShortStockSources(
	ctx context.Context,
	in *pb.GetShortStockSourcesRequest,
	opts ...grpc.CallOption,
) (*pb.GetShortStockSourcesResponse, error) {
	return c.getNextClient().GetShortStockSources(ctx, in, opts...)
}

func (c *Client) GetScanners(
	ctx context.Context,
	in *pb.GetScannersRequest,
	opts ...grpc.CallOption,
) (*pb.GetScannersResponse, error) {
	return c.getNextClient().GetScanners(ctx, in, opts...)
}

func (c *Client) GetPunish(ctx context.Context, in *pb.Empty, opts ...grpc.CallOption) (*pb.Punish, error) {
	return c.getNextClient().GetPunish(ctx, in, opts...)
}

func (c *Client) GetNotice(ctx context.Context, in *pb.Empty, opts ...grpc.CallOption) (*pb.Notice, error) {
	return c.getNextClient().GetNotice(ctx, in, opts...)
}

func (c *Client) FetchContracts(
	ctx context.Context,
	in *pb.FetchContractsRequest,
	opts ...grpc.CallOption,
) (*pb.Empty, error) {
	return c.getNextClient().FetchContracts(ctx, in, opts...)
}

func (c *Client) GetCAExpireTime(
	ctx context.Context,
	in *pb.GetCAExpireTimeRequest,
	opts ...grpc.CallOption,
) (*pb.GetCAExpireTimeResponse, error) {
	return c.getNextClient().GetCAExpireTime(ctx, in, opts...)
}

func (c *Client) SubscribeTrade(
	ctx context.Context,
	in *pb.SubscribeTradeRequest,
	opts ...grpc.CallOption,
) (*pb.SubscribeTradeResponse, error) {
	return c.getNextClient().SubscribeTrade(ctx, in, opts...)
}

func (c *Client) UnsubscribeTrade(
	ctx context.Context,
	in *pb.UnsubscribeTradeRequest,
	opts ...grpc.CallOption,
) (*pb.UnsubscribeTradeResponse, error) {
	return c.getNextClient().UnsubscribeTrade(ctx, in, opts...)
}
