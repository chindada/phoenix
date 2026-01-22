"""
provider.src.server -.
"""

import logging
import os
from concurrent import futures

import grpc
from shioaji import constant
from shioaji_client import ShioajiClient

try:
    import provider_pb2
    import provider_pb2_grpc
except ImportError as exc:
    raise ImportError(
        "Failed to import generated modules or ShioajiClient. "
        "Please ensure 'make codegen-py' has been run and 'provider/src' is in PYTHONPATH."
    ) from exc


class ShioajiService(provider_pb2_grpc.ShioajiProviderServicer):
    """
    ShioajiService -.
    """

    def __init__(self):
        # WARNING: This implementation is stateful and supports only a single user session.
        # It is not suitable for concurrent multi-user environments.
        self.client = ShioajiClient()
        self.logged_in = False

    def Login(self, request, _):
        """
        Login to the Shioaji API.
        """
        try:
            self.client.login(api_key=request.api_key, secret_key=request.secret_key)
            self.logged_in = True
            return provider_pb2.LoginResponse(success=True, message="Login successful")
        except Exception as e:
            return provider_pb2.LoginResponse(success=False, message=str(e))

    def ListAccounts(self, _, context):
        """
        List all accounts associated with the login.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")
        accounts = self.client.list_accounts()
        response_accounts = []
        for acc in accounts:
            response_accounts.append(
                provider_pb2.Account(
                    account_type=str(acc.account_type),
                    person_id=acc.person_id,
                    broker_id=acc.broker_id,
                    account_id=acc.account_id,
                    signed=acc.signed,
                    username=acc.username,
                )
            )
        return provider_pb2.ListAccountsResponse(accounts=response_accounts)

    def GetAccountBalance(self, _, context):
        """
        Get the balance of the default stock account.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")
        balance = self.client.account_balance()
        # balance is usually a single object, assume stock account balance for now
        return provider_pb2.AccountBalanceResponse(
            balance=float(balance.acc_balance), currency=balance.currency
        )

    def ListSettlements(self, _, context):
        """
        List settlements for the default stock account.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")
        settlements = self.client.settlements(self.client.stock_account)
        response_settlements = []
        for s in settlements:
            response_settlements.append(
                provider_pb2.Settlement(date=s.date, amount=float(s.amount), t_time=s.T)
            )
        return provider_pb2.ListSettlementsResponse(settlements=response_settlements)

    def ListProfitLoss(self, request, context):
        """
        List profit and loss.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")
        pnl_list = self.client.list_profit_loss(
            self.client.stock_account,
            begin_date=request.begin_date,
            end_date=request.end_date,
        )
        response_pnl = []
        for p in pnl_list:
            response_pnl.append(
                provider_pb2.ProfitLoss(
                    id=int(p.id),
                    code=p.code,
                    seqno=p.seqno,
                    dseq=p.dseq,
                    quantity=int(p.quantity),
                    price=float(p.price),
                    pnl=float(p.pnl),
                    pr_ratio=float(p.pr_ratio),
                    cond=str(p.cond),
                    date=p.date,
                )
            )
        return provider_pb2.ListProfitLossResponse(profit_loss=response_pnl)

    def ListPositions(self, _, context):
        """
        List current positions.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")
        positions = self.client.list_positions(self.client.stock_account)
        response_positions = []
        for p in positions:
            response_positions.append(
                provider_pb2.Position(
                    id=int(p.id),
                    code=p.code,
                    direction=str(p.direction),
                    quantity=int(p.quantity),
                    price=float(p.price),
                    last_price=float(p.last_price),
                    pnl=float(p.pnl),
                    cond=str(p.cond),
                    order_type=str(p.order_type),
                    price_type=str(p.price_type),
                )
            )
        return provider_pb2.ListPositionsResponse(positions=response_positions)

    def _get_contract(self, code, security_type):
        if security_type == "STK":
            return self.client.contracts.Stocks[code]
        if security_type == "FUT":
            return self.client.contracts.Futures[code]
        if security_type == "OPT":
            return self.client.contracts.Options[code]
        if security_type == "IDX":
            return self.client.contracts.Indexs[code]
        return None

    def PlaceOrder(self, request, context):
        """
        Place a new order.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")

        contract = self._get_contract(
            request.contract_code, request.contract_security_type
        )
        if not contract:
            context.abort(grpc.StatusCode.NOT_FOUND, "Contract not found")

        action = (
            constant.Action.Buy if request.action == "Buy" else constant.Action.Sell
        )
        price_type = (
            constant.StockPriceType.LMT
            if request.price_type == "LMT"
            else constant.StockPriceType.MKT
        )
        order_type = (
            constant.OrderType.ROD
            if request.order_type == "ROD"
            else (
                constant.OrderType.IOC
                if request.order_type == "IOC"
                else constant.OrderType.FOK
            )
        )

        # Determine order lot, handling potential enum differences or string input
        if request.order_lot == "IntradayOdd":
            order_lot = constant.StockOrderLot.IntradayOdd
        else:
            order_lot = constant.StockOrderLot.Common

        order = self.client.api.Order(
            price=request.price,
            quantity=request.quantity,
            action=action,
            price_type=price_type,
            order_type=order_type,
            order_lot=order_lot,
            account=self.client.stock_account,  # Default to stock account for now
        )

        trade = self.client.place_order(contract, order)

        return self._trade_to_proto(trade)

    def _find_trade(self, trade_id):
        self.client.update_status(self.client.stock_account)
        trades = self.client.list_trades()
        for trade in trades:
            # Check status.id first, then order.id as fallback
            if hasattr(trade, "status") and trade.status.id == trade_id:
                return trade
            if hasattr(trade, "order") and trade.order.id == trade_id:
                return trade
        return None

    def UpdateOrder(self, request, context):
        """
        Update an existing order.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")

        trade = self._find_trade(request.trade_id)
        if not trade:
            context.abort(grpc.StatusCode.NOT_FOUND, "Trade not found")
            return provider_pb2.TradeResponse()

        try:
            # Only pass arguments that are set (non-zero/non-empty)
            kwargs = {}
            if request.price:
                kwargs["price"] = request.price
            if request.quantity:
                kwargs["quantity"] = request.quantity

            updated_trade = self.client.update_order(trade, **kwargs)
            return self._trade_to_proto(updated_trade)
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.TradeResponse()

    def CancelOrder(self, request, context):
        """
        Cancel an existing order.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")

        trade = self._find_trade(request.trade_id)
        if not trade:
            context.abort(grpc.StatusCode.NOT_FOUND, "Trade not found")
            return provider_pb2.TradeResponse()

        try:
            self.client.cancel_order(trade)
            # Fetch updated status for the trade
            self.client.update_status(self.client.stock_account)
            # Return the trade (now cancelled)
            return self._trade_to_proto(trade)
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.TradeResponse()

    def ListTrades(self, _, context):
        """
        List all trades.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")
        trades = self.client.list_trades()
        response_trades = [self._trade_to_proto_msg(t) for t in trades]
        return provider_pb2.ListTradesResponse(trades=response_trades)

    def UpdateStatus(self, _, context):
        """
        Update local status from server.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")
        self.client.update_status(self.client.stock_account)
        return provider_pb2.Empty()

    def GetTicks(self, request, context):
        """
        GetTicks -.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")
        contract = self._get_contract(
            request.contract_code, request.contract_security_type
        )
        if not contract:
            context.abort(grpc.StatusCode.NOT_FOUND, "Contract not found")

        ticks = self.client.ticks(contract, date=request.date)
        response_ticks = []
        # Ticks structure is complex (DataFrame like), iteration needs care.
        # This is a simplified iteration assuming it returns a list-like object of objects
        for i, ts in enumerate(ticks.ts):
            response_ticks.append(
                provider_pb2.Tick(
                    code=request.contract_code,
                    datetime=str(ts),
                    open=float(ticks.open[i]),
                    close=float(ticks.close[i]),
                    high=float(ticks.high[i]),
                    low=float(ticks.low[i]),
                    volume=int(ticks.volume[i]),
                )
            )
        return provider_pb2.GetTicksResponse(ticks=response_ticks)

    def GetKbars(self, request, context):
        """
        Get K-Bars (candlestick data).
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")
        contract = self._get_contract(
            request.contract_code, request.contract_security_type
        )
        if not contract:
            context.abort(grpc.StatusCode.NOT_FOUND, "Contract not found")

        kbars = self.client.kbars(
            contract, start=request.start_date, end=request.end_date
        )
        response_kbars = []
        for i, ts in enumerate(kbars.ts):
            response_kbars.append(
                provider_pb2.Kbar(
                    ts=int(ts),
                    open=float(kbars.Open[i]),
                    high=float(kbars.High[i]),
                    low=float(kbars.Low[i]),
                    close=float(kbars.Close[i]),
                    volume=int(kbars.Volume[i]),
                    amount=float(kbars.Amount[i]),
                )
            )
        return provider_pb2.GetKbarsResponse(kbars=response_kbars)

    def GetSnapshots(self, request, context):
        """
        GetSnapshots -.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")
        contracts = []
        for code in request.contract_codes:
            # Assuming stocks for now, logic to detect type needed or passed in request
            c = self.client.contracts.Stocks[code]
            if c:
                contracts.append(c)

        snapshots = self.client.snapshots(contracts)
        response_snapshots = []
        for s in snapshots:
            response_snapshots.append(
                provider_pb2.Snapshot(
                    ts=s.ts,
                    code=s.code,
                    exchange=s.exchange,
                    open=s.open,
                    high=s.high,
                    low=s.low,
                    close=s.close,
                    average_price=s.average_price,
                    volume=s.volume,
                    total_volume=s.total_volume,
                    amount=s.amount,
                    total_amount=s.total_amount,
                    price_change=s.price_change,
                    price_change_percent=s.price_change_percent,
                    buy_price=s.buy_price,
                    buy_volume=s.buy_volume,
                    sell_price=s.sell_price,
                    sell_volume=s.sell_volume,
                )
            )
        return provider_pb2.GetSnapshotsResponse(snapshots=response_snapshots)

    def SubscribeQuote(self, request, context):
        """
        SubscribeQuote -.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")
        contract = self._get_contract(
            request.contract_code, request.contract_security_type
        )
        if not contract:
            context.abort(grpc.StatusCode.NOT_FOUND, "Contract not found")

        quote_type = (
            constant.QuoteType.Tick
            if request.quote_type == "tick"
            else constant.QuoteType.BidAsk
        )
        self.client.subscribe_quote(contract, quote_type=quote_type)
        return provider_pb2.Empty()

    def UnsubscribeQuote(self, request, context):
        """
        UnsubscribeQuote -.
        """
        if not self.logged_in:
            context.abort(grpc.StatusCode.UNAUTHENTICATED, "Not logged in")
        contract = self._get_contract(
            request.contract_code, request.contract_security_type
        )
        if not contract:
            context.abort(grpc.StatusCode.NOT_FOUND, "Contract not found")

        quote_type = (
            constant.QuoteType.Tick
            if request.quote_type == "tick"
            else constant.QuoteType.BidAsk
        )
        self.client.unsubscribe_quote(contract, quote_type=quote_type)
        return provider_pb2.Empty()

    def _trade_to_proto(self, trade):
        # Helper to convert Shioaji Trade object to Proto Trade Response
        # Note: Actual Shioaji Trade object fields might vary slightly, adjustment needed based on runtime inspection
        return provider_pb2.TradeResponse(trade=self._trade_to_proto_msg(trade))

    def _trade_to_proto_msg(self, trade):
        return provider_pb2.Trade(
            id=trade.status.id,  # Use status.id as the primary ID
            status=trade.status.status,
            price=float(trade.order.price),
            quantity=int(trade.order.quantity),
            filled_quantity=int(trade.status.deal_quantity),
            ordno=trade.order.ordno,
            # Populate other fields as available
        )


def serve():
    port = os.getenv("PORT", "50051")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    provider_pb2_grpc.add_ShioajiProviderServicer_to_server(ShioajiService(), server)
    server.add_insecure_port("[::]:" + port)
    logging.info("Server started, listening on %s", port)
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
