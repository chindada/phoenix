from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("api_key", "secret_key")
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    api_key: str
    secret_key: str
    def __init__(self, api_key: _Optional[str] = ..., secret_key: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("accounts",)
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[Account]
    def __init__(self, accounts: _Optional[_Iterable[_Union[Account, _Mapping]]] = ...) -> None: ...

class LogoutResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class Account(_message.Message):
    __slots__ = ("account_type", "person_id", "broker_id", "account_id", "signed", "username")
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    BROKER_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    SIGNED_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    account_type: str
    person_id: str
    broker_id: str
    account_id: str
    signed: bool
    username: str
    def __init__(self, account_type: _Optional[str] = ..., person_id: _Optional[str] = ..., broker_id: _Optional[str] = ..., account_id: _Optional[str] = ..., signed: bool = ..., username: _Optional[str] = ...) -> None: ...

class UsageStatus(_message.Message):
    __slots__ = ("connections", "bytes", "limit_bytes", "remaining_bytes")
    CONNECTIONS_FIELD_NUMBER: _ClassVar[int]
    BYTES_FIELD_NUMBER: _ClassVar[int]
    LIMIT_BYTES_FIELD_NUMBER: _ClassVar[int]
    REMAINING_BYTES_FIELD_NUMBER: _ClassVar[int]
    connections: int
    bytes: int
    limit_bytes: int
    remaining_bytes: int
    def __init__(self, connections: _Optional[int] = ..., bytes: _Optional[int] = ..., limit_bytes: _Optional[int] = ..., remaining_bytes: _Optional[int] = ...) -> None: ...

class ListAccountsResponse(_message.Message):
    __slots__ = ("accounts",)
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[Account]
    def __init__(self, accounts: _Optional[_Iterable[_Union[Account, _Mapping]]] = ...) -> None: ...

class AccountBalance(_message.Message):
    __slots__ = ("acc_balance", "date", "errmsg", "currency")
    ACC_BALANCE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    acc_balance: float
    date: str
    errmsg: str
    currency: str
    def __init__(self, acc_balance: _Optional[float] = ..., date: _Optional[str] = ..., errmsg: _Optional[str] = ..., currency: _Optional[str] = ...) -> None: ...

class Contract(_message.Message):
    __slots__ = ("security_type", "exchange", "code", "symbol", "name", "currency")
    SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    security_type: str
    exchange: str
    code: str
    symbol: str
    name: str
    currency: str
    def __init__(self, security_type: _Optional[str] = ..., exchange: _Optional[str] = ..., code: _Optional[str] = ..., symbol: _Optional[str] = ..., name: _Optional[str] = ..., currency: _Optional[str] = ...) -> None: ...

class ComboContract(_message.Message):
    __slots__ = ("code",)
    CODE_FIELD_NUMBER: _ClassVar[int]
    code: str
    def __init__(self, code: _Optional[str] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ("action", "price", "quantity", "id", "seqno", "ordno", "account", "price_type", "order_type")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    ORDNO_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    action: str
    price: float
    quantity: int
    id: str
    seqno: str
    ordno: str
    account: Account
    price_type: str
    order_type: str
    def __init__(self, action: _Optional[str] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ..., id: _Optional[str] = ..., seqno: _Optional[str] = ..., ordno: _Optional[str] = ..., account: _Optional[_Union[Account, _Mapping]] = ..., price_type: _Optional[str] = ..., order_type: _Optional[str] = ...) -> None: ...

class ComboOrder(_message.Message):
    __slots__ = ("action", "price", "quantity", "id", "seqno", "ordno", "account", "price_type", "order_type")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    ORDNO_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    action: str
    price: float
    quantity: int
    id: str
    seqno: str
    ordno: str
    account: Account
    price_type: str
    order_type: str
    def __init__(self, action: _Optional[str] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ..., id: _Optional[str] = ..., seqno: _Optional[str] = ..., ordno: _Optional[str] = ..., account: _Optional[_Union[Account, _Mapping]] = ..., price_type: _Optional[str] = ..., order_type: _Optional[str] = ...) -> None: ...

class OrderStatus(_message.Message):
    __slots__ = ("id", "status", "status_code", "order_datetime", "deal_quantity", "cancel_quantity")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    ORDER_DATETIME_FIELD_NUMBER: _ClassVar[int]
    DEAL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CANCEL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: str
    status_code: str
    order_datetime: str
    deal_quantity: int
    cancel_quantity: int
    def __init__(self, id: _Optional[str] = ..., status: _Optional[str] = ..., status_code: _Optional[str] = ..., order_datetime: _Optional[str] = ..., deal_quantity: _Optional[int] = ..., cancel_quantity: _Optional[int] = ...) -> None: ...

class Trade(_message.Message):
    __slots__ = ("contract", "order", "status")
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    contract: Contract
    order: Order
    status: OrderStatus
    def __init__(self, contract: _Optional[_Union[Contract, _Mapping]] = ..., order: _Optional[_Union[Order, _Mapping]] = ..., status: _Optional[_Union[OrderStatus, _Mapping]] = ...) -> None: ...

class ComboTrade(_message.Message):
    __slots__ = ("contract", "order", "status")
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    contract: ComboContract
    order: ComboOrder
    status: OrderStatus
    def __init__(self, contract: _Optional[_Union[ComboContract, _Mapping]] = ..., order: _Optional[_Union[ComboOrder, _Mapping]] = ..., status: _Optional[_Union[OrderStatus, _Mapping]] = ...) -> None: ...

class PlaceOrderRequest(_message.Message):
    __slots__ = ("contract", "order")
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    contract: Contract
    order: Order
    def __init__(self, contract: _Optional[_Union[Contract, _Mapping]] = ..., order: _Optional[_Union[Order, _Mapping]] = ...) -> None: ...

class PlaceComboOrderRequest(_message.Message):
    __slots__ = ("combo_contract", "order")
    COMBO_CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    combo_contract: ComboContract
    order: ComboOrder
    def __init__(self, combo_contract: _Optional[_Union[ComboContract, _Mapping]] = ..., order: _Optional[_Union[ComboOrder, _Mapping]] = ...) -> None: ...

class UpdateOrderRequest(_message.Message):
    __slots__ = ("trade", "price", "quantity")
    TRADE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    trade: Trade
    price: float
    quantity: int
    def __init__(self, trade: _Optional[_Union[Trade, _Mapping]] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ...) -> None: ...

class CancelOrderRequest(_message.Message):
    __slots__ = ("trade",)
    TRADE_FIELD_NUMBER: _ClassVar[int]
    trade: Trade
    def __init__(self, trade: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class CancelComboOrderRequest(_message.Message):
    __slots__ = ("combotrade",)
    COMBOTRADE_FIELD_NUMBER: _ClassVar[int]
    combotrade: ComboTrade
    def __init__(self, combotrade: _Optional[_Union[ComboTrade, _Mapping]] = ...) -> None: ...

class UpdateStatusRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class ListTradesResponse(_message.Message):
    __slots__ = ("trades",)
    TRADES_FIELD_NUMBER: _ClassVar[int]
    trades: _containers.RepeatedCompositeFieldContainer[Trade]
    def __init__(self, trades: _Optional[_Iterable[_Union[Trade, _Mapping]]] = ...) -> None: ...

class ListComboTradesResponse(_message.Message):
    __slots__ = ("combo_trades",)
    COMBO_TRADES_FIELD_NUMBER: _ClassVar[int]
    combo_trades: _containers.RepeatedCompositeFieldContainer[ComboTrade]
    def __init__(self, combo_trades: _Optional[_Iterable[_Union[ComboTrade, _Mapping]]] = ...) -> None: ...

class GetOrderDealRecordsRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class GetOrderDealRecordsResponse(_message.Message):
    __slots__ = ("records",)
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    records: _containers.RepeatedCompositeFieldContainer[OrderDealRecord]
    def __init__(self, records: _Optional[_Iterable[_Union[OrderDealRecord, _Mapping]]] = ...) -> None: ...

class OrderDealRecord(_message.Message):
    __slots__ = ("code", "action", "price", "quantity", "ts")
    CODE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    code: str
    action: str
    price: float
    quantity: int
    ts: str
    def __init__(self, code: _Optional[str] = ..., action: _Optional[str] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ..., ts: _Optional[str] = ...) -> None: ...

class ListPositionsRequest(_message.Message):
    __slots__ = ("account", "unit")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    unit: str
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ..., unit: _Optional[str] = ...) -> None: ...

class StockPosition(_message.Message):
    __slots__ = ("id", "code", "direction", "quantity", "price", "last_price", "pnl", "yd_quantity", "cond", "margin_purchase_amount", "collateral", "short_sale_margin", "interest")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    YD_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    COND_FIELD_NUMBER: _ClassVar[int]
    MARGIN_PURCHASE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    COLLATERAL_FIELD_NUMBER: _ClassVar[int]
    SHORT_SALE_MARGIN_FIELD_NUMBER: _ClassVar[int]
    INTEREST_FIELD_NUMBER: _ClassVar[int]
    id: int
    code: str
    direction: str
    quantity: int
    price: float
    last_price: float
    pnl: float
    yd_quantity: int
    cond: str
    margin_purchase_amount: int
    collateral: int
    short_sale_margin: int
    interest: int
    def __init__(self, id: _Optional[int] = ..., code: _Optional[str] = ..., direction: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., last_price: _Optional[float] = ..., pnl: _Optional[float] = ..., yd_quantity: _Optional[int] = ..., cond: _Optional[str] = ..., margin_purchase_amount: _Optional[int] = ..., collateral: _Optional[int] = ..., short_sale_margin: _Optional[int] = ..., interest: _Optional[int] = ...) -> None: ...

class FuturePosition(_message.Message):
    __slots__ = ("id", "code", "direction", "quantity", "price", "last_price", "pnl")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    id: int
    code: str
    direction: str
    quantity: int
    price: float
    last_price: float
    pnl: float
    def __init__(self, id: _Optional[int] = ..., code: _Optional[str] = ..., direction: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., last_price: _Optional[float] = ..., pnl: _Optional[float] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ("stock_position", "future_position")
    STOCK_POSITION_FIELD_NUMBER: _ClassVar[int]
    FUTURE_POSITION_FIELD_NUMBER: _ClassVar[int]
    stock_position: StockPosition
    future_position: FuturePosition
    def __init__(self, stock_position: _Optional[_Union[StockPosition, _Mapping]] = ..., future_position: _Optional[_Union[FuturePosition, _Mapping]] = ...) -> None: ...

class ListPositionsResponse(_message.Message):
    __slots__ = ("positions",)
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    positions: _containers.RepeatedCompositeFieldContainer[Position]
    def __init__(self, positions: _Optional[_Iterable[_Union[Position, _Mapping]]] = ...) -> None: ...

class ListPositionDetailRequest(_message.Message):
    __slots__ = ("account", "detail_id")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DETAIL_ID_FIELD_NUMBER: _ClassVar[int]
    account: Account
    detail_id: int
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ..., detail_id: _Optional[int] = ...) -> None: ...

class StockPositionDetail(_message.Message):
    __slots__ = ("date", "code", "quantity", "price", "last_price", "pnl")
    DATE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    date: str
    code: str
    quantity: int
    price: float
    last_price: float
    pnl: float
    def __init__(self, date: _Optional[str] = ..., code: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., last_price: _Optional[float] = ..., pnl: _Optional[float] = ...) -> None: ...

class FuturePositionDetail(_message.Message):
    __slots__ = ("date", "code", "quantity", "price", "last_price", "pnl", "entry_quantity")
    DATE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    ENTRY_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    date: str
    code: str
    quantity: int
    price: float
    last_price: float
    pnl: float
    entry_quantity: int
    def __init__(self, date: _Optional[str] = ..., code: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., last_price: _Optional[float] = ..., pnl: _Optional[float] = ..., entry_quantity: _Optional[int] = ...) -> None: ...

class PositionDetail(_message.Message):
    __slots__ = ("stock_detail", "future_detail")
    STOCK_DETAIL_FIELD_NUMBER: _ClassVar[int]
    FUTURE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    stock_detail: StockPositionDetail
    future_detail: FuturePositionDetail
    def __init__(self, stock_detail: _Optional[_Union[StockPositionDetail, _Mapping]] = ..., future_detail: _Optional[_Union[FuturePositionDetail, _Mapping]] = ...) -> None: ...

class ListPositionDetailResponse(_message.Message):
    __slots__ = ("details",)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _containers.RepeatedCompositeFieldContainer[PositionDetail]
    def __init__(self, details: _Optional[_Iterable[_Union[PositionDetail, _Mapping]]] = ...) -> None: ...

class ListProfitLossRequest(_message.Message):
    __slots__ = ("account", "begin_date", "end_date")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    BEGIN_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    account: Account
    begin_date: str
    end_date: str
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ..., begin_date: _Optional[str] = ..., end_date: _Optional[str] = ...) -> None: ...

class StockProfitLoss(_message.Message):
    __slots__ = ("dseq", "code", "quantity", "price", "pnl", "pr_ratio", "cond", "date", "seqno")
    DSEQ_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    PR_RATIO_FIELD_NUMBER: _ClassVar[int]
    COND_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    dseq: str
    code: str
    quantity: int
    price: float
    pnl: float
    pr_ratio: float
    cond: str
    date: str
    seqno: str
    def __init__(self, dseq: _Optional[str] = ..., code: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., pnl: _Optional[float] = ..., pr_ratio: _Optional[float] = ..., cond: _Optional[str] = ..., date: _Optional[str] = ..., seqno: _Optional[str] = ...) -> None: ...

class FutureProfitLoss(_message.Message):
    __slots__ = ("date", "code", "quantity", "entry_price", "cover_price", "direction", "pnl", "tax", "fee")
    DATE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ENTRY_PRICE_FIELD_NUMBER: _ClassVar[int]
    COVER_PRICE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    date: str
    code: str
    quantity: int
    entry_price: float
    cover_price: float
    direction: str
    pnl: float
    tax: int
    fee: int
    def __init__(self, date: _Optional[str] = ..., code: _Optional[str] = ..., quantity: _Optional[int] = ..., entry_price: _Optional[float] = ..., cover_price: _Optional[float] = ..., direction: _Optional[str] = ..., pnl: _Optional[float] = ..., tax: _Optional[int] = ..., fee: _Optional[int] = ...) -> None: ...

class ProfitLoss(_message.Message):
    __slots__ = ("stock_pnl", "future_pnl")
    STOCK_PNL_FIELD_NUMBER: _ClassVar[int]
    FUTURE_PNL_FIELD_NUMBER: _ClassVar[int]
    stock_pnl: StockProfitLoss
    future_pnl: FutureProfitLoss
    def __init__(self, stock_pnl: _Optional[_Union[StockProfitLoss, _Mapping]] = ..., future_pnl: _Optional[_Union[FutureProfitLoss, _Mapping]] = ...) -> None: ...

class ListProfitLossResponse(_message.Message):
    __slots__ = ("profit_losses",)
    PROFIT_LOSSES_FIELD_NUMBER: _ClassVar[int]
    profit_losses: _containers.RepeatedCompositeFieldContainer[ProfitLoss]
    def __init__(self, profit_losses: _Optional[_Iterable[_Union[ProfitLoss, _Mapping]]] = ...) -> None: ...

class ListProfitLossDetailRequest(_message.Message):
    __slots__ = ("account", "detail_id")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    DETAIL_ID_FIELD_NUMBER: _ClassVar[int]
    account: Account
    detail_id: int
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ..., detail_id: _Optional[int] = ...) -> None: ...

