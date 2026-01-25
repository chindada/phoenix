"""
provider.src.server -.
"""

import logging
import os
import signal
from concurrent import futures
from datetime import datetime
from typing import Any, Optional, cast

import grpc
from shioaji import constant as sj_constant
from shioaji.account import Account
from shioaji.contracts import ComboBase, ComboContract, Contract
from shioaji.order import (
    ComboOrder,
    ComboTrade,
    Order,
    OrderDealRecords,
    OrderStatus,
    Trade,
)
from shioaji.position import (
    FuturePosition,
    FuturePositionDetail,
    FutureProfitDetail,
    FutureProfitLoss,
    FutureProfitLossSummary,
    StockPosition,
    StockPositionDetail,
    StockProfitDetail,
    StockProfitLoss,
    StockProfitLossSummary,
)
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

    _SECURITY_TYPE_MAP = {
        sj_constant.SecurityType.Index: provider_pb2.SECURITY_TYPE_IND,
        sj_constant.SecurityType.Stock: provider_pb2.SECURITY_TYPE_STK,
        sj_constant.SecurityType.Future: provider_pb2.SECURITY_TYPE_FUT,
        sj_constant.SecurityType.Option: provider_pb2.SECURITY_TYPE_OPT,
    }

    _EXCHANGE_MAP = {
        sj_constant.Exchange.TSE: provider_pb2.EXCHANGE_TSE,
        sj_constant.Exchange.OTC: provider_pb2.EXCHANGE_OTC,
        sj_constant.Exchange.OES: provider_pb2.EXCHANGE_OES,
        sj_constant.Exchange.TAIFEX: provider_pb2.EXCHANGE_TAIFEX,
    }

    _CURRENCY_MAP = {
        sj_constant.Currency.TWD: provider_pb2.CURRENCY_TWD,
        sj_constant.Currency.USD: provider_pb2.CURRENCY_USD,
        sj_constant.Currency.HKD: provider_pb2.CURRENCY_HKD,
        sj_constant.Currency.GBP: provider_pb2.CURRENCY_GBP,
        sj_constant.Currency.AUD: provider_pb2.CURRENCY_AUD,
        sj_constant.Currency.CAD: provider_pb2.CURRENCY_CAD,
        sj_constant.Currency.SGD: provider_pb2.CURRENCY_SGD,
        sj_constant.Currency.CHF: provider_pb2.CURRENCY_CHF,
        sj_constant.Currency.JPY: provider_pb2.CURRENCY_JPY,
        sj_constant.Currency.ZAR: provider_pb2.CURRENCY_ZAR,
        sj_constant.Currency.SEK: provider_pb2.CURRENCY_SEK,
        sj_constant.Currency.NZD: provider_pb2.CURRENCY_NZD,
        sj_constant.Currency.THB: provider_pb2.CURRENCY_THB,
        sj_constant.Currency.PHP: provider_pb2.CURRENCY_PHP,
        sj_constant.Currency.IDR: provider_pb2.CURRENCY_IDR,
        sj_constant.Currency.EUR: provider_pb2.CURRENCY_EUR,
        sj_constant.Currency.KRW: provider_pb2.CURRENCY_KRW,
        sj_constant.Currency.VND: provider_pb2.CURRENCY_VND,
        sj_constant.Currency.MYR: provider_pb2.CURRENCY_MYR,
        sj_constant.Currency.CNY: provider_pb2.CURRENCY_CNY,
    }

    _OPTION_RIGHT_MAP = {
        sj_constant.OptionRight.Call: provider_pb2.OPTION_RIGHT_CALL,
        sj_constant.OptionRight.Put: provider_pb2.OPTION_RIGHT_PUT,
    }

    _DAY_TRADE_MAP = {
        sj_constant.DayTrade.Yes: provider_pb2.DAY_TRADE_YES,
        sj_constant.DayTrade.OnlyBuy: provider_pb2.DAY_TRADE_ONLYBUY,
        sj_constant.DayTrade.No: provider_pb2.DAY_TRADE_NO,
    }

    _ACTION_MAP = {
        sj_constant.Action.Buy: provider_pb2.ACTION_BUY,
        sj_constant.Action.Sell: provider_pb2.ACTION_SELL,
    }

    _ORDER_TYPE_MAP = {
        sj_constant.OrderType.ROD: provider_pb2.ORDER_TYPE_ROD,
        sj_constant.OrderType.IOC: provider_pb2.ORDER_TYPE_IOC,
        sj_constant.OrderType.FOK: provider_pb2.ORDER_TYPE_FOK,
    }

    _STATUS_MAP = {
        sj_constant.Status.Cancelled: provider_pb2.STATUS_CANCELLED,
        sj_constant.Status.Filled: provider_pb2.STATUS_FILLED,
        sj_constant.Status.PartFilled: provider_pb2.STATUS_PARTFILLED,
        sj_constant.Status.Inactive: provider_pb2.STATUS_INACTIVE,
        sj_constant.Status.Failed: provider_pb2.STATUS_FAILED,
        sj_constant.Status.PendingSubmit: provider_pb2.STATUS_PENDINGSUBMIT,
        sj_constant.Status.PreSubmitted: provider_pb2.STATUS_PRESUBMITTED,
        sj_constant.Status.Submitted: provider_pb2.STATUS_SUBMITTED,
    }

    _TICK_TYPE_MAP = {
        sj_constant.TickType.No: provider_pb2.TICK_TYPE_NO,
        sj_constant.TickType.Buy: provider_pb2.TICK_TYPE_BUY,
        sj_constant.TickType.Sell: provider_pb2.TICK_TYPE_SELL,
    }

    _CHANGE_TYPE_MAP = {
        sj_constant.ChangeType.LimitUp: provider_pb2.CHANGE_TYPE_LIMITUP,
        sj_constant.ChangeType.Up: provider_pb2.CHANGE_TYPE_UP,
        sj_constant.ChangeType.Unchanged: provider_pb2.CHANGE_TYPE_UNCHANGED,
        sj_constant.ChangeType.Down: provider_pb2.CHANGE_TYPE_DOWN,
        sj_constant.ChangeType.LimitDown: provider_pb2.CHANGE_TYPE_LIMITDOWN,
    }

    _STOCK_ORDER_COND_MAP = {
        sj_constant.StockOrderCond.Cash: provider_pb2.STOCK_ORDER_COND_CASH,
        sj_constant.StockOrderCond.MarginTrading: provider_pb2.STOCK_ORDER_COND_MARGINTRADING,
        sj_constant.StockOrderCond.ShortSelling: provider_pb2.STOCK_ORDER_COND_SHORTSELLING,
    }

    _TRADE_TYPE_MAP = {
        sj_constant.TradeType.Common: provider_pb2.TRADE_TYPE_COMMON,
        sj_constant.TradeType.DayTrade: provider_pb2.TRADE_TYPE_DAYTRADE,
    }

    def __init__(self):
        self.client = ShioajiClient()
        self.logged_in = False

    def _get_enum(self, mapping: dict, value: Any) -> Any:
        """Helper to look up enum values safely."""
        if value is None:
            return 0
        return mapping.get(value, 0)

    def _safe_str(self, value: Any) -> str:
        """Helper to convert value to string safely, returning empty string if None."""
        return str(value) if value is not None else ""

    def _lookup_contract(self, code: str):
        """Helper to find a contract by code across all categories."""
        # Check if contracts are loaded; if not, they might need to be fetched,
        # but here we just check what's available in memory.
        if (
            hasattr(self.client.api.Contracts, "Stocks")
            and code in self.client.api.Contracts.Stocks
        ):
            return self.client.api.Contracts.Stocks[code]
        if (
            hasattr(self.client.api.Contracts, "Futures")
            and code in self.client.api.Contracts.Futures
        ):
            return self.client.api.Contracts.Futures[code]
        if (
            hasattr(self.client.api.Contracts, "Options")
            and code in self.client.api.Contracts.Options
        ):
            return self.client.api.Contracts.Options[code]
        if (
            hasattr(self.client.api.Contracts, "Indexs")
            and code in self.client.api.Contracts.Indexs
        ):
            return self.client.api.Contracts.Indexs[code]
        raise KeyError(f"Contract code not found: {code}")

    @property
    def _stock_account(self) -> Account:
        if not self.client.api.stock_account:
            raise ValueError("No stock account available")
        return cast(Account, self.client.api.stock_account)

    @property
    def _futopt_account(self) -> Account:
        if not self.client.api.futopt_account:
            raise ValueError("No future/option account available")
        return cast(Account, self.client.api.futopt_account)

    def Login(
        self, request: provider_pb2.LoginRequest, context: grpc.ServicerContext
    ) -> provider_pb2.LoginResponse:
        """Login to the Shioaji API."""
        try:
            # get current folder path
            current_folder = os.path.dirname(os.path.abspath(__file__))
            accounts = self.client.login(request.api_key, request.secret_key)
            activated = self.client.activate_ca(
                ca_path=os.path.join(current_folder, "..", "data", "ca.pfx"),
                person_id="F127522501",
                ca_passwd="F127522501",
            )
            if not activated:
                context.abort(grpc.StatusCode.UNAUTHENTICATED, "Invalid credentials")
                return provider_pb2.LoginResponse()
            logging.info("Login successful")

            self.logged_in = True
            return provider_pb2.LoginResponse(
                accounts=[self._to_pb_account(acc) for acc in accounts]
            )
        except Exception as e:
            logging.error("Error in Login: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.LoginResponse()

    def Logout(
        self, request: provider_pb2.Empty, context: grpc.ServicerContext
    ) -> provider_pb2.LogoutResponse:
        """Logout from the Shioaji API."""
        try:
            success = self.client.logout()
            self.logged_in = False
            return provider_pb2.LogoutResponse(success=success)
        except Exception as e:
            logging.error("Error in Logout: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.LogoutResponse()

    def GetUsage(
        self, request: provider_pb2.Empty, context: grpc.ServicerContext
    ) -> provider_pb2.UsageStatus:
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
            logging.error("Error in GetUsage: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.UsageStatus()

    def ListAccounts(
        self, request: provider_pb2.Empty, context: grpc.ServicerContext
    ) -> provider_pb2.ListAccountsResponse:
        """List all available trading accounts."""
        try:
            accounts = self.client.list_accounts()
            return provider_pb2.ListAccountsResponse(
                accounts=[self._to_pb_account(acc) for acc in accounts]
            )
        except Exception as e:
            logging.error("Error in ListAccounts: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ListAccountsResponse()

    def GetAccountBalance(
        self, request: provider_pb2.Empty, context: grpc.ServicerContext
    ) -> provider_pb2.AccountBalance:
        """Get the account balance."""
        try:
            balance = self.client.account_balance()
            return provider_pb2.AccountBalance(
                acc_balance=balance.acc_balance,
                date=str(balance.date),
                errmsg=balance.errmsg,
            )
        except Exception as e:
            logging.error("Error in GetAccountBalance: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.AccountBalance()

    def _to_pb_account(self, acc: Account):
        """Convert Shioaji Account to Protobuf Account."""
        return provider_pb2.Account(
            account_type=self._safe_str(acc.account_type),
            person_id=acc.person_id,
            broker_id=acc.broker_id,
            account_id=acc.account_id,
            username=acc.username,
            signed=getattr(acc, "signed", False),
        )

    def _to_pb_contract(self, contract: Contract):
        """Convert Shioaji Contract to Protobuf Contract."""
        return provider_pb2.Contract(
            security_type=self._get_enum(
                self._SECURITY_TYPE_MAP, contract.security_type
            ),
            exchange=self._get_enum(self._EXCHANGE_MAP, contract.exchange),
            code=contract.code,
            symbol=contract.symbol,
            name=contract.name,
            currency=self._get_enum(self._CURRENCY_MAP, contract.currency),
            category=self._safe_str(contract.category),
            delivery_month=self._safe_str(contract.delivery_month),
            delivery_date=self._safe_str(contract.delivery_date),
            strike_price=float(contract.strike_price),
            option_right=self._get_enum(self._OPTION_RIGHT_MAP, contract.option_right),
            underlying_kind=self._safe_str(contract.underlying_kind),
            underlying_code=self._safe_str(contract.underlying_code),
            unit=float(contract.unit),
            multiplier=int(contract.multiplier) if contract.multiplier else 0,
            limit_up=contract.limit_up,
            limit_down=contract.limit_down,
            reference=contract.reference,
            update_date=self._safe_str(contract.update_date),
            margin_trading_balance=contract.margin_trading_balance,
            short_selling_balance=contract.short_selling_balance,
            day_trade=self._get_enum(self._DAY_TRADE_MAP, contract.day_trade),
            target_code=self._safe_str(contract.target_code),
        )

    def _to_pb_combo_base(self, combo_base):
        """Convert Shioaji ComboBase to Protobuf ComboBase."""
        return provider_pb2.ComboBase(
            security_type=self._get_enum(
                self._SECURITY_TYPE_MAP, combo_base.security_type
            ),
            exchange=self._get_enum(self._EXCHANGE_MAP, combo_base.exchange),
            code=combo_base.code,
            symbol=combo_base.symbol,
            name=combo_base.name,
            currency=self._get_enum(self._CURRENCY_MAP, combo_base.currency),
            category=self._safe_str(combo_base.category),
            delivery_month=self._safe_str(combo_base.delivery_month),
            delivery_date=self._safe_str(combo_base.delivery_date),
            strike_price=float(combo_base.strike_price),
            option_right=self._get_enum(
                self._OPTION_RIGHT_MAP, combo_base.option_right
            ),
            underlying_kind=self._safe_str(combo_base.underlying_kind),
            underlying_code=self._safe_str(combo_base.underlying_code),
            unit=float(combo_base.unit),
            multiplier=int(combo_base.multiplier) if combo_base.multiplier else 0,
            limit_up=combo_base.limit_up,
            limit_down=combo_base.limit_down,
            reference=combo_base.reference,
            update_date=self._safe_str(combo_base.update_date),
            margin_trading_balance=combo_base.margin_trading_balance,
            short_selling_balance=combo_base.short_selling_balance,
            day_trade=self._get_enum(self._DAY_TRADE_MAP, combo_base.day_trade),
            target_code=self._safe_str(combo_base.target_code),
            action=self._get_enum(self._ACTION_MAP, combo_base.action),
        )

    def _to_pb_combo_contract(self, contract: ComboContract):
        """Convert Shioaji ComboContract to Protobuf ComboContract."""
        return provider_pb2.ComboContract(
            legs=[self._to_pb_combo_base(leg) for leg in contract.legs]
        )

    def _to_pb_order(self, order: Order):
        """Convert Shioaji Order to Protobuf Order."""
        return provider_pb2.Order(
            action=self._get_enum(self._ACTION_MAP, order.action),
            price=order.price,
            quantity=order.quantity,
            id=order.id,
            seqno=order.seqno,
            ordno=order.ordno,
            account=self._to_pb_account(order.account) if order.account else None,
            price_type=str(order.price_type),
            order_type=self._get_enum(self._ORDER_TYPE_MAP, order.order_type),
        )

    def _to_pb_combo_order(self, order: ComboOrder):
        """Convert Shioaji ComboOrder to Protobuf ComboOrder."""
        return provider_pb2.ComboOrder(
            action=self._get_enum(self._ACTION_MAP, order.action),
            price=order.price,
            quantity=order.quantity,
            id=order.id,
            seqno=order.seqno,
            ordno=order.ordno,
            account=self._to_pb_account(order.account) if order.account else None,
            price_type=str(order.price_type),
            order_type=self._get_enum(self._ORDER_TYPE_MAP, order.order_type),
        )

    def _to_pb_deal(self, deal):
        """Convert Shioaji Deal to Protobuf Deal."""
        return provider_pb2.Deal(
            seq=deal.seq,
            price=deal.price,
            quantity=deal.quantity,
            ts=deal.ts,
        )

    def _to_pb_order_status(self, status: OrderStatus):
        """Convert Shioaji OrderStatus to Protobuf OrderStatus."""
        return provider_pb2.OrderStatus(
            id=status.id,
            status=self._get_enum(self._STATUS_MAP, status.status),
            status_code=status.status_code,
            order_datetime=str(status.order_datetime),
            deal_quantity=status.deal_quantity,
            cancel_quantity=status.cancel_quantity,
            web_id=status.web_id,
            msg=status.msg,
            modified_time=str(status.modified_time),
            modified_price=float(status.modified_price),
            order_quantity=status.order_quantity,
            deals=[self._to_pb_deal(d) for d in status.deals],
        )

    def _to_pb_trade(self, trade: Trade):
        """Convert Shioaji Trade to Protobuf Trade."""
        return provider_pb2.Trade(
            contract=self._to_pb_contract(trade.contract),
            order=self._to_pb_order(cast(Order, trade.order)),
            status=self._to_pb_order_status(trade.status),
        )

    def _to_pb_combo_trade(self, trade: ComboTrade):
        """Convert Shioaji ComboTrade to Protobuf ComboTrade."""
        return provider_pb2.ComboTrade(
            contract=self._to_pb_combo_contract(trade.contract),
            order=self._to_pb_combo_order(cast(ComboOrder, trade.order)),
            status=self._to_pb_order_status(trade.status),
        )

    def _to_pb_order_deal_record(self, record: OrderDealRecords):
        """Convert Shioaji OrderDealRecord to Protobuf OrderDealRecord."""
        # record.record is a dict containing the details
        data = record.record
        return provider_pb2.OrderDealRecord(
            code=data.get("code", ""),
            action=self._get_enum(self._ACTION_MAP, data.get("action")),
            price=float(data.get("price", 0.0)),
            quantity=int(data.get("quantity", 0)),
            ts=str(data.get("ts", "")),
        )

    def _to_sj_contract(self, proto_contract: provider_pb2.Contract):
        """Convert Protobuf Contract to Shioaji Contract."""
        if proto_contract.security_type == provider_pb2.SECURITY_TYPE_STK:
            return self.client.api.Contracts.Stocks[proto_contract.code]
        if proto_contract.security_type == provider_pb2.SECURITY_TYPE_FUT:
            return self.client.api.Contracts.Futures[proto_contract.code]
        if proto_contract.security_type == provider_pb2.SECURITY_TYPE_OPT:
            return self.client.api.Contracts.Options[proto_contract.code]
        if proto_contract.security_type == provider_pb2.SECURITY_TYPE_IND:
            return self.client.api.Contracts.Indexs[proto_contract.code]
        return self.client.api.Contracts.Stocks[proto_contract.code]

    def _to_sj_order(self, proto_order: provider_pb2.Order):
        """Convert Protobuf Order to Shioaji Order."""
        action_map = {
            provider_pb2.ACTION_BUY: sj_constant.Action.Buy,
            provider_pb2.ACTION_SELL: sj_constant.Action.Sell,
        }
        order_type_map = {
            provider_pb2.ORDER_TYPE_ROD: sj_constant.OrderType.ROD,
            provider_pb2.ORDER_TYPE_IOC: sj_constant.OrderType.IOC,
            provider_pb2.ORDER_TYPE_FOK: sj_constant.OrderType.FOK,
        }

        return self.client.api.Order(
            price=proto_order.price,
            quantity=proto_order.quantity,
            action=action_map.get(proto_order.action, sj_constant.Action.Buy),
            price_type=cast(
                Any, proto_order.price_type
            ),  # cast to Any for str compatibility
            order_type=order_type_map.get(
                proto_order.order_type, sj_constant.OrderType.ROD
            ),
        )

    def _to_sj_combo_contract(self, proto_contract: provider_pb2.ComboContract):
        """Convert Protobuf ComboContract to Shioaji ComboContract."""
        legs = []
        action_map = {
            provider_pb2.ACTION_BUY: sj_constant.Action.Buy,
            provider_pb2.ACTION_SELL: sj_constant.Action.Sell,
        }

        for leg in proto_contract.legs:
            # Create a temporary proto contract to reuse _to_sj_contract logic
            temp_proto = provider_pb2.Contract(
                security_type=leg.security_type, exchange=leg.exchange, code=leg.code
            )
            base_contract = self._to_sj_contract(temp_proto)

            # ComboBase requires action and contract fields
            # We use dict() to unpack contract fields
            legs.append(
                ComboBase(
                    action=action_map.get(leg.action, sj_constant.Action.Buy),
                    **base_contract.dict(),
                )
            )

        return ComboContract(legs=legs)

    def _to_sj_combo_order(self, proto_order: provider_pb2.ComboOrder):
        """Convert Protobuf ComboOrder to Shioaji ComboOrder."""
        action_map = {
            provider_pb2.ACTION_BUY: sj_constant.Action.Buy,
            provider_pb2.ACTION_SELL: sj_constant.Action.Sell,
        }
        order_type_map = {
            provider_pb2.ORDER_TYPE_ROD: sj_constant.OrderType.ROD,
            provider_pb2.ORDER_TYPE_IOC: sj_constant.OrderType.IOC,
            provider_pb2.ORDER_TYPE_FOK: sj_constant.OrderType.FOK,
        }
        octype_map = {
            provider_pb2.FUTURES_OCTYPE_AUTO: sj_constant.FuturesOCType.Auto,
            provider_pb2.FUTURES_OCTYPE_NEW: sj_constant.FuturesOCType.New,
            provider_pb2.FUTURES_OCTYPE_COVER: sj_constant.FuturesOCType.Cover,
            provider_pb2.FUTURES_OCTYPE_DAYTRADE: sj_constant.FuturesOCType.DayTrade,
        }

        return ComboOrder(
            price=proto_order.price,
            quantity=proto_order.quantity,
            action=action_map.get(proto_order.action, sj_constant.Action.Buy),
            price_type=cast(Any, proto_order.price_type),
            order_type=order_type_map.get(
                proto_order.order_type, sj_constant.OrderType.ROD
            ),
            octype=octype_map.get(proto_order.octype, sj_constant.FuturesOCType.Auto),
        )

    def _find_trade(self, proto_trade: provider_pb2.Trade) -> Optional[Trade]:
        """Find a Shioaji Trade object based on Protobuf Trade info."""
        trades = self.client.list_trades()
        target_seqno = proto_trade.order.seqno
        target_id = proto_trade.order.id

        for trade in trades:
            if target_seqno and trade.order.seqno == target_seqno:
                return trade
            if target_id and trade.order.id == target_id:
                return trade
        return None

    def _find_combo_trade(
        self, proto_trade: provider_pb2.ComboTrade
    ) -> Optional[ComboTrade]:
        """Find a Shioaji ComboTrade object based on Protobuf ComboTrade info."""
        trades = self.client.list_combotrades()
        target_seqno = proto_trade.order.seqno
        target_id = proto_trade.order.id

        for trade in trades:
            if target_seqno and trade.order.seqno == target_seqno:
                return trade
            if target_id and trade.order.id == target_id:
                return trade
        return None

    def PlaceOrder(
        self, request: provider_pb2.PlaceOrderRequest, context: grpc.ServicerContext
    ) -> provider_pb2.Trade:
        """Place a new order."""
        try:
            contract = self._to_sj_contract(request.contract)
            order = self._to_sj_order(request.order)
            trade = self.client.place_order(contract, order)
            return self._to_pb_trade(trade)
        except KeyError as e:
            logging.error("KeyError in PlaceOrder: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.NOT_FOUND, f"Contract not found: {e}")
            return provider_pb2.Trade()
        except Exception as e:
            logging.error("Error in PlaceOrder: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.Trade()

    def PlaceComboOrder(
        self,
        request: provider_pb2.PlaceComboOrderRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.ComboTrade:
        """Place a combination order."""
        try:
            combo_contract = self._to_sj_combo_contract(request.combo_contract)
            order = self._to_sj_combo_order(request.order)
            trade = self.client.place_comboorder(combo_contract, order)
            return self._to_pb_combo_trade(trade)
        except KeyError as e:
            logging.error("KeyError in PlaceComboOrder: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.NOT_FOUND, f"Contract not found: {e}")
            return provider_pb2.ComboTrade()
        except Exception as e:
            logging.error("Error in PlaceComboOrder: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ComboTrade()

    def UpdateOrder(
        self, request: provider_pb2.UpdateOrderRequest, context: grpc.ServicerContext
    ) -> provider_pb2.Trade:
        """Update an existing order."""
        try:
            trade = self._find_trade(request.trade)
            if not trade:
                context.abort(grpc.StatusCode.NOT_FOUND, "Trade not found")
                return provider_pb2.Trade()

            # The client.update_order expects the trade object, price (float), and qty (int)
            res = self.client.update_order(
                trade, price=request.price, qty=request.quantity
            )
            return self._to_pb_trade(res)
        except Exception as e:
            logging.error("Error in UpdateOrder: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.Trade()

    def CancelOrder(
        self, request: provider_pb2.CancelOrderRequest, context: grpc.ServicerContext
    ) -> provider_pb2.Trade:
        """Cancel an existing order."""
        try:
            trade = self._find_trade(request.trade)
            if not trade:
                context.abort(grpc.StatusCode.NOT_FOUND, "Trade not found")
                return provider_pb2.Trade()

            res = self.client.cancel_order(trade)
            return self._to_pb_trade(res)
        except Exception as e:
            logging.error("Error in CancelOrder: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.Trade()

    def CancelComboOrder(
        self,
        request: provider_pb2.CancelComboOrderRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.ComboTrade:
        """Cancel a combination order."""
        try:
            trade = self._find_combo_trade(request.combotrade)
            if not trade:
                context.abort(grpc.StatusCode.NOT_FOUND, "ComboTrade not found")
                return provider_pb2.ComboTrade()

            res = self.client.cancel_comboorder(trade)
            return self._to_pb_combo_trade(res)
        except Exception as e:
            logging.error("Error in CancelComboOrder: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ComboTrade()

    def UpdateStatus(
        self, request: provider_pb2.UpdateStatusRequest, context: grpc.ServicerContext
    ) -> provider_pb2.Empty:
        """Update the status of orders and trades for an account."""
        try:
            self.client.update_status(self._stock_account)
            return provider_pb2.Empty()
        except Exception as e:
            logging.error("Error in UpdateStatus: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.Empty()

    def UpdateComboStatus(
        self, request: provider_pb2.UpdateStatusRequest, context: grpc.ServicerContext
    ) -> provider_pb2.Empty:
        """Update the status of combination orders for an account."""
        try:
            self.client.update_combostatus(self._stock_account)
            return provider_pb2.Empty()
        except Exception as e:
            logging.error("Error in UpdateComboStatus: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.Empty()

    def ListTrades(
        self, request: provider_pb2.Empty, context: grpc.ServicerContext
    ) -> provider_pb2.ListTradesResponse:
        """List all trades."""
        try:
            trades = self.client.list_trades()
            return provider_pb2.ListTradesResponse(
                trades=[self._to_pb_trade(t) for t in trades]
            )
        except Exception as e:
            logging.error("Error in ListTrades: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ListTradesResponse()

    def ListComboTrades(
        self, request: provider_pb2.Empty, context: grpc.ServicerContext
    ) -> provider_pb2.ListComboTradesResponse:
        """List all combination trades."""
        try:
            trades = self.client.list_combotrades()
            return provider_pb2.ListComboTradesResponse(
                combo_trades=[self._to_pb_combo_trade(t) for t in trades]
            )
        except Exception as e:
            logging.error("Error in ListComboTrades: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ListComboTradesResponse()

    def GetOrderDealRecords(
        self,
        request: provider_pb2.GetOrderDealRecordsRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.GetOrderDealRecordsResponse:
        """Get order deal records."""
        try:
            records = self.client.order_deal_records(self._stock_account)
            return provider_pb2.GetOrderDealRecordsResponse(
                records=[self._to_pb_order_deal_record(r) for r in records]
            )
        except Exception as e:
            logging.error("Error in GetOrderDealRecords: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.GetOrderDealRecordsResponse()

    def ListPositions(
        self, request: provider_pb2.ListPositionsRequest, context: grpc.ServicerContext
    ) -> provider_pb2.ListPositionsResponse:
        """List current positions for an account."""
        try:
            positions = self.client.list_positions(self._stock_account)
            pb_positions = []
            for p in positions:
                if isinstance(p, StockPosition):
                    pb_positions.append(
                        provider_pb2.Position(
                            stock_position=provider_pb2.StockPosition(
                                id=p.id,
                                code=p.code,
                                direction=self._get_enum(self._ACTION_MAP, p.direction),
                                quantity=p.quantity,
                                price=p.price,
                                last_price=p.last_price,
                                pnl=p.pnl,
                                yd_quantity=p.yd_quantity,
                                cond=self._get_enum(
                                    self._STOCK_ORDER_COND_MAP,
                                    p.cond,
                                ),
                                margin_purchase_amount=p.margin_purchase_amount,
                                collateral=p.collateral,
                                short_sale_margin=p.short_sale_margin,
                                interest=p.interest,
                            )
                        )
                    )
                elif isinstance(p, FuturePosition):
                    pb_positions.append(
                        provider_pb2.Position(
                            future_position=provider_pb2.FuturePosition(
                                id=p.id,
                                code=p.code,
                                direction=self._get_enum(self._ACTION_MAP, p.direction),
                                quantity=p.quantity,
                                price=p.price,
                                last_price=p.last_price,
                                pnl=p.pnl,
                            )
                        )
                    )
            return provider_pb2.ListPositionsResponse(positions=pb_positions)
        except Exception as e:
            logging.error("Error in ListPositions: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ListPositionsResponse()

    def ListPositionDetail(
        self,
        request: provider_pb2.ListPositionDetailRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.ListPositionDetailResponse:
        """Get detailed information for a specific position."""
        try:
            details = self.client.list_position_detail(
                self._stock_account, request.detail_id
            )
            pb_details = []
            for d in details:
                if isinstance(d, StockPositionDetail):
                    pb_details.append(
                        provider_pb2.PositionDetail(
                            stock_detail=provider_pb2.StockPositionDetail(
                                date=d.date,
                                code=d.code,
                                quantity=d.quantity,
                                price=d.price,
                                last_price=d.last_price,
                                pnl=d.pnl,
                                dseq=d.dseq,
                                direction=self._get_enum(self._ACTION_MAP, d.direction),
                                currency=self._get_enum(self._CURRENCY_MAP, d.currency),
                                fee=float(d.fee),
                                cond=self._get_enum(
                                    self._STOCK_ORDER_COND_MAP,
                                    d.cond,
                                ),
                                ex_dividends=d.ex_dividends,
                                interest=d.interest,
                                margintrading_amt=d.margintrading_amt,
                                collateral=d.collateral,
                            )
                        )
                    )
                elif isinstance(d, FuturePositionDetail):
                    pb_details.append(
                        provider_pb2.PositionDetail(
                            future_detail=provider_pb2.FuturePositionDetail(
                                date=d.date,
                                code=d.code,
                                quantity=d.quantity,
                                price=d.price,
                                last_price=d.last_price,
                                pnl=d.pnl,
                                dseq=d.dseq,
                                direction=self._get_enum(self._ACTION_MAP, d.direction),
                                currency=self._get_enum(self._CURRENCY_MAP, d.currency),
                                fee=float(d.fee),
                                entry_quantity=d.entry_quantity,
                            )
                        )
                    )
            return provider_pb2.ListPositionDetailResponse(details=pb_details)
        except Exception as e:
            logging.error("Error in ListPositionDetail: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ListPositionDetailResponse()

    def ListProfitLoss(
        self, request: provider_pb2.ListProfitLossRequest, context: grpc.ServicerContext
    ) -> provider_pb2.ListProfitLossResponse:
        """List realized profit and loss."""
        try:
            pnls = self.client.list_profit_loss(self._stock_account)
            pb_pnls = []
            for p in pnls:
                if isinstance(p, StockProfitLoss):
                    pb_pnls.append(
                        provider_pb2.ProfitLoss(
                            stock_pnl=provider_pb2.StockProfitLoss(
                                dseq=p.dseq,
                                code=p.code,
                                quantity=p.quantity,
                                price=p.price,
                                pnl=p.pnl,
                                pr_ratio=p.pr_ratio,
                                cond=self._get_enum(
                                    self._STOCK_ORDER_COND_MAP,
                                    p.cond,
                                ),
                                date=p.date,
                                seqno=p.seqno,
                                id=p.id,
                            )
                        )
                    )
                elif isinstance(p, FutureProfitLoss):
                    pb_pnls.append(
                        provider_pb2.ProfitLoss(
                            future_pnl=provider_pb2.FutureProfitLoss(
                                date=p.date,
                                code=p.code,
                                quantity=p.quantity,
                                entry_price=p.entry_price,
                                cover_price=p.cover_price,
                                direction=self._get_enum(self._ACTION_MAP, p.direction),
                                pnl=p.pnl,
                                tax=p.tax,
                                fee=p.fee,
                                id=p.id,
                            )
                        )
                    )
            return provider_pb2.ListProfitLossResponse(profit_losses=pb_pnls)
        except Exception as e:
            logging.error("Error in ListProfitLoss: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ListProfitLossResponse()

    def ListProfitLossDetail(
        self,
        request: provider_pb2.ListProfitLossDetailRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.ListProfitLossDetailResponse:
        """Get detailed realized profit and loss for a specific entry."""
        try:
            details = self.client.list_profit_loss_detail(
                self._stock_account, request.detail_id
            )
            pb_details = []
            for d in details:
                if isinstance(d, StockProfitDetail):
                    pb_details.append(
                        provider_pb2.ProfitDetail(
                            stock_detail=provider_pb2.StockProfitDetail(
                                price=d.price,
                                cost=d.cost,
                                interest=d.interest,
                                date=d.date,
                                code=d.code,
                                quantity=d.quantity,
                                dseq=d.dseq,
                                fee=d.fee,
                                tax=d.tax,
                                currency=self._get_enum(self._CURRENCY_MAP, d.currency),
                                rep_margintrading_amt=d.rep_margintrading_amt,
                                rep_collateral=d.rep_collateral,
                                rep_margin=d.rep_margin,
                                shortselling_fee=d.shortselling_fee,
                                ex_dividend_amt=d.ex_dividend_amt,
                                trade_type=self._get_enum(
                                    self._TRADE_TYPE_MAP, d.trade_type
                                ),
                                cond=self._get_enum(
                                    self._STOCK_ORDER_COND_MAP,
                                    d.cond,
                                ),
                            )
                        )
                    )
                elif isinstance(d, FutureProfitDetail):
                    pb_details.append(
                        provider_pb2.ProfitDetail(
                            future_detail=provider_pb2.FutureProfitDetail(
                                direction=self._get_enum(self._ACTION_MAP, d.direction),
                                entry_date=d.entry_date,
                                entry_price=d.entry_price,
                                cover_price=d.cover_price,
                                pnl=d.pnl,
                                date=d.date,
                                code=d.code,
                                quantity=d.quantity,
                                dseq=d.dseq,
                                fee=d.fee,
                                tax=d.tax,
                                currency=self._get_enum(self._CURRENCY_MAP, d.currency),
                            )
                        )
                    )
            return provider_pb2.ListProfitLossDetailResponse(details=pb_details)
        except Exception as e:
            logging.error("Error in ListProfitLossDetail: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ListProfitLossDetailResponse()

    def ListProfitLossSummary(
        self,
        request: provider_pb2.ListProfitLossSummaryRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.ListProfitLossSummaryResponse:
        """Get a summary of profit and loss."""
        try:
            summaries = self.client.list_profit_loss_summary(self._stock_account)
            pb_summaries = []
            for s in summaries:
                if isinstance(s, StockProfitLossSummary):
                    pb_summaries.append(
                        provider_pb2.ProfitLossSummary(
                            stock_summary=provider_pb2.StockProfitLossSummary(
                                entry_cost=s.entry_cost,
                                cover_cost=s.cover_cost,
                                code=s.code,
                                quantity=s.quantity,
                                entry_price=s.entry_price,
                                cover_price=s.cover_price,
                                pnl=s.pnl,
                                currency=self._get_enum(self._CURRENCY_MAP, s.currency),
                                buy_cost=s.buy_cost,
                                sell_cost=s.sell_cost,
                                pr_ratio=s.pr_ratio,
                                cond=self._get_enum(
                                    self._STOCK_ORDER_COND_MAP,
                                    s.cond,
                                ),
                            )
                        )
                    )
                elif isinstance(s, FutureProfitLossSummary):
                    pb_summaries.append(
                        provider_pb2.ProfitLossSummary(
                            future_summary=provider_pb2.FutureProfitLossSummary(
                                direction=self._get_enum(self._ACTION_MAP, s.direction),
                                tax=s.tax,
                                fee=s.fee,
                                code=s.code,
                                quantity=s.quantity,
                                entry_price=s.entry_price,
                                cover_price=s.cover_price,
                                pnl=s.pnl,
                                currency=self._get_enum(self._CURRENCY_MAP, s.currency),
                            )
                        )
                    )
            return provider_pb2.ListProfitLossSummaryResponse(summaries=pb_summaries)
        except Exception as e:
            logging.error("Error in ListProfitLossSummary: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ListProfitLossSummaryResponse()

    def GetSettlements(
        self, request: provider_pb2.GetSettlementsRequest, context: grpc.ServicerContext
    ) -> provider_pb2.GetSettlementsResponse:
        """Get settlement information."""
        try:
            settlements = self.client.settlements(self._stock_account)
            return provider_pb2.GetSettlementsResponse(
                settlements=[
                    provider_pb2.Settlement(
                        date=str(getattr(s, "date", "")),
                        amount=getattr(s, "amount", 0.0),
                        t_money=getattr(s, "t_money", 0.0),
                        t_day=str(getattr(s, "t_day", "")),
                        t1_money=getattr(s, "t1_money", 0.0),
                        t1_day=str(getattr(s, "t1_day", "")),
                        t2_money=getattr(s, "t2_money", 0.0),
                        t2_day=str(getattr(s, "t2_day", "")),
                    )
                    for s in settlements
                ]
            )
        except Exception as e:
            logging.error("Error in GetSettlements: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.GetSettlementsResponse()

    def ListSettlements(
        self, request: provider_pb2.GetSettlementsRequest, context: grpc.ServicerContext
    ) -> provider_pb2.GetSettlementsResponse:
        """List settlement information (Alias)."""
        return self.GetSettlements(request, context)

    def GetMargin(
        self, request: provider_pb2.GetMarginRequest, context: grpc.ServicerContext
    ) -> provider_pb2.Margin:
        try:
            margin = self.client.margin(self._futopt_account)
            return provider_pb2.Margin(
                equity=margin.equity,
                available_margin=margin.available_margin,
                initial_margin=margin.initial_margin,
                maintenance_margin=margin.maintenance_margin,
                yesterday_balance=margin.yesterday_balance,
                today_balance=margin.today_balance,
                deposit_withdrawal=margin.deposit_withdrawal,
                fee=margin.fee,
                tax=margin.tax,
                margin_call=margin.margin_call,
                risk_indicator=margin.risk_indicator,
                royalty_revenue_expenditure=margin.royalty_revenue_expenditure,
                equity_amount=margin.equity_amount,
                option_openbuy_market_value=margin.option_openbuy_market_value,
                option_opensell_market_value=margin.option_opensell_market_value,
                option_open_position=margin.option_open_position,
                option_settle_profitloss=margin.option_settle_profitloss,
                future_open_position=margin.future_open_position,
                today_future_open_position=margin.today_future_open_position,
                future_settle_profitloss=margin.future_settle_profitloss,
            )
        except Exception as e:
            logging.error("Error in GetMargin: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.Margin()

    def GetTradingLimits(
        self,
        request: provider_pb2.GetTradingLimitsRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.TradingLimits:
        """Get trading limits for a stock account."""
        try:
            limits = self.client.trading_limits(self._stock_account)
            return provider_pb2.TradingLimits(
                trading_limit=limits.trading_limit,
                trading_used=limits.trading_used,
                trading_available=limits.trading_available,
                margin_limit=limits.margin_limit,
                margin_used=limits.margin_used,
                margin_available=limits.margin_available,
                short_limit=limits.short_limit,
                short_used=limits.short_used,
                short_available=limits.short_available,
            )
        except Exception as e:
            logging.error("Error in GetTradingLimits: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.TradingLimits()

    def GetStockReserveSummary(
        self,
        request: provider_pb2.GetStockReserveSummaryRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.ReserveStocksSummaryResponse:
        """Get stock reserve summary."""
        try:
            summary = self.client.stock_reserve_summary(self._stock_account)
            return provider_pb2.ReserveStocksSummaryResponse(response_json=str(summary))
        except Exception as e:
            logging.error("Error in GetStockReserveSummary: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ReserveStocksSummaryResponse()

    def GetStockReserveDetail(
        self,
        request: provider_pb2.GetStockReserveDetailRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.ReserveStocksDetailResponse:
        """Get stock reserve details."""
        try:
            detail = self.client.stock_reserve_detail(self._stock_account)
            return provider_pb2.ReserveStocksDetailResponse(response_json=str(detail))
        except Exception as e:
            logging.error("Error in GetStockReserveDetail: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ReserveStocksDetailResponse()

    def ReserveStock(
        self, request: provider_pb2.ReserveStockRequest, context: grpc.ServicerContext
    ) -> provider_pb2.ReserveStockResponse:
        """Reserve stock for borrowing."""
        try:
            # Needs contract conversion
            contract = self._to_sj_contract(request.contract)
            resp = self.client.reserve_stock(
                self._stock_account, contract, request.share
            )
            return provider_pb2.ReserveStockResponse(response_json=str(resp))
        except KeyError as e:
            logging.error("KeyError in ReserveStock: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.NOT_FOUND, f"Contract not found: {e}")
            return provider_pb2.ReserveStockResponse()
        except Exception as e:
            logging.error("Error in ReserveStock: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ReserveStockResponse()

    def GetEarmarkingDetail(
        self,
        request: provider_pb2.GetEarmarkingDetailRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.EarmarkStocksDetailResponse:
        """Get earmarking details."""
        try:
            detail = self.client.earmarking_detail(self._stock_account)
            return provider_pb2.EarmarkStocksDetailResponse(response_json=str(detail))
        except Exception as e:
            logging.error("Error in GetEarmarkingDetail: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.EarmarkStocksDetailResponse()

    def ReserveEarmarking(
        self,
        request: provider_pb2.ReserveEarmarkingRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.ReserveEarmarkingResponse:
        """Apply for earmarking."""
        try:
            contract = self._to_sj_contract(request.contract)
            resp = self.client.reserve_earmarking(
                self._stock_account, contract, request.share, request.price
            )
            return provider_pb2.ReserveEarmarkingResponse(response_json=str(resp))
        except KeyError as e:
            logging.error("KeyError in ReserveEarmarking: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.NOT_FOUND, f"Contract not found: {e}")
            return provider_pb2.ReserveEarmarkingResponse()
        except Exception as e:
            logging.error("Error in ReserveEarmarking: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.ReserveEarmarkingResponse()

    def GetSnapshots(
        self, request: provider_pb2.GetSnapshotsRequest, context: grpc.ServicerContext
    ) -> provider_pb2.GetSnapshotsResponse:
        """Get market snapshots for a list of contracts."""
        try:
            contracts = [self._lookup_contract(code) for code in request.contract_codes]
            snapshots = self.client.snapshots(contracts)
            return provider_pb2.GetSnapshotsResponse(
                snapshots=[
                    provider_pb2.Snapshot(
                        ts=s.ts,
                        code=s.code,
                        exchange=self._get_enum(self._EXCHANGE_MAP, s.exchange),
                        open=s.open,
                        high=s.high,
                        low=s.low,
                        close=s.close,
                        change_price=s.change_price,
                        change_rate=s.change_rate,
                        average_price=s.average_price,
                        volume=s.volume,
                        total_volume=s.total_volume,
                        amount=s.amount,
                        total_amount=s.total_amount,
                        buy_price=s.buy_price,
                        buy_volume=float(s.buy_volume),
                        sell_price=s.sell_price,
                        sell_volume=s.sell_volume,
                        tick_type=self._get_enum(self._TICK_TYPE_MAP, s.tick_type),
                        change_type=self._get_enum(
                            self._CHANGE_TYPE_MAP, s.change_type
                        ),
                        yesterday_volume=s.yesterday_volume,
                        volume_ratio=s.volume_ratio,
                    )
                    for s in snapshots
                ]
            )
        except KeyError as e:
            logging.error("KeyError in GetSnapshots: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.NOT_FOUND, f"Contract not found: {e}")
            return provider_pb2.GetSnapshotsResponse()
        except Exception as e:
            logging.error("Error in GetSnapshots: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.GetSnapshotsResponse()

    def GetTicks(
        self, request: provider_pb2.GetTicksRequest, context: grpc.ServicerContext
    ) -> provider_pb2.Ticks:
        """Get tick data for a specific contract and date."""
        try:
            contract = self._lookup_contract(request.contract_code)
            ticks = self.client.ticks(contract, request.date)
            return provider_pb2.Ticks(
                ts=ticks.ts,
                close=ticks.close,
                volume=ticks.volume,
                bid_price=ticks.bid_price,
                bid_volume=ticks.bid_volume,
                ask_price=ticks.ask_price,
                ask_volume=ticks.ask_volume,
                tick_type=ticks.tick_type,
            )
        except KeyError as e:
            logging.error("KeyError in GetTicks: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.NOT_FOUND, f"Contract not found: {e}")
            return provider_pb2.Ticks()
        except Exception as e:
            logging.error("Error in GetTicks: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.Ticks()

    def GetKbars(
        self, request: provider_pb2.GetKbarsRequest, context: grpc.ServicerContext
    ) -> provider_pb2.Kbars:
        """Get K-bar (candlestick) data for a specific contract and date range."""
        try:
            contract = self._lookup_contract(request.contract_code)
            kbars = self.client.kbars(contract, request.start_date, request.end_date)
            return provider_pb2.Kbars(
                ts=kbars.ts,
                open=kbars.Open,
                high=kbars.High,
                low=kbars.Low,
                close=kbars.Close,
                volume=kbars.Volume,
                amount=kbars.Amount,
            )
        except KeyError as e:
            logging.error("KeyError in GetKbars: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.NOT_FOUND, f"Contract not found: {e}")
            return provider_pb2.Kbars()
        except Exception as e:
            logging.error("Error in GetKbars: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.Kbars()

    def GetDailyQuotes(
        self, request: provider_pb2.GetDailyQuotesRequest, context: grpc.ServicerContext
    ) -> provider_pb2.DailyQuotes:
        """Get daily quotes."""
        try:
            # request.date is string YYYY-MM-DD
            try:
                date_obj = datetime.strptime(request.date, "%Y-%m-%d").date()
            except ValueError:
                context.abort(
                    grpc.StatusCode.INVALID_ARGUMENT,
                    f"Invalid date format: {request.date}. Expected YYYY-MM-DD",
                )
                return provider_pb2.DailyQuotes()

            quotes = self.client.daily_quotes(date_obj)
            return provider_pb2.DailyQuotes(
                code=quotes.Code,
                open=quotes.Open,
                high=quotes.High,
                low=quotes.Low,
                close=quotes.Close,
                volume=quotes.Volume,
                date=[str(d) for d in quotes.Date],
                transaction=quotes.Transaction,
                amount=quotes.Amount,
            )
        except Exception as e:
            logging.error("Error in GetDailyQuotes: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.DailyQuotes()

    def CreditEnquires(
        self, request: provider_pb2.CreditEnquiresRequest, context: grpc.ServicerContext
    ) -> provider_pb2.CreditEnquiresResponse:
        """Enquire about credit for a list of contracts."""
        try:
            contracts = [
                self.client.api.Contracts.Stocks[code]
                for code in request.contract_codes
            ]
            res = self.client.credit_enquires(contracts)
            return provider_pb2.CreditEnquiresResponse(
                credit_enquires=[
                    provider_pb2.CreditEnquire(
                        stock_id=r.stock_id,
                        margin_unit=r.margin_unit,
                        short_unit=r.short_unit,
                        update_time=r.update_time,
                        system=r.system,
                    )
                    for r in res
                ]
            )
        except KeyError as e:
            logging.error("KeyError in CreditEnquires: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.NOT_FOUND, f"Contract not found: {e}")
            return provider_pb2.CreditEnquiresResponse()
        except Exception as e:
            logging.error("Error in CreditEnquires: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.CreditEnquiresResponse()

    def GetShortStockSources(
        self,
        request: provider_pb2.GetShortStockSourcesRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.GetShortStockSourcesResponse:
        """Get short stock sources for a list of contracts."""
        try:
            contracts = [
                self.client.api.Contracts.Stocks[code]
                for code in request.contract_codes
            ]
            res = self.client.short_stock_sources(contracts)
            return provider_pb2.GetShortStockSourcesResponse(
                sources=[
                    provider_pb2.ShortStockSource(
                        code=s.code, short_stock_source=s.short_stock_source, ts=s.ts
                    )
                    for s in res
                ]
            )
        except KeyError as e:
            logging.error("KeyError in GetShortStockSources: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.NOT_FOUND, f"Contract not found: {e}")
            return provider_pb2.GetShortStockSourcesResponse()
        except Exception as e:
            logging.error("Error in GetShortStockSources: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.GetShortStockSourcesResponse()

    def GetScanners(
        self, request: provider_pb2.GetScannersRequest, context: grpc.ServicerContext
    ) -> provider_pb2.GetScannersResponse:
        """Get scanner results (ranked stocks)."""
        try:
            # Reverse map Proto Enum to Shioaji Constant Enum (String)
            # request.scanner_type is int
            # scanner_type_name = provider_pb2.ScannerType.Name(request.scanner_type)
            # Name is SCANNER_TYPE_AMOUNTRANK
            # We want "AmountRank"

            pb_to_sj_scanner = {
                provider_pb2.SCANNER_TYPE_CHANGEPERCENTRANK: sj_constant.ScannerType.ChangePercentRank,
                provider_pb2.SCANNER_TYPE_CHANGEPRICERANK: sj_constant.ScannerType.ChangePriceRank,
                provider_pb2.SCANNER_TYPE_DAYRANGERANK: sj_constant.ScannerType.DayRangeRank,
                provider_pb2.SCANNER_TYPE_VOLUMERANK: sj_constant.ScannerType.VolumeRank,
                provider_pb2.SCANNER_TYPE_AMOUNTRANK: sj_constant.ScannerType.AmountRank,
                provider_pb2.SCANNER_TYPE_TICKCOUNTRANK: sj_constant.ScannerType.TickCountRank,
            }

            stype = pb_to_sj_scanner.get(
                request.scanner_type, sj_constant.ScannerType.AmountRank
            )

            res = self.client.scanners(
                scanner_type=stype,
                ascending=request.ascending,
                date_str=request.date,
                count=request.count,
            )
            return provider_pb2.GetScannersResponse(
                scanners=[
                    provider_pb2.ScannerItem(
                        code=s.code,
                        name=s.name,
                        close=s.close,
                        date=s.date,
                        ts=s.ts,
                        open=s.open,
                        high=s.high,
                        low=s.low,
                        price_range=s.price_range,
                        tick_type=self._get_enum(self._TICK_TYPE_MAP, s.tick_type),
                        change_price=s.change_price,
                        change_type=self._get_enum(
                            self._CHANGE_TYPE_MAP, s.change_type
                        ),
                        average_price=s.average_price,
                        volume=s.volume,
                        total_volume=s.total_volume,
                        amount=s.amount,
                        total_amount=s.total_amount,
                        yesterday_volume=s.yesterday_volume,
                        volume_ratio=s.volume_ratio,
                        buy_price=s.buy_price,
                        buy_volume=s.buy_volume,
                        sell_price=s.sell_price,
                        sell_volume=s.sell_volume,
                        bid_orders=s.bid_orders,
                        bid_volumes=s.bid_volumes,
                        ask_orders=s.ask_orders,
                        ask_volumes=s.ask_volumes,
                        rank_value=s.rank_value,
                    )
                    for s in res
                ]
            )
        except Exception as e:
            logging.error("Error in GetScanners: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.GetScannersResponse()

    def GetPunish(
        self, request: provider_pb2.Empty, context: grpc.ServicerContext
    ) -> provider_pb2.Punish:
        """Get punishment information (disposition stocks)."""
        try:
            res = self.client.punish()
            return provider_pb2.Punish(
                code=res.code,
                start_date=[str(d) for d in res.start_date],
                end_date=[str(d) for d in res.end_date],
                interval=res.interval,
                updated_at=[str(d) for d in res.updated_at],
                unit_limit=[float(x) if x is not None else 0.0 for x in res.unit_limit],
                total_limit=[
                    float(x) if x is not None else 0.0 for x in res.total_limit
                ],
                description=res.description,
                announced_date=[str(d) for d in res.announced_date],
            )
        except Exception as e:
            logging.error("Error in GetPunish: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.Punish()

    def GetNotice(
        self, request: provider_pb2.Empty, context: grpc.ServicerContext
    ) -> provider_pb2.Notice:
        """Get notice information (attention stocks)."""
        try:
            res = self.client.notice()
            return provider_pb2.Notice(
                code=res.code,
                reason=res.reason,
                updated_at=[str(d) for d in res.updated_at],
                close=[float(x) if x is not None else 0.0 for x in res.close],
                announced_date=[str(d) for d in res.announced_date],
            )
        except Exception as e:
            logging.error("Error in GetNotice: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.Notice()

    def FetchContracts(
        self, request: provider_pb2.FetchContractsRequest, context: grpc.ServicerContext
    ) -> provider_pb2.Empty:
        """Manually fetch contracts."""
        try:
            self.client.fetch_contracts(request.contract_download)
            return provider_pb2.Empty()
        except Exception as e:
            logging.error("Error in FetchContracts: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.Empty()

    def GetCAExpireTime(
        self,
        request: provider_pb2.GetCAExpireTimeRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.GetCAExpireTimeResponse:
        """Get the CA expiration time."""
        try:
            expire_time = self.client.get_ca_expiretime(request.person_id)
            return provider_pb2.GetCAExpireTimeResponse(expire_time=str(expire_time))
        except Exception as e:
            logging.error("Error in GetCAExpireTime: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.GetCAExpireTimeResponse()

    def SubscribeTrade(
        self, request: provider_pb2.SubscribeTradeRequest, context: grpc.ServicerContext
    ) -> provider_pb2.SubscribeTradeResponse:
        """Subscribe to trade updates for an account."""
        try:
            success = self.client.subscribe_trade(self._stock_account)
            return provider_pb2.SubscribeTradeResponse(success=success)
        except Exception as e:
            logging.error("Error in SubscribeTrade: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.SubscribeTradeResponse()

    def UnsubscribeTrade(
        self,
        request: provider_pb2.UnsubscribeTradeRequest,
        context: grpc.ServicerContext,
    ) -> provider_pb2.UnsubscribeTradeResponse:
        """Unsubscribe from trade updates for an account."""
        try:
            success = self.client.unsubscribe_trade(self._stock_account)
            return provider_pb2.UnsubscribeTradeResponse(success=success)
        except Exception as e:
            logging.error("Error in UnsubscribeTrade: %s", e, exc_info=True)
            context.abort(grpc.StatusCode.INTERNAL, str(e))
            return provider_pb2.UnsubscribeTradeResponse()


def serve():
    """Start the gRPC server."""
    addr = os.getenv("PROVIDER_ADDR", "localhost:50051")
    if addr.startswith("unix:"):
        # Extract the path from the unix address
        # unix:///tmp/phoenix.sock -> /tmp/phoenix.sock
        # unix:./phoenix.sock -> ./phoenix.sock
        path = addr[5:]
        if path.startswith("//"):
            path = path[2:]

        if os.path.exists(path):
            try:
                os.unlink(path)
                logging.info("Removed existing socket file: %s", path)
            except OSError as e:
                logging.error("Error removing socket file: %s", e)

    server = grpc.server(futures.ThreadPoolExecutor())
    service = ShioajiService()
    provider_pb2_grpc.add_ShioajiProviderServicer_to_server(service, server)
    server.add_insecure_port(addr)
    logging.info("Server started, listening on %s", addr)

    def shutdown_handler(signum, _):
        logging.info("Received signal %s. Starting graceful shutdown...", signum)
        if service.logged_in:
            try:
                logging.info("Logging out from Shioaji...")
                service.client.logout()
                logging.info("Shioaji logout successful.")
            except Exception as e:
                logging.error("Error during Shioaji logout: %s", e)
        server.stop(0)
        logging.info("Server stopped.")

    # Register signals
    for sig in (signal.SIGINT, signal.SIGTERM, signal.SIGQUIT):
        signal.signal(sig, shutdown_handler)

    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    serve()
    os._exit(0)  # pylint: disable=protected-access
