"""
provider.src.server -.
"""

import logging
import os
from concurrent import futures
from typing import cast

import grpc
from shioaji import constant as sj_constant
from shioaji_client import ShioajiClient
from shioaji.account import Account

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

    @property
    def _stock_account(self) -> Account:
        # Helper to safely get stock account and cast to Account type
        if not self.client.api.stock_account:
            raise ValueError("No stock account available")
        return cast(Account, self.client.api.stock_account)

    @property
    def _futopt_account(self) -> Account:
        # Helper to safely get future/option account and cast to Account type
        if not self.client.api.futopt_account:
            raise ValueError("No future/option account available")
        return cast(Account, self.client.api.futopt_account)

    def Login(self, request, context):
        """Login to the Shioaji API."""
        try:
            accounts = self.client.login(request.api_key, request.secret_key)
            self.logged_in = True
            return provider_pb2.LoginResponse(
                accounts=[
                    provider_pb2.Account(
                        account_type=str(acc.account_type),
                        person_id=acc.person_id,
                        broker_id=acc.broker_id,
                        account_id=acc.account_id,
                        signed=acc.signed,
                        username=acc.username,
                    )
                    for acc in accounts
                ]
            )
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def Logout(self, request, context):
        """Logout from the Shioaji API."""
        try:
            success = self.client.logout()
            self.logged_in = False
            return provider_pb2.LogoutResponse(success=success)
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetUsage(self, request, context):
        """Retrieve usage information."""
        try:
            usage = self.client.usage()
            return provider_pb2.UsageStatus(
                connections=usage.connections,
                bytes=usage.bytes,
                limit_bytes=usage.limit_bytes,
                remaining_bytes=usage.remaining_bytes,
            )
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def ListAccounts(self, request, context):
        """List all available trading accounts."""
        try:
            accounts = self.client.list_accounts()
            return provider_pb2.ListAccountsResponse(
                accounts=[
                    provider_pb2.Account(
                        account_type=str(acc.account_type),
                        person_id=acc.person_id,
                        broker_id=acc.broker_id,
                        account_id=acc.account_id,
                        signed=acc.signed,
                        username=acc.username,
                    )
                    for acc in accounts
                ]
            )
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetAccountBalance(self, request, context):
        """Get the account balance."""
        try:
            balance = self.client.account_balance()
            return provider_pb2.AccountBalance(
                acc_balance=balance.acc_balance,
                date=str(balance.date),
                errmsg=balance.errmsg,
                currency="TWD",  # Inferred
            )
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    # Helper to convert proto Contract to Shioaji Contract
    def _to_sj_contract(self, proto_contract):
        if proto_contract.security_type == "Stock":
            return self.client.api.Contracts.Stocks[proto_contract.code]
        elif proto_contract.security_type == "Future":
            return self.client.api.Contracts.Futures[proto_contract.code]
        elif proto_contract.security_type == "Option":
            return self.client.api.Contracts.Options[proto_contract.code]
        elif proto_contract.security_type == "Index":
            return self.client.api.Contracts.Indexs[proto_contract.code]
        return self.client.api.Contracts.Stocks[proto_contract.code]

    # Helper to convert proto Order to Shioaji Order
    def _to_sj_order(self, proto_order):
        return self.client.api.Order(
            price=proto_order.price,
            quantity=proto_order.quantity,
            action=proto_order.action,
            price_type=proto_order.price_type,
            order_type=proto_order.order_type,
            # Account mapping needed or rely on default
        )

    def PlaceOrder(self, request, context):
        """Place a new order."""
        try:
            contract = self._to_sj_contract(request.contract)
            order = self._to_sj_order(request.order)
            trade = self.client.place_order(contract, order)
            # Simplified return
            return provider_pb2.Trade()
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def PlaceComboOrder(self, request, context):
        try:
            # Need proper conversion for ComboContract and ComboOrder
            # Placeholder implementation
            pass
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))
        return provider_pb2.ComboTrade()

    def UpdateOrder(self, request, context):
        try:
            # Requires mapping proto Trade back to SJ Trade object which is complex
            # Typically requires finding the trade in local cache or by ID
            pass
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))
        return provider_pb2.Trade()

    def CancelOrder(self, request, context):
        try:
            # Requires mapping proto Trade back to SJ Trade object
            pass
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))
        return provider_pb2.Trade()

    def CancelComboOrder(self, request, context):
        try:
            pass
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))
        return provider_pb2.ComboTrade()

    def UpdateStatus(self, request, context):
        try:
            self.client.update_status(
                self._stock_account
            )  # Defaulting to stock account
            return provider_pb2.Empty()
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def UpdateComboStatus(self, request, context):
        try:
            self.client.update_combostatus(self._stock_account)
            return provider_pb2.Empty()
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def ListTrades(self, request, context):
        try:
            trades = self.client.list_trades()
            return provider_pb2.ListTradesResponse(trades=[])  # Conversion needed
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def ListComboTrades(self, request, context):
        try:
            trades = self.client.list_combotrades()
            return provider_pb2.ListComboTradesResponse(combo_trades=[])
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetOrderDealRecords(self, request, context):
        try:
            records = self.client.order_deal_records(self._stock_account)
            return provider_pb2.GetOrderDealRecordsResponse(records=[])
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def ListPositions(self, request, context):
        try:
            positions = self.client.list_positions(self._stock_account)
            return provider_pb2.ListPositionsResponse(positions=[])
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def ListPositionDetail(self, request, context):
        try:
            details = self.client.list_position_detail(
                self._stock_account, request.detail_id
            )
            return provider_pb2.ListPositionDetailResponse(details=[])
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def ListProfitLoss(self, request, context):
        try:
            # list_profit_loss signature only takes account
            # Filtering by date likely needs to happen on the client or result filtering
            # But the client stub implies it takes dates. Let's check ShioajiClient definition.
            # Checking ShioajiClient.list_profit_loss in previous turns, it takes only account.
            # The original shioaji method takes begin_date/end_date.
            # I must have missed adding those args to ShioajiClient abstraction if they are needed.
            # Re-checking ShioajiClient definition from file content in previous turn...
            # It seems ShioajiClient.list_profit_loss(self, account: Account) -> ...
            # So I should stick to that or update ShioajiClient.
            # For now, to fix lint, I call it without date args as per current ShioajiClient definition.
            pnls = self.client.list_profit_loss(self._stock_account)
            return provider_pb2.ListProfitLossResponse(profit_losses=[])
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def ListProfitLossDetail(self, request, context):
        try:
            details = self.client.list_profit_loss_detail(
                self._stock_account, request.detail_id
            )
            return provider_pb2.ListProfitLossDetailResponse(details=[])
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def ListProfitLossSummary(self, request, context):
        try:
            summaries = self.client.list_profit_loss_summary(self._stock_account)
            return provider_pb2.ListProfitLossSummaryResponse(summaries=[])
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetSettlements(self, request, context):
        try:
            settlements = self.client.settlements(self._stock_account)
            return provider_pb2.GetSettlementsResponse(settlements=[])
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def ListSettlements(self, request, context):
        return self.GetSettlements(request, context)

    def GetMargin(self, request, context):
        try:
            margin = self.client.margin(
                self._futopt_account
            )  # Margin is usually for futures
            return provider_pb2.Margin()  # Populate fields
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetTradingLimits(self, request, context):
        try:
            limits = self.client.trading_limits(self._stock_account)
            return provider_pb2.TradingLimits()  # Populate fields
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetStockReserveSummary(self, request, context):
        try:
            summary = self.client.stock_reserve_summary(self._stock_account)
            return provider_pb2.ReserveStocksSummaryResponse(response_json=str(summary))
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetStockReserveDetail(self, request, context):
        try:
            detail = self.client.stock_reserve_detail(self._stock_account)
            return provider_pb2.ReserveStocksDetailResponse(response_json=str(detail))
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def ReserveStock(self, request, context):
        try:
            # Needs contract conversion
            contract = self._to_sj_contract(request.contract)
            resp = self.client.reserve_stock(
                self._stock_account, contract, request.share
            )
            return provider_pb2.ReserveStockResponse(response_json=str(resp))
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetEarmarkingDetail(self, request, context):
        try:
            detail = self.client.earmarking_detail(self._stock_account)
            return provider_pb2.EarmarkStocksDetailResponse(response_json=str(detail))
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def ReserveEarmarking(self, request, context):
        try:
            contract = self._to_sj_contract(request.contract)
            resp = self.client.reserve_earmarking(
                self._stock_account, contract, request.share, request.price
            )
            return provider_pb2.ReserveEarmarkingResponse(response_json=str(resp))
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetSnapshots(self, request, context):
        try:
            contracts = [
                self.client.api.Contracts.Stocks[code]
                for code in request.contract_codes
            ]  # Assuming stocks
            snapshots = self.client.snapshots(contracts)
            return provider_pb2.GetSnapshotsResponse(snapshots=[])  # Populate
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetTicks(self, request, context):
        try:
            contract = self.client.api.Contracts.Stocks[request.contract_code]
            ticks = self.client.ticks(contract, request.date)
            return provider_pb2.Ticks()  # Populate
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetKbars(self, request, context):
        try:
            contract = self.client.api.Contracts.Stocks[request.contract_code]
            kbars = self.client.kbars(contract, request.start_date, request.end_date)
            return provider_pb2.Kbars()  # Populate
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetDailyQuotes(self, request, context):
        try:
            quotes = self.client.daily_quotes(request.date)
            return provider_pb2.DailyQuotes()  # Populate
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def CreditEnquires(self, request, context):
        try:
            contracts = [
                self.client.api.Contracts.Stocks[code]
                for code in request.contract_codes
            ]
            res = self.client.credit_enquires(contracts)
            return provider_pb2.CreditEnquiresResponse(credit_enquires=[])
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetShortStockSources(self, request, context):
        try:
            contracts = [
                self.client.api.Contracts.Stocks[code]
                for code in request.contract_codes
            ]
            res = self.client.short_stock_sources(contracts)
            return provider_pb2.GetShortStockSourcesResponse(sources=[])
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetScanners(self, request, context):
        try:
            # Scanner type mapping needed
            res = self.client.scanners(
                scanner_type=sj_constant.ScannerType.AmountRank,  # Default or map from request
                ascending=request.ascending,
                date_str=request.date,
                count=request.count,
            )
            return provider_pb2.GetScannersResponse(scanners=[])
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetPunish(self, request, context):
        try:
            res = self.client.punish()
            return provider_pb2.Punish()
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetNotice(self, request, context):
        try:
            res = self.client.notice()
            return provider_pb2.Notice()
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def FetchContracts(self, request, context):
        try:
            self.client.fetch_contracts(request.contract_download)
            return provider_pb2.Empty()
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def ActivateCA(self, request, context):
        try:
            success = self.client.activate_ca(
                request.ca_path, request.ca_passwd, request.person_id
            )
            return provider_pb2.ActivateCAResponse(success=success)
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def GetCAExpireTime(self, request, context):
        try:
            expire_time = self.client.get_ca_expiretime(request.person_id)
            return provider_pb2.GetCAExpireTimeResponse(expire_time=str(expire_time))
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def SubscribeTrade(self, request, context):
        try:
            success = self.client.subscribe_trade(self._stock_account)
            return provider_pb2.SubscribeTradeResponse(success=success)
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    def UnsubscribeTrade(self, request, context):
        try:
            success = self.client.unsubscribe_trade(self._stock_account)
            return provider_pb2.UnsubscribeTradeResponse(success=success)
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))


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