class StockProfitDetail(_message.Message):
    __slots__ = ("price", "cost", "interest")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    INTEREST_FIELD_NUMBER: _ClassVar[int]
    price: float
    cost: int
    interest: int
    def __init__(self, price: _Optional[float] = ..., cost: _Optional[int] = ..., interest: _Optional[int] = ...) -> None: ...

class FutureProfitDetail(_message.Message):
    __slots__ = ("direction", "entry_date", "entry_price", "cover_price", "pnl")
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ENTRY_DATE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_PRICE_FIELD_NUMBER: _ClassVar[int]
    COVER_PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    direction: str
    entry_date: str
    entry_price: float
    cover_price: float
    pnl: int
    def __init__(self, direction: _Optional[str] = ..., entry_date: _Optional[str] = ..., entry_price: _Optional[float] = ..., cover_price: _Optional[float] = ..., pnl: _Optional[int] = ...) -> None: ...

class ProfitDetail(_message.Message):
    __slots__ = ("stock_detail", "future_detail")
    STOCK_DETAIL_FIELD_NUMBER: _ClassVar[int]
    FUTURE_DETAIL_FIELD_NUMBER: _ClassVar[int]
    stock_detail: StockProfitDetail
    future_detail: FutureProfitDetail
    def __init__(self, stock_detail: _Optional[_Union[StockProfitDetail, _Mapping]] = ..., future_detail: _Optional[_Union[FutureProfitDetail, _Mapping]] = ...) -> None: ...

