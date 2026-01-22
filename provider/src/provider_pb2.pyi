from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

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

class Contract(_message.Message):
    __slots__ = ("security_type", "code", "symbol", "exchange", "name", "currency", "limit_up", "limit_down", "reference", "update_date", "day_trade")
    SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_UP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_DOWN_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DATE_FIELD_NUMBER: _ClassVar[int]
    DAY_TRADE_FIELD_NUMBER: _ClassVar[int]
    security_type: str
    code: str
    symbol: str
    exchange: str
    name: str
    currency: str
    limit_up: float
    limit_down: float
    reference: float
    update_date: str
    day_trade: str
    def __init__(self, security_type: _Optional[str] = ..., code: _Optional[str] = ..., symbol: _Optional[str] = ..., exchange: _Optional[str] = ..., name: _Optional[str] = ..., currency: _Optional[str] = ..., limit_up: _Optional[float] = ..., limit_down: _Optional[float] = ..., reference: _Optional[float] = ..., update_date: _Optional[str] = ..., day_trade: _Optional[str] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ("action", "price", "quantity", "price_type", "order_type", "order_lot", "order_cond", "id", "seqno", "ordno", "account", "custom_field")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_LOT_FIELD_NUMBER: _ClassVar[int]
    ORDER_COND_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    ORDNO_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_FIELD_NUMBER: _ClassVar[int]
    action: str
    price: float
    quantity: int
    price_type: str
    order_type: str
    order_lot: str
    order_cond: str
    id: str
    seqno: str
    ordno: str
    account: Account
    custom_field: str
    def __init__(self, action: _Optional[str] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ..., price_type: _Optional[str] = ..., order_type: _Optional[str] = ..., order_lot: _Optional[str] = ..., order_cond: _Optional[str] = ..., id: _Optional[str] = ..., seqno: _Optional[str] = ..., ordno: _Optional[str] = ..., account: _Optional[_Union[Account, _Mapping]] = ..., custom_field: _Optional[str] = ...) -> None: ...

class Trade(_message.Message):
    __slots__ = ("id", "status", "status_code", "order_ts", "msg", "price", "quantity", "filled_quantity", "cancelled_quantity", "ordno", "contract", "order")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    ORDER_TS_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    FILLED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CANCELLED_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ORDNO_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: str
    status_code: str
    order_ts: int
    msg: str
    price: float
    quantity: int
    filled_quantity: int
    cancelled_quantity: int
    ordno: str
    contract: Contract
    order: Order
    def __init__(self, id: _Optional[str] = ..., status: _Optional[str] = ..., status_code: _Optional[str] = ..., order_ts: _Optional[int] = ..., msg: _Optional[str] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ..., filled_quantity: _Optional[int] = ..., cancelled_quantity: _Optional[int] = ..., ordno: _Optional[str] = ..., contract: _Optional[_Union[Contract, _Mapping]] = ..., order: _Optional[_Union[Order, _Mapping]] = ...) -> None: ...

class Tick(_message.Message):
    __slots__ = ("code", "datetime", "open", "avg_price", "close", "high", "low", "amount", "total_amount", "volume", "total_volume", "tick_type", "chg_type", "price_chg", "pct_chg", "bid_side_total_vol", "ask_side_total_vol", "simtrade")
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATETIME_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    AVG_PRICE_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    TICK_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHG_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRICE_CHG_FIELD_NUMBER: _ClassVar[int]
    PCT_CHG_FIELD_NUMBER: _ClassVar[int]
    BID_SIDE_TOTAL_VOL_FIELD_NUMBER: _ClassVar[int]
    ASK_SIDE_TOTAL_VOL_FIELD_NUMBER: _ClassVar[int]
    SIMTRADE_FIELD_NUMBER: _ClassVar[int]
    code: str
    datetime: str
    open: float
    avg_price: float
    close: float
    high: float
    low: float
    amount: float
    total_amount: float
    volume: int
    total_volume: int
    tick_type: int
    chg_type: int
    price_chg: float
    pct_chg: float
    bid_side_total_vol: int
    ask_side_total_vol: int
    simtrade: bool
    def __init__(self, code: _Optional[str] = ..., datetime: _Optional[str] = ..., open: _Optional[float] = ..., avg_price: _Optional[float] = ..., close: _Optional[float] = ..., high: _Optional[float] = ..., low: _Optional[float] = ..., amount: _Optional[float] = ..., total_amount: _Optional[float] = ..., volume: _Optional[int] = ..., total_volume: _Optional[int] = ..., tick_type: _Optional[int] = ..., chg_type: _Optional[int] = ..., price_chg: _Optional[float] = ..., pct_chg: _Optional[float] = ..., bid_side_total_vol: _Optional[int] = ..., ask_side_total_vol: _Optional[int] = ..., simtrade: bool = ...) -> None: ...

class Kbar(_message.Message):
    __slots__ = ("ts", "open", "high", "low", "close", "volume", "amount")
    TS_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ts: int
    open: float
    high: float
    low: float
    close: float
    volume: int
    amount: float
    def __init__(self, ts: _Optional[int] = ..., open: _Optional[float] = ..., high: _Optional[float] = ..., low: _Optional[float] = ..., close: _Optional[float] = ..., volume: _Optional[int] = ..., amount: _Optional[float] = ...) -> None: ...

class Snapshot(_message.Message):
    __slots__ = ("ts", "code", "exchange", "open", "high", "low", "close", "average_price", "volume", "total_volume", "amount", "total_amount", "price_change", "price_change_percent", "buy_price", "buy_volume", "sell_price", "sell_volume")
    TS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_PRICE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_CHANGE_FIELD_NUMBER: _ClassVar[int]
    PRICE_CHANGE_PERCENT_FIELD_NUMBER: _ClassVar[int]
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
    average_price: float
    volume: int
    total_volume: int
    amount: float
    total_amount: float
    price_change: float
    price_change_percent: float
    buy_price: float
    buy_volume: int
    sell_price: float
    sell_volume: int
    def __init__(self, ts: _Optional[int] = ..., code: _Optional[str] = ..., exchange: _Optional[str] = ..., open: _Optional[float] = ..., high: _Optional[float] = ..., low: _Optional[float] = ..., close: _Optional[float] = ..., average_price: _Optional[float] = ..., volume: _Optional[int] = ..., total_volume: _Optional[int] = ..., amount: _Optional[float] = ..., total_amount: _Optional[float] = ..., price_change: _Optional[float] = ..., price_change_percent: _Optional[float] = ..., buy_price: _Optional[float] = ..., buy_volume: _Optional[int] = ..., sell_price: _Optional[float] = ..., sell_volume: _Optional[int] = ...) -> None: ...

class ProfitLoss(_message.Message):
    __slots__ = ("id", "code", "seqno", "dseq", "quantity", "price", "pnl", "pr_ratio", "cond", "date")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    DSEQ_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    PR_RATIO_FIELD_NUMBER: _ClassVar[int]
    COND_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    code: str
    seqno: str
    dseq: str
    quantity: int
    price: float
    pnl: float
    pr_ratio: float
    cond: str
    date: str
    def __init__(self, id: _Optional[int] = ..., code: _Optional[str] = ..., seqno: _Optional[str] = ..., dseq: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., pnl: _Optional[float] = ..., pr_ratio: _Optional[float] = ..., cond: _Optional[str] = ..., date: _Optional[str] = ...) -> None: ...

class Settlement(_message.Message):
    __slots__ = ("date", "amount", "t_time")
    DATE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    T_TIME_FIELD_NUMBER: _ClassVar[int]
    date: str
    amount: float
    t_time: str
    def __init__(self, date: _Optional[str] = ..., amount: _Optional[float] = ..., t_time: _Optional[str] = ...) -> None: ...

class Position(_message.Message):
    __slots__ = ("id", "code", "direction", "quantity", "price", "last_price", "pnl", "cond", "order_type", "price_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    COND_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: int
    code: str
    direction: str
    quantity: int
    price: float
    last_price: float
    pnl: float
    cond: str
    order_type: str
    price_type: str
    def __init__(self, id: _Optional[int] = ..., code: _Optional[str] = ..., direction: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., last_price: _Optional[float] = ..., pnl: _Optional[float] = ..., cond: _Optional[str] = ..., order_type: _Optional[str] = ..., price_type: _Optional[str] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ("person_id", "passwd", "api_key", "secret_key")
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    PASSWD_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    SECRET_KEY_FIELD_NUMBER: _ClassVar[int]
    person_id: str
    passwd: str
    api_key: str
    secret_key: str
    def __init__(self, person_id: _Optional[str] = ..., passwd: _Optional[str] = ..., api_key: _Optional[str] = ..., secret_key: _Optional[str] = ...) -> None: ...

class LoginResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: bool = ..., message: _Optional[str] = ...) -> None: ...

class ListAccountsResponse(_message.Message):
    __slots__ = ("accounts",)
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[Account]
    def __init__(self, accounts: _Optional[_Iterable[_Union[Account, _Mapping]]] = ...) -> None: ...

class AccountBalanceResponse(_message.Message):
    __slots__ = ("balance", "currency")
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    balance: float
    currency: str
    def __init__(self, balance: _Optional[float] = ..., currency: _Optional[str] = ...) -> None: ...

class ListSettlementsResponse(_message.Message):
    __slots__ = ("settlements",)
    SETTLEMENTS_FIELD_NUMBER: _ClassVar[int]
    settlements: _containers.RepeatedCompositeFieldContainer[Settlement]
    def __init__(self, settlements: _Optional[_Iterable[_Union[Settlement, _Mapping]]] = ...) -> None: ...

class ListProfitLossRequest(_message.Message):
    __slots__ = ("begin_date", "end_date")
    BEGIN_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    begin_date: str
    end_date: str
    def __init__(self, begin_date: _Optional[str] = ..., end_date: _Optional[str] = ...) -> None: ...

class ListProfitLossResponse(_message.Message):
    __slots__ = ("profit_loss",)
    PROFIT_LOSS_FIELD_NUMBER: _ClassVar[int]
    profit_loss: _containers.RepeatedCompositeFieldContainer[ProfitLoss]
    def __init__(self, profit_loss: _Optional[_Iterable[_Union[ProfitLoss, _Mapping]]] = ...) -> None: ...

class ListPositionsResponse(_message.Message):
    __slots__ = ("positions",)
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    positions: _containers.RepeatedCompositeFieldContainer[Position]
    def __init__(self, positions: _Optional[_Iterable[_Union[Position, _Mapping]]] = ...) -> None: ...

class PlaceOrderRequest(_message.Message):
    __slots__ = ("contract_code", "contract_security_type", "action", "price", "quantity", "price_type", "order_type", "order_lot", "account_id")
    CONTRACT_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_LOT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    contract_code: str
    contract_security_type: str
    action: str
    price: float
    quantity: int
    price_type: str
    order_type: str
    order_lot: str
    account_id: str
    def __init__(self, contract_code: _Optional[str] = ..., contract_security_type: _Optional[str] = ..., action: _Optional[str] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ..., price_type: _Optional[str] = ..., order_type: _Optional[str] = ..., order_lot: _Optional[str] = ..., account_id: _Optional[str] = ...) -> None: ...

class UpdateOrderRequest(_message.Message):
    __slots__ = ("trade_id", "price", "quantity")
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    price: float
    quantity: int
    def __init__(self, trade_id: _Optional[str] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ...) -> None: ...

class CancelOrderRequest(_message.Message):
    __slots__ = ("trade_id",)
    TRADE_ID_FIELD_NUMBER: _ClassVar[int]
    trade_id: str
    def __init__(self, trade_id: _Optional[str] = ...) -> None: ...

class TradeResponse(_message.Message):
    __slots__ = ("trade",)
    TRADE_FIELD_NUMBER: _ClassVar[int]
    trade: Trade
    def __init__(self, trade: _Optional[_Union[Trade, _Mapping]] = ...) -> None: ...

class ListTradesResponse(_message.Message):
    __slots__ = ("trades",)
    TRADES_FIELD_NUMBER: _ClassVar[int]
    trades: _containers.RepeatedCompositeFieldContainer[Trade]
    def __init__(self, trades: _Optional[_Iterable[_Union[Trade, _Mapping]]] = ...) -> None: ...

class GetTicksRequest(_message.Message):
    __slots__ = ("contract_code", "contract_security_type", "date")
    CONTRACT_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    contract_code: str
    contract_security_type: str
    date: str
    def __init__(self, contract_code: _Optional[str] = ..., contract_security_type: _Optional[str] = ..., date: _Optional[str] = ...) -> None: ...

class GetTicksResponse(_message.Message):
    __slots__ = ("ticks",)
    TICKS_FIELD_NUMBER: _ClassVar[int]
    ticks: _containers.RepeatedCompositeFieldContainer[Tick]
    def __init__(self, ticks: _Optional[_Iterable[_Union[Tick, _Mapping]]] = ...) -> None: ...

class GetKbarsRequest(_message.Message):
    __slots__ = ("contract_code", "contract_security_type", "start_date", "end_date")
    CONTRACT_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    contract_code: str
    contract_security_type: str
    start_date: str
    end_date: str
    def __init__(self, contract_code: _Optional[str] = ..., contract_security_type: _Optional[str] = ..., start_date: _Optional[str] = ..., end_date: _Optional[str] = ...) -> None: ...

class GetKbarsResponse(_message.Message):
    __slots__ = ("kbars",)
    KBARS_FIELD_NUMBER: _ClassVar[int]
    kbars: _containers.RepeatedCompositeFieldContainer[Kbar]
    def __init__(self, kbars: _Optional[_Iterable[_Union[Kbar, _Mapping]]] = ...) -> None: ...

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

class SubscribeQuoteRequest(_message.Message):
    __slots__ = ("contract_code", "contract_security_type", "quote_type")
    CONTRACT_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUOTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    contract_code: str
    contract_security_type: str
    quote_type: str
    def __init__(self, contract_code: _Optional[str] = ..., contract_security_type: _Optional[str] = ..., quote_type: _Optional[str] = ...) -> None: ...

class UnsubscribeQuoteRequest(_message.Message):
    __slots__ = ("contract_code", "contract_security_type", "quote_type")
    CONTRACT_CODE_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUOTE_TYPE_FIELD_NUMBER: _ClassVar[int]
    contract_code: str
    contract_security_type: str
    quote_type: str
    def __init__(self, contract_code: _Optional[str] = ..., contract_security_type: _Optional[str] = ..., quote_type: _Optional[str] = ...) -> None: ...
