"""
provider.src.server -.
"""

import logging
import os
from concurrent import futures

import grpc
from shioaji_client import ShioajiClient
import shioaji as sj

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
        # This is a simplification. Real implementation needs to look up contract from client.contracts
        # or construct a proper object.
        # Assuming we can find it by code and security_type
        if proto_contract.security_type == "Stock":
             return self.client.api.Contracts.Stocks[proto_contract.code]
        elif proto_contract.security_type == "Future":
             return self.client.api.Contracts.Futures[proto_contract.code]
        elif proto_contract.security_type == "Option":
             return self.client.api.Contracts.Options[proto_contract.code]
        # Fallback or strict lookup
        return self.client.api.Contracts.Stocks[proto_contract.code]

    # Helper to convert proto Order to Shioaji Order
    def _to_sj_order(self, proto_order):
        return self.client.api.Order(
            price=proto_order.price,
            quantity=proto_order.quantity,
            action=proto_order.action,
            price_type=proto_order.price_type,
            order_type=proto_order.order_type,
            # Account mapping needed
        )

    def PlaceOrder(self, request, context):
        """Place a new order."""
        try:
            contract = self._to_sj_contract(request.contract)
            order = self._to_sj_order(request.order)
            trade = self.client.place_order(contract, order)
            # Convert trade back to proto Trade (simplified)
            return provider_pb2.Trade() 
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    # ... Continuing with other methods, implementing a few key ones fully ...

    def ListTrades(self, request, context):
        try:
            trades = self.client.list_trades()
            return provider_pb2.ListTradesResponse(trades=[]) # Need conversion
        except Exception as e:
            context.abort(grpc.StatusCode.INTERNAL, str(e))

    # Placeholder implementations for the rest to make it runnable
    def PlaceComboOrder(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def UpdateOrder(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def CancelOrder(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def CancelComboOrder(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def UpdateStatus(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def UpdateComboStatus(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def ListComboTrades(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetOrderDealRecords(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def ListPositions(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def ListPositionDetail(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def ListProfitLoss(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def ListProfitLossDetail(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def ListProfitLossSummary(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetSettlements(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def ListSettlements(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetMargin(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetTradingLimits(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetStockReserveSummary(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetStockReserveDetail(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def ReserveStock(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetEarmarkingDetail(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def ReserveEarmarking(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetSnapshots(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetTicks(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetKbars(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetDailyQuotes(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def CreditEnquires(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetShortStockSources(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetScanners(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetPunish(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetNotice(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def FetchContracts(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def ActivateCA(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def GetCAExpireTime(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def SubscribeTrade(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")
    def UnsubscribeTrade(self, request, context): context.abort(grpc.StatusCode.UNIMPLEMENTED, "Not implemented")


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