class ListProfitLossDetailResponse(_message.Message):
    __slots__ = ("details",)
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    details: _containers.RepeatedCompositeFieldContainer[ProfitDetail]
    def __init__(self, details: _Optional[_Iterable[_Union[ProfitDetail, _Mapping]]] = ...) -> None: ...

class ListProfitLossSummaryRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class StockProfitLossSummary(_message.Message):
    __slots__ = ("entry_cost", "cover_cost")
    ENTRY_COST_FIELD_NUMBER: _ClassVar[int]
    COVER_COST_FIELD_NUMBER: _ClassVar[int]
    entry_cost: int
    cover_cost: int
    def __init__(self, entry_cost: _Optional[int] = ..., cover_cost: _Optional[int] = ...) -> None: ...

class FutureProfitLossSummary(_message.Message):
    __slots__ = ("direction", "tax", "fee")
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    direction: str
    tax: int
    fee: int
    def __init__(self, direction: _Optional[str] = ..., tax: _Optional[int] = ..., fee: _Optional[int] = ...) -> None: ...

class ProfitLossSummary(_message.Message):
    __slots__ = ("stock_summary", "future_summary")
    STOCK_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    FUTURE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    stock_summary: StockProfitLossSummary
    future_summary: FutureProfitLossSummary
    def __init__(self, stock_summary: _Optional[_Union[StockProfitLossSummary, _Mapping]] = ..., future_summary: _Optional[_Union[FutureProfitLossSummary, _Mapping]] = ...) -> None: ...

