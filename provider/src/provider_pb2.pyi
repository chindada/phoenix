from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_UNSPECIFIED: _ClassVar[Action]
    ACTION_BUY: _ClassVar[Action]
    ACTION_SELL: _ClassVar[Action]

class OrderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDER_TYPE_UNSPECIFIED: _ClassVar[OrderType]
    ORDER_TYPE_ROD: _ClassVar[OrderType]
    ORDER_TYPE_IOC: _ClassVar[OrderType]
    ORDER_TYPE_FOK: _ClassVar[OrderType]

class StockPriceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STOCK_PRICE_TYPE_UNSPECIFIED: _ClassVar[StockPriceType]
    STOCK_PRICE_TYPE_LMT: _ClassVar[StockPriceType]
    STOCK_PRICE_TYPE_MKT: _ClassVar[StockPriceType]
    STOCK_PRICE_TYPE_CLOSE: _ClassVar[StockPriceType]

class StockOrderLot(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STOCK_ORDER_LOT_UNSPECIFIED: _ClassVar[StockOrderLot]
    STOCK_ORDER_LOT_COMMON: _ClassVar[StockOrderLot]
    STOCK_ORDER_LOT_BLOCKTRADE: _ClassVar[StockOrderLot]
    STOCK_ORDER_LOT_FIXING: _ClassVar[StockOrderLot]
    STOCK_ORDER_LOT_ODD: _ClassVar[StockOrderLot]
    STOCK_ORDER_LOT_INTRADAY_ODD: _ClassVar[StockOrderLot]

class StockOrderCond(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STOCK_ORDER_COND_UNSPECIFIED: _ClassVar[StockOrderCond]
    STOCK_ORDER_COND_CASH: _ClassVar[StockOrderCond]
    STOCK_ORDER_COND_NETTING: _ClassVar[StockOrderCond]
    STOCK_ORDER_COND_MARGINTRADING: _ClassVar[StockOrderCond]
    STOCK_ORDER_COND_SHORTSELLING: _ClassVar[StockOrderCond]
    STOCK_ORDER_COND_EMERGING: _ClassVar[StockOrderCond]

class FuturesPriceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FUTURES_PRICE_TYPE_UNSPECIFIED: _ClassVar[FuturesPriceType]
    FUTURES_PRICE_TYPE_LMT: _ClassVar[FuturesPriceType]
    FUTURES_PRICE_TYPE_MKT: _ClassVar[FuturesPriceType]
    FUTURES_PRICE_TYPE_MKP: _ClassVar[FuturesPriceType]

class FuturesOCType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FUTURES_OCTYPE_UNSPECIFIED: _ClassVar[FuturesOCType]
    FUTURES_OCTYPE_AUTO: _ClassVar[FuturesOCType]
    FUTURES_OCTYPE_NEW: _ClassVar[FuturesOCType]
    FUTURES_OCTYPE_COVER: _ClassVar[FuturesOCType]
    FUTURES_OCTYPE_DAYTRADE: _ClassVar[FuturesOCType]

class SecurityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SECURITY_TYPE_UNSPECIFIED: _ClassVar[SecurityType]
    SECURITY_TYPE_IND: _ClassVar[SecurityType]
    SECURITY_TYPE_STK: _ClassVar[SecurityType]
    SECURITY_TYPE_FUT: _ClassVar[SecurityType]
    SECURITY_TYPE_OPT: _ClassVar[SecurityType]

class Exchange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EXCHANGE_UNSPECIFIED: _ClassVar[Exchange]
    EXCHANGE_TSE: _ClassVar[Exchange]
    EXCHANGE_OTC: _ClassVar[Exchange]
    EXCHANGE_OES: _ClassVar[Exchange]
    EXCHANGE_TAIFEX: _ClassVar[Exchange]

class Currency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CURRENCY_UNSPECIFIED: _ClassVar[Currency]
    CURRENCY_TWD: _ClassVar[Currency]
    CURRENCY_USD: _ClassVar[Currency]
    CURRENCY_HKD: _ClassVar[Currency]
    CURRENCY_GBP: _ClassVar[Currency]
    CURRENCY_AUD: _ClassVar[Currency]
    CURRENCY_CAD: _ClassVar[Currency]
    CURRENCY_SGD: _ClassVar[Currency]
    CURRENCY_CHF: _ClassVar[Currency]
    CURRENCY_JPY: _ClassVar[Currency]
    CURRENCY_ZAR: _ClassVar[Currency]
    CURRENCY_SEK: _ClassVar[Currency]
    CURRENCY_NZD: _ClassVar[Currency]
    CURRENCY_THB: _ClassVar[Currency]
    CURRENCY_PHP: _ClassVar[Currency]
    CURRENCY_IDR: _ClassVar[Currency]
    CURRENCY_EUR: _ClassVar[Currency]
    CURRENCY_KRW: _ClassVar[Currency]
    CURRENCY_VND: _ClassVar[Currency]
    CURRENCY_MYR: _ClassVar[Currency]
    CURRENCY_CNY: _ClassVar[Currency]

class OptionRight(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    OPTION_RIGHT_UNSPECIFIED: _ClassVar[OptionRight]
    OPTION_RIGHT_NO: _ClassVar[OptionRight]
    OPTION_RIGHT_CALL: _ClassVar[OptionRight]
    OPTION_RIGHT_PUT: _ClassVar[OptionRight]

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    STATUS_UNSPECIFIED: _ClassVar[Status]
    STATUS_CANCELLED: _ClassVar[Status]
    STATUS_FILLED: _ClassVar[Status]
    STATUS_PARTFILLED: _ClassVar[Status]
    STATUS_INACTIVE: _ClassVar[Status]
    STATUS_FAILED: _ClassVar[Status]
    STATUS_PENDINGSUBMIT: _ClassVar[Status]
    STATUS_PRESUBMITTED: _ClassVar[Status]
    STATUS_SUBMITTED: _ClassVar[Status]

class OrderState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ORDER_STATE_UNSPECIFIED: _ClassVar[OrderState]
    ORDER_STATE_STOCKDEAL: _ClassVar[OrderState]
    ORDER_STATE_STOCKORDER: _ClassVar[OrderState]
    ORDER_STATE_FUTURESORDER: _ClassVar[OrderState]
    ORDER_STATE_FUTURESDEAL: _ClassVar[OrderState]

class QuoteType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUOTE_TYPE_UNSPECIFIED: _ClassVar[QuoteType]
    QUOTE_TYPE_TICK: _ClassVar[QuoteType]
    QUOTE_TYPE_BIDASK: _ClassVar[QuoteType]
    QUOTE_TYPE_QUOTE: _ClassVar[QuoteType]

class QuoteVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    QUOTE_VERSION_UNSPECIFIED: _ClassVar[QuoteVersion]
    QUOTE_VERSION_V1: _ClassVar[QuoteVersion]

class DayTrade(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DAY_TRADE_UNSPECIFIED: _ClassVar[DayTrade]
    DAY_TRADE_YES: _ClassVar[DayTrade]
    DAY_TRADE_ONLYBUY: _ClassVar[DayTrade]
    DAY_TRADE_NO: _ClassVar[DayTrade]

class TickType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TICK_TYPE_UNSPECIFIED: _ClassVar[TickType]
    TICK_TYPE_NO: _ClassVar[TickType]
    TICK_TYPE_BUY: _ClassVar[TickType]
    TICK_TYPE_SELL: _ClassVar[TickType]

class ChangeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CHANGE_TYPE_UNSPECIFIED: _ClassVar[ChangeType]
    CHANGE_TYPE_LIMITUP: _ClassVar[ChangeType]
    CHANGE_TYPE_UP: _ClassVar[ChangeType]
    CHANGE_TYPE_UNCHANGED: _ClassVar[ChangeType]
    CHANGE_TYPE_DOWN: _ClassVar[ChangeType]
    CHANGE_TYPE_LIMITDOWN: _ClassVar[ChangeType]

class Unit(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNIT_UNSPECIFIED: _ClassVar[Unit]
    UNIT_COMMON: _ClassVar[Unit]
    UNIT_SHARE: _ClassVar[Unit]

class TradeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TRADE_TYPE_UNSPECIFIED: _ClassVar[TradeType]
    TRADE_TYPE_COMMON: _ClassVar[TradeType]
    TRADE_TYPE_DAYTRADE: _ClassVar[TradeType]

class ScannerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SCANNER_TYPE_UNSPECIFIED: _ClassVar[ScannerType]
    SCANNER_TYPE_CHANGEPERCENTRANK: _ClassVar[ScannerType]
    SCANNER_TYPE_CHANGEPRICERANK: _ClassVar[ScannerType]
    SCANNER_TYPE_DAYRANGERANK: _ClassVar[ScannerType]
    SCANNER_TYPE_VOLUMERANK: _ClassVar[ScannerType]
    SCANNER_TYPE_AMOUNTRANK: _ClassVar[ScannerType]
    SCANNER_TYPE_TICKCOUNTRANK: _ClassVar[ScannerType]

class TicksQueryType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TICKS_QUERY_TYPE_UNSPECIFIED: _ClassVar[TicksQueryType]
    TICKS_QUERY_TYPE_ALLDAY: _ClassVar[TicksQueryType]
    TICKS_QUERY_TYPE_RANGETIME: _ClassVar[TicksQueryType]
    TICKS_QUERY_TYPE_LASTCOUNT: _ClassVar[TicksQueryType]

class FetchStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FETCH_STATUS_UNSPECIFIED: _ClassVar[FetchStatus]
    FETCH_STATUS_SUCCESS: _ClassVar[FetchStatus]
    FETCH_STATUS_FAIL: _ClassVar[FetchStatus]
ACTION_UNSPECIFIED: Action
ACTION_BUY: Action
ACTION_SELL: Action
ORDER_TYPE_UNSPECIFIED: OrderType
ORDER_TYPE_ROD: OrderType
ORDER_TYPE_IOC: OrderType
ORDER_TYPE_FOK: OrderType
STOCK_PRICE_TYPE_UNSPECIFIED: StockPriceType
STOCK_PRICE_TYPE_LMT: StockPriceType
STOCK_PRICE_TYPE_MKT: StockPriceType
STOCK_PRICE_TYPE_CLOSE: StockPriceType
STOCK_ORDER_LOT_UNSPECIFIED: StockOrderLot
STOCK_ORDER_LOT_COMMON: StockOrderLot
STOCK_ORDER_LOT_BLOCKTRADE: StockOrderLot
STOCK_ORDER_LOT_FIXING: StockOrderLot
STOCK_ORDER_LOT_ODD: StockOrderLot
STOCK_ORDER_LOT_INTRADAY_ODD: StockOrderLot
STOCK_ORDER_COND_UNSPECIFIED: StockOrderCond
STOCK_ORDER_COND_CASH: StockOrderCond
STOCK_ORDER_COND_NETTING: StockOrderCond
STOCK_ORDER_COND_MARGINTRADING: StockOrderCond
STOCK_ORDER_COND_SHORTSELLING: StockOrderCond
STOCK_ORDER_COND_EMERGING: StockOrderCond
FUTURES_PRICE_TYPE_UNSPECIFIED: FuturesPriceType
FUTURES_PRICE_TYPE_LMT: FuturesPriceType
FUTURES_PRICE_TYPE_MKT: FuturesPriceType
FUTURES_PRICE_TYPE_MKP: FuturesPriceType
FUTURES_OCTYPE_UNSPECIFIED: FuturesOCType
FUTURES_OCTYPE_AUTO: FuturesOCType
FUTURES_OCTYPE_NEW: FuturesOCType
FUTURES_OCTYPE_COVER: FuturesOCType
FUTURES_OCTYPE_DAYTRADE: FuturesOCType
SECURITY_TYPE_UNSPECIFIED: SecurityType
SECURITY_TYPE_IND: SecurityType
SECURITY_TYPE_STK: SecurityType
SECURITY_TYPE_FUT: SecurityType
SECURITY_TYPE_OPT: SecurityType
EXCHANGE_UNSPECIFIED: Exchange
EXCHANGE_TSE: Exchange
EXCHANGE_OTC: Exchange
EXCHANGE_OES: Exchange
EXCHANGE_TAIFEX: Exchange
CURRENCY_UNSPECIFIED: Currency
CURRENCY_TWD: Currency
CURRENCY_USD: Currency
CURRENCY_HKD: Currency
CURRENCY_GBP: Currency
CURRENCY_AUD: Currency
CURRENCY_CAD: Currency
CURRENCY_SGD: Currency
CURRENCY_CHF: Currency
CURRENCY_JPY: Currency
CURRENCY_ZAR: Currency
CURRENCY_SEK: Currency
CURRENCY_NZD: Currency
CURRENCY_THB: Currency
CURRENCY_PHP: Currency
CURRENCY_IDR: Currency
CURRENCY_EUR: Currency
CURRENCY_KRW: Currency
CURRENCY_VND: Currency
CURRENCY_MYR: Currency
CURRENCY_CNY: Currency
OPTION_RIGHT_UNSPECIFIED: OptionRight
OPTION_RIGHT_NO: OptionRight
OPTION_RIGHT_CALL: OptionRight
OPTION_RIGHT_PUT: OptionRight
STATUS_UNSPECIFIED: Status
STATUS_CANCELLED: Status
STATUS_FILLED: Status
STATUS_PARTFILLED: Status
STATUS_INACTIVE: Status
STATUS_FAILED: Status
STATUS_PENDINGSUBMIT: Status
STATUS_PRESUBMITTED: Status
STATUS_SUBMITTED: Status
ORDER_STATE_UNSPECIFIED: OrderState
ORDER_STATE_STOCKDEAL: OrderState
ORDER_STATE_STOCKORDER: OrderState
ORDER_STATE_FUTURESORDER: OrderState
ORDER_STATE_FUTURESDEAL: OrderState
QUOTE_TYPE_UNSPECIFIED: QuoteType
QUOTE_TYPE_TICK: QuoteType
QUOTE_TYPE_BIDASK: QuoteType
QUOTE_TYPE_QUOTE: QuoteType
QUOTE_VERSION_UNSPECIFIED: QuoteVersion
QUOTE_VERSION_V1: QuoteVersion
DAY_TRADE_UNSPECIFIED: DayTrade
DAY_TRADE_YES: DayTrade
DAY_TRADE_ONLYBUY: DayTrade
DAY_TRADE_NO: DayTrade
TICK_TYPE_UNSPECIFIED: TickType
TICK_TYPE_NO: TickType
TICK_TYPE_BUY: TickType
TICK_TYPE_SELL: TickType
CHANGE_TYPE_UNSPECIFIED: ChangeType
CHANGE_TYPE_LIMITUP: ChangeType
CHANGE_TYPE_UP: ChangeType
CHANGE_TYPE_UNCHANGED: ChangeType
CHANGE_TYPE_DOWN: ChangeType
CHANGE_TYPE_LIMITDOWN: ChangeType
UNIT_UNSPECIFIED: Unit
UNIT_COMMON: Unit
UNIT_SHARE: Unit
TRADE_TYPE_UNSPECIFIED: TradeType
TRADE_TYPE_COMMON: TradeType
TRADE_TYPE_DAYTRADE: TradeType
SCANNER_TYPE_UNSPECIFIED: ScannerType
SCANNER_TYPE_CHANGEPERCENTRANK: ScannerType
SCANNER_TYPE_CHANGEPRICERANK: ScannerType
SCANNER_TYPE_DAYRANGERANK: ScannerType
SCANNER_TYPE_VOLUMERANK: ScannerType
SCANNER_TYPE_AMOUNTRANK: ScannerType
SCANNER_TYPE_TICKCOUNTRANK: ScannerType
TICKS_QUERY_TYPE_UNSPECIFIED: TicksQueryType
TICKS_QUERY_TYPE_ALLDAY: TicksQueryType
TICKS_QUERY_TYPE_RANGETIME: TicksQueryType
TICKS_QUERY_TYPE_LASTCOUNT: TicksQueryType
FETCH_STATUS_UNSPECIFIED: FetchStatus
FETCH_STATUS_SUCCESS: FetchStatus
FETCH_STATUS_FAIL: FetchStatus

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
    __slots__ = ("account_type", "person_id", "broker_id", "account_id", "username", "signed")
    ACCOUNT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERSON_ID_FIELD_NUMBER: _ClassVar[int]
    BROKER_ID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    SIGNED_FIELD_NUMBER: _ClassVar[int]
    account_type: str
    person_id: str
    broker_id: str
    account_id: str
    username: str
    signed: bool
    def __init__(self, account_type: _Optional[str] = ..., person_id: _Optional[str] = ..., broker_id: _Optional[str] = ..., account_id: _Optional[str] = ..., username: _Optional[str] = ..., signed: bool = ...) -> None: ...

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
    __slots__ = ("acc_balance", "date", "errmsg", "status")
    ACC_BALANCE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    acc_balance: float
    date: str
    errmsg: str
    status: FetchStatus
    def __init__(self, acc_balance: _Optional[float] = ..., date: _Optional[str] = ..., errmsg: _Optional[str] = ..., status: _Optional[_Union[FetchStatus, str]] = ...) -> None: ...

class Contract(_message.Message):
    __slots__ = ("security_type", "exchange", "code", "symbol", "name", "currency", "category", "delivery_month", "delivery_date", "strike_price", "option_right", "underlying_kind", "underlying_code", "unit", "multiplier", "limit_up", "limit_down", "reference", "update_date", "margin_trading_balance", "short_selling_balance", "day_trade", "target_code")
    SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_MONTH_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_DATE_FIELD_NUMBER: _ClassVar[int]
    STRIKE_PRICE_FIELD_NUMBER: _ClassVar[int]
    OPTION_RIGHT_FIELD_NUMBER: _ClassVar[int]
    UNDERLYING_KIND_FIELD_NUMBER: _ClassVar[int]
    UNDERLYING_CODE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_UP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_DOWN_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DATE_FIELD_NUMBER: _ClassVar[int]
    MARGIN_TRADING_BALANCE_FIELD_NUMBER: _ClassVar[int]
    SHORT_SELLING_BALANCE_FIELD_NUMBER: _ClassVar[int]
    DAY_TRADE_FIELD_NUMBER: _ClassVar[int]
    TARGET_CODE_FIELD_NUMBER: _ClassVar[int]
    security_type: SecurityType
    exchange: Exchange
    code: str
    symbol: str
    name: str
    currency: Currency
    category: str
    delivery_month: str
    delivery_date: str
    strike_price: float
    option_right: OptionRight
    underlying_kind: str
    underlying_code: str
    unit: float
    multiplier: int
    limit_up: float
    limit_down: float
    reference: float
    update_date: str
    margin_trading_balance: int
    short_selling_balance: int
    day_trade: DayTrade
    target_code: str
    def __init__(self, security_type: _Optional[_Union[SecurityType, str]] = ..., exchange: _Optional[_Union[Exchange, str]] = ..., code: _Optional[str] = ..., symbol: _Optional[str] = ..., name: _Optional[str] = ..., currency: _Optional[_Union[Currency, str]] = ..., category: _Optional[str] = ..., delivery_month: _Optional[str] = ..., delivery_date: _Optional[str] = ..., strike_price: _Optional[float] = ..., option_right: _Optional[_Union[OptionRight, str]] = ..., underlying_kind: _Optional[str] = ..., underlying_code: _Optional[str] = ..., unit: _Optional[float] = ..., multiplier: _Optional[int] = ..., limit_up: _Optional[float] = ..., limit_down: _Optional[float] = ..., reference: _Optional[float] = ..., update_date: _Optional[str] = ..., margin_trading_balance: _Optional[int] = ..., short_selling_balance: _Optional[int] = ..., day_trade: _Optional[_Union[DayTrade, str]] = ..., target_code: _Optional[str] = ...) -> None: ...

class ComboContract(_message.Message):
    __slots__ = ("legs",)
    LEGS_FIELD_NUMBER: _ClassVar[int]
    legs: _containers.RepeatedCompositeFieldContainer[ComboBase]
    def __init__(self, legs: _Optional[_Iterable[_Union[ComboBase, _Mapping]]] = ...) -> None: ...

class ComboBase(_message.Message):
    __slots__ = ("security_type", "exchange", "code", "symbol", "name", "currency", "category", "delivery_month", "delivery_date", "strike_price", "option_right", "underlying_kind", "underlying_code", "unit", "multiplier", "limit_up", "limit_down", "reference", "update_date", "margin_trading_balance", "short_selling_balance", "day_trade", "target_code", "action")
    SECURITY_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    SYMBOL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_MONTH_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_DATE_FIELD_NUMBER: _ClassVar[int]
    STRIKE_PRICE_FIELD_NUMBER: _ClassVar[int]
    OPTION_RIGHT_FIELD_NUMBER: _ClassVar[int]
    UNDERLYING_KIND_FIELD_NUMBER: _ClassVar[int]
    UNDERLYING_CODE_FIELD_NUMBER: _ClassVar[int]
    UNIT_FIELD_NUMBER: _ClassVar[int]
    MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    LIMIT_UP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_DOWN_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_DATE_FIELD_NUMBER: _ClassVar[int]
    MARGIN_TRADING_BALANCE_FIELD_NUMBER: _ClassVar[int]
    SHORT_SELLING_BALANCE_FIELD_NUMBER: _ClassVar[int]
    DAY_TRADE_FIELD_NUMBER: _ClassVar[int]
    TARGET_CODE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    security_type: SecurityType
    exchange: Exchange
    code: str
    symbol: str
    name: str
    currency: Currency
    category: str
    delivery_month: str
    delivery_date: str
    strike_price: float
    option_right: OptionRight
    underlying_kind: str
    underlying_code: str
    unit: float
    multiplier: int
    limit_up: float
    limit_down: float
    reference: float
    update_date: str
    margin_trading_balance: int
    short_selling_balance: int
    day_trade: DayTrade
    target_code: str
    action: Action
    def __init__(self, security_type: _Optional[_Union[SecurityType, str]] = ..., exchange: _Optional[_Union[Exchange, str]] = ..., code: _Optional[str] = ..., symbol: _Optional[str] = ..., name: _Optional[str] = ..., currency: _Optional[_Union[Currency, str]] = ..., category: _Optional[str] = ..., delivery_month: _Optional[str] = ..., delivery_date: _Optional[str] = ..., strike_price: _Optional[float] = ..., option_right: _Optional[_Union[OptionRight, str]] = ..., underlying_kind: _Optional[str] = ..., underlying_code: _Optional[str] = ..., unit: _Optional[float] = ..., multiplier: _Optional[int] = ..., limit_up: _Optional[float] = ..., limit_down: _Optional[float] = ..., reference: _Optional[float] = ..., update_date: _Optional[str] = ..., margin_trading_balance: _Optional[int] = ..., short_selling_balance: _Optional[int] = ..., day_trade: _Optional[_Union[DayTrade, str]] = ..., target_code: _Optional[str] = ..., action: _Optional[_Union[Action, str]] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ("action", "price", "quantity", "id", "seqno", "ordno", "account", "price_type", "order_type", "octype", "order_lot", "order_cond", "daytrade_short", "custom_field", "ca")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    ORDNO_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    OCTYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_LOT_FIELD_NUMBER: _ClassVar[int]
    ORDER_COND_FIELD_NUMBER: _ClassVar[int]
    DAYTRADE_SHORT_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_FIELD_NUMBER: _ClassVar[int]
    CA_FIELD_NUMBER: _ClassVar[int]
    action: Action
    price: float
    quantity: int
    id: str
    seqno: str
    ordno: str
    account: Account
    price_type: str
    order_type: OrderType
    octype: FuturesOCType
    order_lot: StockOrderLot
    order_cond: StockOrderCond
    daytrade_short: bool
    custom_field: str
    ca: str
    def __init__(self, action: _Optional[_Union[Action, str]] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ..., id: _Optional[str] = ..., seqno: _Optional[str] = ..., ordno: _Optional[str] = ..., account: _Optional[_Union[Account, _Mapping]] = ..., price_type: _Optional[str] = ..., order_type: _Optional[_Union[OrderType, str]] = ..., octype: _Optional[_Union[FuturesOCType, str]] = ..., order_lot: _Optional[_Union[StockOrderLot, str]] = ..., order_cond: _Optional[_Union[StockOrderCond, str]] = ..., daytrade_short: bool = ..., custom_field: _Optional[str] = ..., ca: _Optional[str] = ...) -> None: ...

class ComboOrder(_message.Message):
    __slots__ = ("action", "price", "quantity", "id", "seqno", "ordno", "account", "price_type", "order_type", "octype", "custom_field", "ca")
    ACTION_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    ORDNO_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PRICE_TYPE_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    OCTYPE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_FIELD_FIELD_NUMBER: _ClassVar[int]
    CA_FIELD_NUMBER: _ClassVar[int]
    action: Action
    price: float
    quantity: int
    id: str
    seqno: str
    ordno: str
    account: Account
    price_type: str
    order_type: OrderType
    octype: FuturesOCType
    custom_field: str
    ca: str
    def __init__(self, action: _Optional[_Union[Action, str]] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ..., id: _Optional[str] = ..., seqno: _Optional[str] = ..., ordno: _Optional[str] = ..., account: _Optional[_Union[Account, _Mapping]] = ..., price_type: _Optional[str] = ..., order_type: _Optional[_Union[OrderType, str]] = ..., octype: _Optional[_Union[FuturesOCType, str]] = ..., custom_field: _Optional[str] = ..., ca: _Optional[str] = ...) -> None: ...

class OrderStatus(_message.Message):
    __slots__ = ("id", "status", "status_code", "order_datetime", "deal_quantity", "cancel_quantity", "web_id", "msg", "modified_time", "modified_price", "order_quantity", "deals")
    ID_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    STATUS_CODE_FIELD_NUMBER: _ClassVar[int]
    ORDER_DATETIME_FIELD_NUMBER: _ClassVar[int]
    DEAL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    CANCEL_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    WEB_ID_FIELD_NUMBER: _ClassVar[int]
    MSG_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_TIME_FIELD_NUMBER: _ClassVar[int]
    MODIFIED_PRICE_FIELD_NUMBER: _ClassVar[int]
    ORDER_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DEALS_FIELD_NUMBER: _ClassVar[int]
    id: str
    status: Status
    status_code: str
    order_datetime: str
    deal_quantity: int
    cancel_quantity: int
    web_id: str
    msg: str
    modified_time: str
    modified_price: float
    order_quantity: int
    deals: _containers.RepeatedCompositeFieldContainer[Deal]
    def __init__(self, id: _Optional[str] = ..., status: _Optional[_Union[Status, str]] = ..., status_code: _Optional[str] = ..., order_datetime: _Optional[str] = ..., deal_quantity: _Optional[int] = ..., cancel_quantity: _Optional[int] = ..., web_id: _Optional[str] = ..., msg: _Optional[str] = ..., modified_time: _Optional[str] = ..., modified_price: _Optional[float] = ..., order_quantity: _Optional[int] = ..., deals: _Optional[_Iterable[_Union[Deal, _Mapping]]] = ...) -> None: ...

class Deal(_message.Message):
    __slots__ = ("seq", "price", "quantity", "ts")
    SEQ_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    seq: str
    price: float
    quantity: int
    ts: float
    def __init__(self, seq: _Optional[str] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ..., ts: _Optional[float] = ...) -> None: ...

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
    action: Action
    price: float
    quantity: int
    ts: str
    def __init__(self, code: _Optional[str] = ..., action: _Optional[_Union[Action, str]] = ..., price: _Optional[float] = ..., quantity: _Optional[int] = ..., ts: _Optional[str] = ...) -> None: ...

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
    direction: Action
    quantity: int
    price: float
    last_price: float
    pnl: float
    yd_quantity: int
    cond: StockOrderCond
    margin_purchase_amount: int
    collateral: int
    short_sale_margin: int
    interest: int
    def __init__(self, id: _Optional[int] = ..., code: _Optional[str] = ..., direction: _Optional[_Union[Action, str]] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., last_price: _Optional[float] = ..., pnl: _Optional[float] = ..., yd_quantity: _Optional[int] = ..., cond: _Optional[_Union[StockOrderCond, str]] = ..., margin_purchase_amount: _Optional[int] = ..., collateral: _Optional[int] = ..., short_sale_margin: _Optional[int] = ..., interest: _Optional[int] = ...) -> None: ...

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
    direction: Action
    quantity: int
    price: float
    last_price: float
    pnl: float
    def __init__(self, id: _Optional[int] = ..., code: _Optional[str] = ..., direction: _Optional[_Union[Action, str]] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., last_price: _Optional[float] = ..., pnl: _Optional[float] = ...) -> None: ...

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
    __slots__ = ("date", "code", "quantity", "price", "last_price", "pnl", "dseq", "direction", "currency", "fee", "cond", "ex_dividends", "interest", "margintrading_amt", "collateral")
    DATE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    DSEQ_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    COND_FIELD_NUMBER: _ClassVar[int]
    EX_DIVIDENDS_FIELD_NUMBER: _ClassVar[int]
    INTEREST_FIELD_NUMBER: _ClassVar[int]
    MARGINTRADING_AMT_FIELD_NUMBER: _ClassVar[int]
    COLLATERAL_FIELD_NUMBER: _ClassVar[int]
    date: str
    code: str
    quantity: int
    price: float
    last_price: float
    pnl: float
    dseq: str
    direction: Action
    currency: Currency
    fee: float
    cond: StockOrderCond
    ex_dividends: int
    interest: int
    margintrading_amt: int
    collateral: int
    def __init__(self, date: _Optional[str] = ..., code: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., last_price: _Optional[float] = ..., pnl: _Optional[float] = ..., dseq: _Optional[str] = ..., direction: _Optional[_Union[Action, str]] = ..., currency: _Optional[_Union[Currency, str]] = ..., fee: _Optional[float] = ..., cond: _Optional[_Union[StockOrderCond, str]] = ..., ex_dividends: _Optional[int] = ..., interest: _Optional[int] = ..., margintrading_amt: _Optional[int] = ..., collateral: _Optional[int] = ...) -> None: ...

class FuturePositionDetail(_message.Message):
    __slots__ = ("date", "code", "quantity", "price", "last_price", "pnl", "dseq", "direction", "currency", "fee", "entry_quantity")
    DATE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    DSEQ_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    date: str
    code: str
    quantity: int
    price: float
    last_price: float
    pnl: float
    dseq: str
    direction: Action
    currency: Currency
    fee: float
    entry_quantity: int
    def __init__(self, date: _Optional[str] = ..., code: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., last_price: _Optional[float] = ..., pnl: _Optional[float] = ..., dseq: _Optional[str] = ..., direction: _Optional[_Union[Action, str]] = ..., currency: _Optional[_Union[Currency, str]] = ..., fee: _Optional[float] = ..., entry_quantity: _Optional[int] = ...) -> None: ...

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
    __slots__ = ("dseq", "code", "quantity", "price", "pnl", "pr_ratio", "cond", "date", "seqno", "id")
    DSEQ_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    PR_RATIO_FIELD_NUMBER: _ClassVar[int]
    COND_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    SEQNO_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    dseq: str
    code: str
    quantity: int
    price: float
    pnl: float
    pr_ratio: float
    cond: StockOrderCond
    date: str
    seqno: str
    id: int
    def __init__(self, dseq: _Optional[str] = ..., code: _Optional[str] = ..., quantity: _Optional[int] = ..., price: _Optional[float] = ..., pnl: _Optional[float] = ..., pr_ratio: _Optional[float] = ..., cond: _Optional[_Union[StockOrderCond, str]] = ..., date: _Optional[str] = ..., seqno: _Optional[str] = ..., id: _Optional[int] = ...) -> None: ...

class FutureProfitLoss(_message.Message):
    __slots__ = ("date", "code", "quantity", "entry_price", "cover_price", "direction", "pnl", "tax", "fee", "id")
    DATE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ENTRY_PRICE_FIELD_NUMBER: _ClassVar[int]
    COVER_PRICE_FIELD_NUMBER: _ClassVar[int]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    date: str
    code: str
    quantity: int
    entry_price: float
    cover_price: float
    direction: Action
    pnl: float
    tax: int
    fee: int
    id: int
    def __init__(self, date: _Optional[str] = ..., code: _Optional[str] = ..., quantity: _Optional[int] = ..., entry_price: _Optional[float] = ..., cover_price: _Optional[float] = ..., direction: _Optional[_Union[Action, str]] = ..., pnl: _Optional[float] = ..., tax: _Optional[int] = ..., fee: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

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
    __slots__ = ("price", "cost", "interest", "date", "code", "quantity", "dseq", "fee", "tax", "currency", "rep_margintrading_amt", "rep_collateral", "rep_margin", "shortselling_fee", "ex_dividend_amt", "trade_type", "cond")
    PRICE_FIELD_NUMBER: _ClassVar[int]
    COST_FIELD_NUMBER: _ClassVar[int]
    INTEREST_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DSEQ_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    REP_MARGINTRADING_AMT_FIELD_NUMBER: _ClassVar[int]
    REP_COLLATERAL_FIELD_NUMBER: _ClassVar[int]
    REP_MARGIN_FIELD_NUMBER: _ClassVar[int]
    SHORTSELLING_FEE_FIELD_NUMBER: _ClassVar[int]
    EX_DIVIDEND_AMT_FIELD_NUMBER: _ClassVar[int]
    TRADE_TYPE_FIELD_NUMBER: _ClassVar[int]
    COND_FIELD_NUMBER: _ClassVar[int]
    price: float
    cost: int
    interest: int
    date: str
    code: str
    quantity: int
    dseq: str
    fee: int
    tax: int
    currency: Currency
    rep_margintrading_amt: int
    rep_collateral: int
    rep_margin: int
    shortselling_fee: int
    ex_dividend_amt: int
    trade_type: TradeType
    cond: StockOrderCond
    def __init__(self, price: _Optional[float] = ..., cost: _Optional[int] = ..., interest: _Optional[int] = ..., date: _Optional[str] = ..., code: _Optional[str] = ..., quantity: _Optional[int] = ..., dseq: _Optional[str] = ..., fee: _Optional[int] = ..., tax: _Optional[int] = ..., currency: _Optional[_Union[Currency, str]] = ..., rep_margintrading_amt: _Optional[int] = ..., rep_collateral: _Optional[int] = ..., rep_margin: _Optional[int] = ..., shortselling_fee: _Optional[int] = ..., ex_dividend_amt: _Optional[int] = ..., trade_type: _Optional[_Union[TradeType, str]] = ..., cond: _Optional[_Union[StockOrderCond, str]] = ...) -> None: ...

class FutureProfitDetail(_message.Message):
    __slots__ = ("direction", "entry_date", "entry_price", "cover_price", "pnl", "date", "code", "quantity", "dseq", "fee", "tax", "currency")
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ENTRY_DATE_FIELD_NUMBER: _ClassVar[int]
    ENTRY_PRICE_FIELD_NUMBER: _ClassVar[int]
    COVER_PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    DSEQ_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    direction: Action
    entry_date: str
    entry_price: float
    cover_price: float
    pnl: int
    date: str
    code: str
    quantity: int
    dseq: str
    fee: int
    tax: int
    currency: Currency
    def __init__(self, direction: _Optional[_Union[Action, str]] = ..., entry_date: _Optional[str] = ..., entry_price: _Optional[float] = ..., cover_price: _Optional[float] = ..., pnl: _Optional[int] = ..., date: _Optional[str] = ..., code: _Optional[str] = ..., quantity: _Optional[int] = ..., dseq: _Optional[str] = ..., fee: _Optional[int] = ..., tax: _Optional[int] = ..., currency: _Optional[_Union[Currency, str]] = ...) -> None: ...

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
    __slots__ = ("entry_cost", "cover_cost", "code", "quantity", "entry_price", "cover_price", "pnl", "currency", "buy_cost", "sell_cost", "pr_ratio", "cond")
    ENTRY_COST_FIELD_NUMBER: _ClassVar[int]
    COVER_COST_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ENTRY_PRICE_FIELD_NUMBER: _ClassVar[int]
    COVER_PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    BUY_COST_FIELD_NUMBER: _ClassVar[int]
    SELL_COST_FIELD_NUMBER: _ClassVar[int]
    PR_RATIO_FIELD_NUMBER: _ClassVar[int]
    COND_FIELD_NUMBER: _ClassVar[int]
    entry_cost: int
    cover_cost: int
    code: str
    quantity: int
    entry_price: float
    cover_price: float
    pnl: float
    currency: Currency
    buy_cost: int
    sell_cost: int
    pr_ratio: float
    cond: StockOrderCond
    def __init__(self, entry_cost: _Optional[int] = ..., cover_cost: _Optional[int] = ..., code: _Optional[str] = ..., quantity: _Optional[int] = ..., entry_price: _Optional[float] = ..., cover_price: _Optional[float] = ..., pnl: _Optional[float] = ..., currency: _Optional[_Union[Currency, str]] = ..., buy_cost: _Optional[int] = ..., sell_cost: _Optional[int] = ..., pr_ratio: _Optional[float] = ..., cond: _Optional[_Union[StockOrderCond, str]] = ...) -> None: ...

class FutureProfitLossSummary(_message.Message):
    __slots__ = ("direction", "tax", "fee", "code", "quantity", "entry_price", "cover_price", "pnl", "currency")
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    ENTRY_PRICE_FIELD_NUMBER: _ClassVar[int]
    COVER_PRICE_FIELD_NUMBER: _ClassVar[int]
    PNL_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    direction: Action
    tax: int
    fee: int
    code: str
    quantity: int
    entry_price: float
    cover_price: float
    pnl: float
    currency: Currency
    def __init__(self, direction: _Optional[_Union[Action, str]] = ..., tax: _Optional[int] = ..., fee: _Optional[int] = ..., code: _Optional[str] = ..., quantity: _Optional[int] = ..., entry_price: _Optional[float] = ..., cover_price: _Optional[float] = ..., pnl: _Optional[float] = ..., currency: _Optional[_Union[Currency, str]] = ...) -> None: ...

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
    __slots__ = ("date", "amount", "t_money", "t_day", "t1_money", "t1_day", "t2_money", "t2_day", "status")
    DATE_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    T_MONEY_FIELD_NUMBER: _ClassVar[int]
    T_DAY_FIELD_NUMBER: _ClassVar[int]
    T1_MONEY_FIELD_NUMBER: _ClassVar[int]
    T1_DAY_FIELD_NUMBER: _ClassVar[int]
    T2_MONEY_FIELD_NUMBER: _ClassVar[int]
    T2_DAY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    date: str
    amount: float
    t_money: float
    t_day: str
    t1_money: float
    t1_day: str
    t2_money: float
    t2_day: str
    status: FetchStatus
    def __init__(self, date: _Optional[str] = ..., amount: _Optional[float] = ..., t_money: _Optional[float] = ..., t_day: _Optional[str] = ..., t1_money: _Optional[float] = ..., t1_day: _Optional[str] = ..., t2_money: _Optional[float] = ..., t2_day: _Optional[str] = ..., status: _Optional[_Union[FetchStatus, str]] = ...) -> None: ...

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
    __slots__ = ("equity", "available_margin", "initial_margin", "maintenance_margin", "yesterday_balance", "today_balance", "deposit_withdrawal", "fee", "tax", "margin_call", "risk_indicator", "royalty_revenue_expenditure", "equity_amount", "option_openbuy_market_value", "option_opensell_market_value", "option_open_position", "option_settle_profitloss", "future_open_position", "today_future_open_position", "future_settle_profitloss", "plus_margin", "plus_margin_indicator", "security_collateral_amount", "order_margin_premium", "collateral_amount", "status")
    EQUITY_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_MARGIN_FIELD_NUMBER: _ClassVar[int]
    INITIAL_MARGIN_FIELD_NUMBER: _ClassVar[int]
    MAINTENANCE_MARGIN_FIELD_NUMBER: _ClassVar[int]
    YESTERDAY_BALANCE_FIELD_NUMBER: _ClassVar[int]
    TODAY_BALANCE_FIELD_NUMBER: _ClassVar[int]
    DEPOSIT_WITHDRAWAL_FIELD_NUMBER: _ClassVar[int]
    FEE_FIELD_NUMBER: _ClassVar[int]
    TAX_FIELD_NUMBER: _ClassVar[int]
    MARGIN_CALL_FIELD_NUMBER: _ClassVar[int]
    RISK_INDICATOR_FIELD_NUMBER: _ClassVar[int]
    ROYALTY_REVENUE_EXPENDITURE_FIELD_NUMBER: _ClassVar[int]
    EQUITY_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    OPTION_OPENBUY_MARKET_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTION_OPENSELL_MARKET_VALUE_FIELD_NUMBER: _ClassVar[int]
    OPTION_OPEN_POSITION_FIELD_NUMBER: _ClassVar[int]
    OPTION_SETTLE_PROFITLOSS_FIELD_NUMBER: _ClassVar[int]
    FUTURE_OPEN_POSITION_FIELD_NUMBER: _ClassVar[int]
    TODAY_FUTURE_OPEN_POSITION_FIELD_NUMBER: _ClassVar[int]
    FUTURE_SETTLE_PROFITLOSS_FIELD_NUMBER: _ClassVar[int]
    PLUS_MARGIN_FIELD_NUMBER: _ClassVar[int]
    PLUS_MARGIN_INDICATOR_FIELD_NUMBER: _ClassVar[int]
    SECURITY_COLLATERAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ORDER_MARGIN_PREMIUM_FIELD_NUMBER: _ClassVar[int]
    COLLATERAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    equity: float
    available_margin: float
    initial_margin: float
    maintenance_margin: float
    yesterday_balance: float
    today_balance: float
    deposit_withdrawal: float
    fee: float
    tax: float
    margin_call: float
    risk_indicator: float
    royalty_revenue_expenditure: float
    equity_amount: float
    option_openbuy_market_value: float
    option_opensell_market_value: float
    option_open_position: float
    option_settle_profitloss: float
    future_open_position: float
    today_future_open_position: float
    future_settle_profitloss: float
    plus_margin: float
    plus_margin_indicator: float
    security_collateral_amount: float
    order_margin_premium: float
    collateral_amount: float
    status: FetchStatus
    def __init__(self, equity: _Optional[float] = ..., available_margin: _Optional[float] = ..., initial_margin: _Optional[float] = ..., maintenance_margin: _Optional[float] = ..., yesterday_balance: _Optional[float] = ..., today_balance: _Optional[float] = ..., deposit_withdrawal: _Optional[float] = ..., fee: _Optional[float] = ..., tax: _Optional[float] = ..., margin_call: _Optional[float] = ..., risk_indicator: _Optional[float] = ..., royalty_revenue_expenditure: _Optional[float] = ..., equity_amount: _Optional[float] = ..., option_openbuy_market_value: _Optional[float] = ..., option_opensell_market_value: _Optional[float] = ..., option_open_position: _Optional[float] = ..., option_settle_profitloss: _Optional[float] = ..., future_open_position: _Optional[float] = ..., today_future_open_position: _Optional[float] = ..., future_settle_profitloss: _Optional[float] = ..., plus_margin: _Optional[float] = ..., plus_margin_indicator: _Optional[float] = ..., security_collateral_amount: _Optional[float] = ..., order_margin_premium: _Optional[float] = ..., collateral_amount: _Optional[float] = ..., status: _Optional[_Union[FetchStatus, str]] = ...) -> None: ...

class GetTradingLimitsRequest(_message.Message):
    __slots__ = ("account",)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: Account
    def __init__(self, account: _Optional[_Union[Account, _Mapping]] = ...) -> None: ...

class TradingLimits(_message.Message):
    __slots__ = ("trading_limit", "trading_used", "trading_available", "margin_limit", "margin_used", "margin_available", "short_limit", "short_used", "short_available", "status")
    TRADING_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TRADING_USED_FIELD_NUMBER: _ClassVar[int]
    TRADING_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    MARGIN_LIMIT_FIELD_NUMBER: _ClassVar[int]
    MARGIN_USED_FIELD_NUMBER: _ClassVar[int]
    MARGIN_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    SHORT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    SHORT_USED_FIELD_NUMBER: _ClassVar[int]
    SHORT_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    trading_limit: int
    trading_used: int
    trading_available: int
    margin_limit: int
    margin_used: int
    margin_available: int
    short_limit: int
    short_used: int
    short_available: int
    status: FetchStatus
    def __init__(self, trading_limit: _Optional[int] = ..., trading_used: _Optional[int] = ..., trading_available: _Optional[int] = ..., margin_limit: _Optional[int] = ..., margin_used: _Optional[int] = ..., margin_available: _Optional[int] = ..., short_limit: _Optional[int] = ..., short_used: _Optional[int] = ..., short_available: _Optional[int] = ..., status: _Optional[_Union[FetchStatus, str]] = ...) -> None: ...

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
    __slots__ = ("ts", "code", "exchange", "open", "high", "low", "close", "change_price", "change_rate", "average_price", "volume", "total_volume", "amount", "total_amount", "buy_price", "buy_volume", "sell_price", "sell_volume", "tick_type", "change_type", "yesterday_volume", "volume_ratio")
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
    TICK_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    YESTERDAY_VOLUME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_RATIO_FIELD_NUMBER: _ClassVar[int]
    ts: int
    code: str
    exchange: Exchange
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
    buy_volume: float
    sell_price: float
    sell_volume: int
    tick_type: TickType
    change_type: ChangeType
    yesterday_volume: float
    volume_ratio: float
    def __init__(self, ts: _Optional[int] = ..., code: _Optional[str] = ..., exchange: _Optional[_Union[Exchange, str]] = ..., open: _Optional[float] = ..., high: _Optional[float] = ..., low: _Optional[float] = ..., close: _Optional[float] = ..., change_price: _Optional[float] = ..., change_rate: _Optional[float] = ..., average_price: _Optional[float] = ..., volume: _Optional[int] = ..., total_volume: _Optional[int] = ..., amount: _Optional[int] = ..., total_amount: _Optional[int] = ..., buy_price: _Optional[float] = ..., buy_volume: _Optional[float] = ..., sell_price: _Optional[float] = ..., sell_volume: _Optional[int] = ..., tick_type: _Optional[_Union[TickType, str]] = ..., change_type: _Optional[_Union[ChangeType, str]] = ..., yesterday_volume: _Optional[float] = ..., volume_ratio: _Optional[float] = ...) -> None: ...

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
    __slots__ = ("code", "open", "high", "low", "close", "volume", "date", "transaction", "amount")
    CODE_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    code: _containers.RepeatedScalarFieldContainer[str]
    open: _containers.RepeatedScalarFieldContainer[float]
    high: _containers.RepeatedScalarFieldContainer[float]
    low: _containers.RepeatedScalarFieldContainer[float]
    close: _containers.RepeatedScalarFieldContainer[float]
    volume: _containers.RepeatedScalarFieldContainer[int]
    date: _containers.RepeatedScalarFieldContainer[str]
    transaction: _containers.RepeatedScalarFieldContainer[int]
    amount: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, code: _Optional[_Iterable[str]] = ..., open: _Optional[_Iterable[float]] = ..., high: _Optional[_Iterable[float]] = ..., low: _Optional[_Iterable[float]] = ..., close: _Optional[_Iterable[float]] = ..., volume: _Optional[_Iterable[int]] = ..., date: _Optional[_Iterable[str]] = ..., transaction: _Optional[_Iterable[int]] = ..., amount: _Optional[_Iterable[int]] = ...) -> None: ...

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
    __slots__ = ("stock_id", "margin_unit", "short_unit", "update_time", "system")
    STOCK_ID_FIELD_NUMBER: _ClassVar[int]
    MARGIN_UNIT_FIELD_NUMBER: _ClassVar[int]
    SHORT_UNIT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_FIELD_NUMBER: _ClassVar[int]
    stock_id: str
    margin_unit: int
    short_unit: int
    update_time: str
    system: str
    def __init__(self, stock_id: _Optional[str] = ..., margin_unit: _Optional[int] = ..., short_unit: _Optional[int] = ..., update_time: _Optional[str] = ..., system: _Optional[str] = ...) -> None: ...

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
    scanner_type: ScannerType
    ascending: bool
    date: str
    count: int
    def __init__(self, scanner_type: _Optional[_Union[ScannerType, str]] = ..., ascending: bool = ..., date: _Optional[str] = ..., count: _Optional[int] = ...) -> None: ...

class GetScannersResponse(_message.Message):
    __slots__ = ("scanners",)
    SCANNERS_FIELD_NUMBER: _ClassVar[int]
    scanners: _containers.RepeatedCompositeFieldContainer[ScannerItem]
    def __init__(self, scanners: _Optional[_Iterable[_Union[ScannerItem, _Mapping]]] = ...) -> None: ...

class ScannerItem(_message.Message):
    __slots__ = ("date", "code", "name", "ts", "open", "high", "low", "close", "price_range", "tick_type", "change_price", "change_type", "average_price", "volume", "total_volume", "amount", "total_amount", "yesterday_volume", "volume_ratio", "buy_price", "buy_volume", "sell_price", "sell_volume", "bid_orders", "bid_volumes", "ask_orders", "ask_volumes", "rank_value")
    DATE_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TS_FIELD_NUMBER: _ClassVar[int]
    OPEN_FIELD_NUMBER: _ClassVar[int]
    HIGH_FIELD_NUMBER: _ClassVar[int]
    LOW_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    PRICE_RANGE_FIELD_NUMBER: _ClassVar[int]
    TICK_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_PRICE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    AVERAGE_PRICE_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    TOTAL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    YESTERDAY_VOLUME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_RATIO_FIELD_NUMBER: _ClassVar[int]
    BUY_PRICE_FIELD_NUMBER: _ClassVar[int]
    BUY_VOLUME_FIELD_NUMBER: _ClassVar[int]
    SELL_PRICE_FIELD_NUMBER: _ClassVar[int]
    SELL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    BID_ORDERS_FIELD_NUMBER: _ClassVar[int]
    BID_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    ASK_ORDERS_FIELD_NUMBER: _ClassVar[int]
    ASK_VOLUMES_FIELD_NUMBER: _ClassVar[int]
    RANK_VALUE_FIELD_NUMBER: _ClassVar[int]
    date: str
    code: str
    name: str
    ts: int
    open: float
    high: float
    low: float
    close: float
    price_range: float
    tick_type: TickType
    change_price: float
    change_type: ChangeType
    average_price: float
    volume: int
    total_volume: int
    amount: int
    total_amount: int
    yesterday_volume: int
    volume_ratio: float
    buy_price: float
    buy_volume: int
    sell_price: float
    sell_volume: int
    bid_orders: int
    bid_volumes: int
    ask_orders: int
    ask_volumes: int
    rank_value: float
    def __init__(self, date: _Optional[str] = ..., code: _Optional[str] = ..., name: _Optional[str] = ..., ts: _Optional[int] = ..., open: _Optional[float] = ..., high: _Optional[float] = ..., low: _Optional[float] = ..., close: _Optional[float] = ..., price_range: _Optional[float] = ..., tick_type: _Optional[_Union[TickType, str]] = ..., change_price: _Optional[float] = ..., change_type: _Optional[_Union[ChangeType, str]] = ..., average_price: _Optional[float] = ..., volume: _Optional[int] = ..., total_volume: _Optional[int] = ..., amount: _Optional[int] = ..., total_amount: _Optional[int] = ..., yesterday_volume: _Optional[int] = ..., volume_ratio: _Optional[float] = ..., buy_price: _Optional[float] = ..., buy_volume: _Optional[int] = ..., sell_price: _Optional[float] = ..., sell_volume: _Optional[int] = ..., bid_orders: _Optional[int] = ..., bid_volumes: _Optional[int] = ..., ask_orders: _Optional[int] = ..., ask_volumes: _Optional[int] = ..., rank_value: _Optional[float] = ...) -> None: ...

class Punish(_message.Message):
    __slots__ = ("code", "start_date", "end_date", "interval", "updated_at", "unit_limit", "total_limit", "description", "announced_date")
    CODE_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    INTERVAL_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    UNIT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_LIMIT_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCED_DATE_FIELD_NUMBER: _ClassVar[int]
    code: _containers.RepeatedScalarFieldContainer[str]
    start_date: _containers.RepeatedScalarFieldContainer[str]
    end_date: _containers.RepeatedScalarFieldContainer[str]
    interval: _containers.RepeatedScalarFieldContainer[str]
    updated_at: _containers.RepeatedScalarFieldContainer[str]
    unit_limit: _containers.RepeatedScalarFieldContainer[float]
    total_limit: _containers.RepeatedScalarFieldContainer[float]
    description: _containers.RepeatedScalarFieldContainer[str]
    announced_date: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, code: _Optional[_Iterable[str]] = ..., start_date: _Optional[_Iterable[str]] = ..., end_date: _Optional[_Iterable[str]] = ..., interval: _Optional[_Iterable[str]] = ..., updated_at: _Optional[_Iterable[str]] = ..., unit_limit: _Optional[_Iterable[float]] = ..., total_limit: _Optional[_Iterable[float]] = ..., description: _Optional[_Iterable[str]] = ..., announced_date: _Optional[_Iterable[str]] = ...) -> None: ...

class Notice(_message.Message):
    __slots__ = ("code", "reason", "updated_at", "close", "announced_date")
    CODE_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    UPDATED_AT_FIELD_NUMBER: _ClassVar[int]
    CLOSE_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCED_DATE_FIELD_NUMBER: _ClassVar[int]
    code: _containers.RepeatedScalarFieldContainer[str]
    reason: _containers.RepeatedScalarFieldContainer[str]
    updated_at: _containers.RepeatedScalarFieldContainer[str]
    close: _containers.RepeatedScalarFieldContainer[float]
    announced_date: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, code: _Optional[_Iterable[str]] = ..., reason: _Optional[_Iterable[str]] = ..., updated_at: _Optional[_Iterable[str]] = ..., close: _Optional[_Iterable[float]] = ..., announced_date: _Optional[_Iterable[str]] = ...) -> None: ...

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