class ListProfitLossSummaryResponse(_message.Message):
    __slots__ = ("summaries",)
    SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    summaries: _containers.RepeatedCompositeFieldContainer[ProfitLossSummary]
    def __init__(self, summaries: _Optional[_Iterable[_Union[ProfitLossSummary, _Mapping]]] = ...) -> None: ...

class GetSettlementsRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class Settlement(_message.Message):
    __slots__ = ("date", "amount", "t_money", "t_day", "t1_money", "t1_day", "t2_money", "t2_day")
    DATE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    T_MONEY_FIELD_NUMBER: _ClassVar[int]
    T_DAY_FIELD_NUMBER: _ClassVar[int]
    T1_MONEY_FIELD_NUMBER: _ClassVar[int]
    T1_DAY_FIELD_NUMBER: _ClassVar[int]
    T2_MONEY_FIELD_NUMBER: _ClassVar[int]
    T2_DAY_FIELD_NUMBER: _ClassVar[int]
    date: str
    amount: float
    t_money: float
    t_day: str
    t1_money: float
    t1_day: str
    t2_money: float
    t2_day: str
    def __init__(self, date: _Optional[str] = ..., amount: _Optional[float] = ..., t_money: _Optional[float] = ..., t_day: _Optional[str] = ..., t1_money: _Optional[float] = ..., t1_day: _Optional[str] = ..., t2_money: _Optional[float] = ..., t2_day: _Optional[str] = ...) -> None: ...

class GetSettlementsResponse(_message.Message):
    __slots__ = ("settlements",)
    SETTLEMENTS_FIELD_NUMBER: _ClassVar[int]
    settlements: _containers.RepeatedCompositeFieldContainer[Settlement]
    def __init__(self, settlements: _Optional[_Iterable[_Union[Settlement, _Mapping]]] = ...) -> None: ...

class GetMarginRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class Margin(_message.Message):
    __slots__ = ("equity", "available_margin", "initial_margin", "maintenance_margin")
    EQUITY_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_MARGIN_FIELD_NUMBER: _ClassVar[int]
    INITIAL_MARGIN_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_MARGIN_FIELD_NUMBER: _ClassVar[int]
    equity: float
    available_margin: float
    initial_margin: float
    maintenance_margin: float
    def __init__(self, equity: _Optional[float] = ..., available_margin: _Optional[float] = ..., initial_margin: _Optional[float] = ..., maintenance_margin: _Optional[float] = ...) -> None: ...

class GetTradingLimitsRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class TradingLimits(_message.Message):
    __slots__ = ("trading_limit", "trading_used", "trading_available", "margin_limit", "margin_used", "margin_available", "short_limit", "short_used", "short_available")
    TRADING_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TRADING_USED_FIELD_NUMBER: _ClassVar[int]
    TRADING_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    MARGIN_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MARGIN_USED_FIELD_NUMBER: _ClassVar[int]
    MARGIN_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SHORT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SHORT_USED_FIELD_NUMBER: _ClassVar[int]
    SHORT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    trading_limit: int
    trading_used: int
    trading_available: int
    margin_limit: int
    margin_used: int
    margin_available: int
    short_limit: int
    short_used: int
    short_available: int
    def __init__(self, trading_limit: _Optional[int] = ..., trading_used: _Optional[int] = ..., trading_available: _Optional[int] = ..., margin_limit: _Optional[int] = ..., margin_used: _Optional[int] = ..., margin_available: _Optional[int] = ..., short_limit: _Optional[int] = ..., short_used: _Optional[int] = ..., short_available: _Optional[int] = ...) -> None: ...

class GetStockReserveSummaryRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class ReserveStocksSummaryResponse(_message.Message):
    __slots__ = ("response_json",)
    RESPONSE_JSON_FIELD_NUMBER: _ClassVar[int]
    response_json: str
    def __init__(self, response_json: _Optional[str] = ...) -> None: ...

class GetStockReserveDetailRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class ReserveStocksDetailResponse(_message.Message):
    __slots__ = ("response_json",)
    RESPONSE_JSON_FIELD_NUMBER: _ClassVar[int]
    response_json: str
    def __init__(self, response_json: _Optional[str] = ...) -> None: ...

class ReserveStockRequest(_message.Message):
    __slots__ = ("account", "contract", "share")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    SHARE_FIELD_NUMBER: _ClassVar[int]
    account: Account
    contract: Contract
    share: int
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ..., contract: _Optional[_Union[Contract, _Mapping]] = ..., share: _Optional[int] = ...) -> None: ...

class ReserveStockResponse(_message.Message):
    __slots__ = ("response_json",)
    RESPONSE_JSON_FIELD_NUMBER: _ClassVar[int]
    response_json: str
    def __init__(self, response_json: _Optional[str] = ...) -> None: ...

class GetEarmarkingDetailRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class EarmarkStocksDetailResponse(_message.Message):
    __slots__ = ("response_json",)
    RESPONSE_JSON_FIELD_NUMBER: _ClassVar[int]
    response_json: str
    def __init__(self, response_json: _Optional[str] = ...) -> None: ...

class ReserveEarmarkingRequest(_message.Message):
    __slots__ = ("account", "contract", "share", "price")
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    SHARE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    account: Account
    contract: Contract
    share: int
    price: float
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ..., contract: _Optional[_Union[Contract, _Mapping]] = ..., share: _Optional[int] = ..., price: _Optional[float] = ...) -> None: ...

class ReserveEarmarkingResponse(_message.Message):
    __slots__ = ("response_json",)
    RESPONSE_JSON_FIELD_NUMBER: _ClassVar[int]
    response_json: str
    def __init__(self, response_json: _Optional[str] = ...) -> None: ...

class GetSnapshotsRequest(_message.Message):
    __slots__ = ("contract_codes",)
    CONTRACT_CODES_FIELD_NUMBER: _ClassVar[int]
    contract_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, contract_codes: _Optional[_Iterable[str]] = ...) -> None: ...

class GetSnapshotsResponse(_message.Message):
    __slots__ = ("snapshots",)
    SNAPSHOTS_FIELD_NUMBER: _ClassVar[int]
    snapshots: _containers.RepeatedCompositeFieldContainer[Snapshot]
    def __init__(self, snapshots: _Optional[_Iterable[_Union[Snapshot, _Mapping]]] = ...) -> None: ...

class Snapshot(_message.Message):
    __slots__ = ("ts", "code", "exchange", "open", "high", "low", "close", "change_price", "change_rate", "average_price", "volume", "total_volume", "amount", "total_amount", "buy_price", "buy_volume", "sell_price", "sell_volume")
    TS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_PRICE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_RATE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_PRICE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BUY_PRICE_FIELD_NUMBER: _ClassVar[int]
    BUY_VOLUME_FIELD_NUMBER: _ClassVar[int]
    SELL_PRICE_FIELD_NUMBER: _ClassVar[int]
    SELL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    ts: int
    code: str
    exchange: str
    open: float
    high: float
    low: float
    close: float
    change_price: float
    change_rate: float
    average_price: float
    volume: int
    total_volume: int
    amount: int
    total_amount: int
    buy_price: float
    buy_volume: int
    sell_price: float
    sell_volume: int
    def __init__(self, ts: _Optional[int] = ..., code: _Optional[str] = ..., exchange: _Optional[str] = ..., open: _Optional[float] = ..., high: _Optional[float] = ..., low: _Optional[float] = ..., close: _Optional[float] = ..., change_price: _Optional[float] = ..., change_rate: _Optional[float] = ..., average_price: _Optional[float] = ..., volume: _Optional[int] = ..., total_volume: _Optional[int] = ..., amount: _Optional[int] = ..., total_amount: _Optional[int] = ..., buy_price: _Optional[float] = ..., buy_volume: _Optional[int] = ..., sell_price: _Optional[float] = ..., sell_volume: _Optional[int] = ...) -> None: ...

class GetTicksRequest(_message.Message):
    __slots__ = ("contract_code", "date")
    CONTRACT_CODE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    contract_code: str
    date: str
    def __init__(self, contract_code: _Optional[str] = ..., date: _Optional[str] = ...) -> None: ...

class Ticks(_message.Message):
    __slots__ = ("ts", "close", "volume", "bid_price", "bid_volume", "ask_price", "ask_volume", "tick_type")
    TS_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    BID_PRICE_FIELD_NUMBER: _ClassVar[int]
    BID_VOLUME_FIELD_NUMBER: _ClassVar[int]
    ASK_PRICE_FIELD_NUMBER: _ClassVar[int]
    ASK_VOLUME_FIELD_NUMBER: _ClassVar[int]
    TICK_TYPE_FIELD_NUMBER: _ClassVar[int]
    ts: _containers.RepeatedScalarFieldContainer[int]
    close: _containers.RepeatedScalarFieldContainer[float]
    volume: _containers.RepeatedScalarFieldContainer[int]
    bid_price: _containers.RepeatedScalarFieldContainer[float]
    bid_volume: _containers.RepeatedScalarFieldContainer[int]
    ask_price: _containers.RepeatedScalarFieldContainer[float]
    ask_volume: _containers.RepeatedScalarFieldContainer[int]
    tick_type: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, ts: _Optional[_Iterable[int]] = ..., close: _Optional[_Iterable[float]] = ..., volume: _Optional[_Iterable[int]] = ..., bid_price: _Optional[_Iterable[float]] = ..., bid_volume: _Optional[_Iterable[int]] = ..., ask_price: _Optional[_Iterable[float]] = ..., ask_volume: _Optional[_Iterable[int]] = ..., tick_type: _Optional[_Iterable[int]] = ...) -> None: ...

class GetKbarsRequest(_message.Message):
    __slots__ = ("contract_code", "start_date", "end_date")
    CONTRACT_CODE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    contract_code: str
    start_date: str
    end_date: str
    def __init__(self, contract_code: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ...) -> None: ...

class Kbars(_message.Message):
    __slots__ = ("ts", "open", "high", "low", "close", "volume", "amount")
    TS_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ts: _containers.RepeatedScalarFieldContainer[int]
    open: _containers.RepeatedScalarFieldContainer[float]
    high: _containers.RepeatedScalarFieldContainer[float]
    low: _containers.RepeatedScalarFieldContainer[float]
    close: _containers.RepeatedScalarFieldContainer[float]
    volume: _containers.RepeatedScalarFieldContainer[int]
    amount: _containers.RepeatedScalarFieldContainer[float]
    def __init__(self, ts: _Optional[_Iterable[int]] = ..., open: _Optional[_Iterable[float]] = ..., high: _Optional[_Iterable[float]] = ..., low: _Optional[_Iterable[float]] = ..., close: _Optional[_Iterable[float]] = ..., volume: _Optional[_Iterable[int]] = ..., amount: _Optional[_Iterable[float]] = ...) -> None: ...

class GetDailyQuotesRequest(_message.Message):
    __slots__ = ("date",)
    DATE_FIELD_NUMBER: _ClassVar[int]
    date: str
    def __init__(self, date: _Optional[str] = ...) -> None: ...

class DailyQuotes(_message.Message):
    __slots__ = ("code", "open", "high", "low", "close", "volume")
    CODE_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    code: _containers.RepeatedScalarFieldContainer[str]
    open: _containers.RepeatedScalarFieldContainer[float]
    high: _containers.RepeatedScalarFieldContainer[float]
    low: _containers.RepeatedScalarFieldContainer[float]
    close: _containers.RepeatedScalarFieldContainer[float]
    volume: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, code: _Optional[_Iterable[str]] = ..., open: _Optional[_Iterable[float]] = ..., high: _Optional[_Iterable[float]] = ..., low: _Optional[_Iterable[float]] = ..., close: _Optional[_Iterable[float]] = ..., volume: _Optional[_Iterable[int]] = ...) -> None: ...

class CreditEnquiresRequest(_message.Message):
    __slots__ = ("contract_codes",)
    CONTRACT_CODES_FIELD_NUMBER: _ClassVar[int]
    contract_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, contract_codes: _Optional[_Iterable[str]] = ...) -> None: ...

class CreditEnquiresResponse(_message.Message):
    __slots__ = ("credit_enquires",)
    CREDIT_ENQUIRES_FIELD_NUMBER: _ClassVar[int]
    credit_enquires: _containers.RepeatedCompositeFieldContainer[CreditEnquire]
    def __init__(self, credit_enquires: _Optional[_Iterable[_Union[CreditEnquire, _Mapping]]] = ...) -> None: ...

class CreditEnquire(_message.Message):
    __slots__ = ("stock_id", "margin_unit", "short_unit")
    STOCK_ID_FIELD_NUMBER: _ClassVar[int]
    MARGIN_UNIT_FIELD_NUMBER: _ClassVar[int]
    SHORT_UNIT_FIELD_NUMBER: _ClassVar[int]
    stock_id: str
    margin_unit: int
    short_unit: int
    def __init__(self, stock_id: _Optional[str] = ..., margin_unit: _Optional[int] = ..., short_unit: _Optional[int] = ...) -> None: ...

class GetShortStockSourcesRequest(_message.Message):
    __slots__ = ("contract_codes",)
    CONTRACT_CODES_FIELD_NUMBER: _ClassVar[int]
    contract_codes: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, contract_codes: _Optional[_Iterable[str]] = ...) -> None: ...

class GetShortStockSourcesResponse(_message.Message):
    __slots__ = ("sources",)
    SOURCES_FIELD_NUMBER: _ClassVar[int]
    sources: _containers.RepeatedCompositeFieldContainer[ShortStockSource]
    def __init__(self, sources: _Optional[_Iterable[_Union[ShortStockSource, _Mapping]]] = ...) -> None: ...

class ShortStockSource(_message.Message):
    __slots__ = ("code", "short_stock_source", "ts")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SHORT_STOCK_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    code: str
    short_stock_source: int
    ts: int
    def __init__(self, code: _Optional[str] = ..., short_stock_source: _Optional[int] = ..., ts: _Optional[int] = ...) -> None: ...

class GetScannersRequest(_message.Message):
    __slots__ = ("scanner_type", "ascending", "date", "count")
    SCANNER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ASCENDING_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    scanner_type: str
    ascending: bool
    date: str
    count: int
    def __init__(self, scanner_type: _Optional[str] = ..., ascending: bool = ..., date: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class GetScannersResponse(_message.Message):
    __slots__ = ("scanners",)
    SCANNERS_FIELD_NUMBER: _ClassVar[int]
    scanners: _containers.RepeatedCompositeFieldContainer[ScannerItem]
    def __init__(self, scanners: _Optional[_Iterable[_Union[ScannerItem, _Mapping]]] = ...) -> None: ...

class ScannerItem(_message.Message):
    __slots__ = ("code", "name", "close", "change_price", "total_volume")
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_PRICE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    code: str
    name: str
    close: float
    change_price: float
    total_volume: int
    def __init__(self, code: _Optional[str] = ..., name: _Optional[str] = ..., close: _Optional[float] = ..., change_price: _Optional[float] = ..., total_volume: _Optional[int] = ...) -> None: ...

class Punish(_message.Message):
    __slots__ = ("code", "start_date", "end_date", "interval")
    CODE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    code: _containers.RepeatedScalarFieldContainer[str]
    start_date: _containers.RepeatedScalarFieldContainer[str]
    end_date: _containers.RepeatedScalarFieldContainer[str]
    interval: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, code: _Optional[_Iterable[str]] = ..., start_date: _Optional[_Iterable[str]] = ..., end_date: _Optional[_Iterable[str]] = ..., interval: _Optional[_Iterable[str]] = ...) -> None: ...

class Notice(_message.Message):
    __slots__ = ("code", "reason")
    CODE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    code: _containers.RepeatedScalarFieldContainer[str]
    reason: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, code: _Optional[_Iterable[str]] = ..., reason: _Optional[_Iterable[str]] = ...) -> None: ...

class FetchContractsRequest(_message.Message):
    __slots__ = ("contract_download",)
    CONTRACT_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    contract_download: bool
    def __init__(self, contract_download: bool = ...) -> None: ...

class ActivateCARequest(_message.Message):
    __slots__ = ("ca_path", "ca_passwd", "person_id")
    CA_PATH_FIELD_NUMBER: _ClassVar[int]
    CA_PASSWD_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    ca_path: str
    ca_passwd: str
    person_id: str
    def __init__(self, ca_path: _Optional[str] = ..., ca_passwd: _Optional[str] = ..., person_id: _Optional[str] = ...) -> None: ...

class ActivateCAResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class GetCAExpireTimeRequest(_message.Message):
    __slots__ = ("person_id",)
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    person_id: str
    def __init__(self, person_id: _Optional[str] = ...) -> None: ...

class GetCAExpireTimeResponse(_message.Message):
    __slots__ = ("expire_time",)
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    expire_time: str
    def __init__(self, expire_time: _Optional[str] = ...) -> None: ...

class SubscribeTradeRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class SubscribeTradeResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...

class UnsubscribeTradeRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class UnsubscribeTradeResponse(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
