"""
provider.src.shioaji_client -.
"""

import logging
import threading
from typing import Any, Callable, List, Optional, TypeAlias

import shioaji as sj
import shioaji.constant as sc
from shioaji.account import Account
from shioaji.data import Kbars, Snapshot, Ticks
from shioaji.order import Order, Trade
from shioaji.position import FuturePosition, StockPosition

ContractData: TypeAlias = Any
AccountData: TypeAlias = Any | Account
OrderData: TypeAlias = Order
TradeData: TypeAlias = Trade
PositionData: TypeAlias = StockPosition | FuturePosition
SnapshotData: TypeAlias = Snapshot
TickData: TypeAlias = Ticks
KBarData: TypeAlias = Kbars


class ShioajiClient:
    """
    ShioajiClient -.
    """

    def __init__(self, simulation: bool = False):
        self.api = sj.Shioaji(simulation=simulation)
        self.on_event(self.event_logger_cb)
        self.__login_status_lock = threading.Lock()
        self.__login_progess = int()

    @property
    def contracts(self) -> Any:
        """
        Access contract data (Stocks, Futures, Options, Indexs).
        """
        return self.api.Contracts

    @property
    def stock_account(self) -> Optional[AccountData]:
        """
        Get default stock account.
        """
        account = self.api.stock_account
        if account is None:
            raise ValueError(
                "Stock account not found. Please ensure you are logged in and have a stock account."
            )
        return account

    @property
    def futopt_account(self) -> Optional[AccountData]:
        """
        Get default futures/options account.
        """
        account = self.api.futopt_account
        if account is None:
            raise ValueError(
                "Futures/Options account not found. Please ensure you are logged in and have a futures/options account."
            )
        return account

    def event_logger_cb(self, resp_code: int, event_code: int, info: str, event: str):
        if event_code != 0:
            logging.warning("resp_code: %d", resp_code)
            logging.warning("event_code: %d", event_code)
            logging.warning("info: %s", info)
            logging.warning("event: %s", event)

    def login_cb(self, security_type: sc.SecurityType):
        with self.__login_status_lock:
            if security_type.value in [item.value for item in sc.SecurityType]:
                self.__login_progess += 1
                logging.info(
                    "login progress: %d/4, %s", self.__login_progess, security_type
                )

    def login(
        self,
        api_key: Optional[str] = None,
        secret_key: Optional[str] = None,
        contracts_timeout: int = 120000,
        fetch_contract: bool = True,
        subscribe_trade: bool = True,
        receive_window: int = 30000,
    ) -> List[AccountData]:
        """
        Login to Shioaji API.
        Support both person_id/passwd (v<1.0) and api_key/secret_key (v>=1.0).

        Returns:
            List[Account]: A list of available trading accounts.
        """
        result: List[AccountData] = []
        if api_key is None or secret_key is None:
            raise ValueError(
                "Either (api_key and secret_key) or (person_id and passwd) must be provided."
            )
        result = self.api.login(
            api_key=api_key,
            secret_key=secret_key,
            contracts_cb=self.login_cb,
            contracts_timeout=contracts_timeout,
            fetch_contract=fetch_contract,
            subscribe_trade=subscribe_trade,
            receive_window=receive_window,
        )
        while True:
            with self.__login_status_lock:
                if self.__login_progess == 4:
                    break
        return result

    def logout(self) -> None:
        """
        Closes the connection between the client and server.
        """
        return self.api.logout()

    def usage(self) -> Any:
        """
        Retrieves usage information.
        """
        return self.api.usage()

    def subscribe_trade(self, account: AccountData) -> None:
        """
        Subscribe to trade reports for the account.
        """
        return self.api.subscribe_trade(account)

    def unsubscribe_trade(self, account: AccountData) -> None:
        """
        Unsubscribe from trade reports for the account.
        """
        return self.api.unsubscribe_trade(account)

    def fetch_contracts(self, contract_download: bool = True) -> None:
        """
        Manually downloads contract files.
        """
        return self.api.fetch_contracts(contract_download=contract_download)

    def list_accounts(self) -> List[AccountData]:
        """
        Retrieves a list of all available trading accounts.
        """
        return self.api.list_accounts()

    def set_default_account(self, account: AccountData) -> None:
        """
        Sets a specific account as the default.
        """
        return self.api.set_default_account(account)

    def place_order(
        self,
        contract: ContractData,
        order: OrderData,
        timeout: int = 5000,
        cb: Optional[Callable] = None,
    ) -> TradeData:
        """
        Place a trading order.

        Args:
            contract: The contract to trade.
            order: The order details.
            timeout: Timeout in milliseconds.
            cb: Callback function.

        Returns:
            Trade: The resulting trade object.
        """
        return self.api.place_order(contract, order, timeout=timeout, cb=cb)

    def place_comboorder(
        self,
        combo_contract: ContractData,
        order: OrderData,
        timeout: int = 5000,
        cb: Optional[Callable] = None,
    ) -> TradeData:
        """
        Places a combination order.
        """
        return self.api.place_comboorder(combo_contract, order, timeout=timeout, cb=cb)

    def update_status(
        self,
        account: Optional[AccountData] = None,
        trade: Optional[TradeData] = None,
        timeout: int = 5000,
        cb: Optional[Callable] = None,
    ) -> None:
        """
        Update the status of orders.
        """
        return self.api.update_status(
            account=account, trade=trade, timeout=timeout, cb=cb
        )

    def list_trades(self) -> List[TradeData]:
        """
        List executed trades.
        """
        return self.api.list_trades()

    def cancel_order(
        self,
        trade: TradeData,
        timeout: int = 5000,
        cb: Optional[Callable] = None,
        **kwargs: Any,
    ) -> TradeData:
        """
        Cancel an existing order.
        """
        return self.api.cancel_order(trade, timeout=timeout, cb=cb, **kwargs)

    def cancel_comboorder(self, trade: TradeData) -> TradeData:
        """
        Cancels a combination order.
        """
        return self.api.cancel_comboorder(trade)

    def update_order(
        self,
        trade: TradeData,
        price: Optional[float] = None,
        quantity: Optional[int] = None,
        timeout: int = 5000,
        cb: Optional[Callable] = None,
        **kwargs: Any,
    ) -> TradeData:
        """
        Update an existing order.
        """
        return self.api.update_order(
            trade=trade,
            price=price,
            qty=quantity,
            timeout=timeout,
            cb=cb,
            **kwargs,
        )

    def account_balance(
        self, timeout: int = 5000, cb: Optional[Callable] = None
    ) -> Any:
        """
        Query account balance.
        """
        return self.api.account_balance(timeout=timeout, cb=cb)

    def ticks(
        self,
        contract: ContractData,
        date: Optional[str] = None,
        query_type: Optional[Any] = None,
        time_start: Optional[str] = None,
        time_end: Optional[str] = None,
        last_cnt: int = 0,
        timeout: int = 30000,
        cb: Optional[Callable] = None,
    ) -> TickData:
        """
        Retrieve tick data.
        """
        return self.api.ticks(
            contract,
            date=date,
            query_type=query_type,
            time_start=time_start,
            time_end=time_end,
            last_cnt=last_cnt,
            timeout=timeout,
            cb=cb,
        )

    def kbars(
        self,
        contract: ContractData,
        start: Optional[str] = None,
        end: Optional[str] = None,
        timeout: int = 30000,
        cb: Optional[Callable] = None,
    ) -> KBarData:
        """
        Retrieve kbar (candlestick) data.
        """
        return self.api.kbars(contract, start=start, end=end, timeout=timeout, cb=cb)

    def snapshots(
        self,
        contracts: List[ContractData],
        timeout: int = 30000,
        cb: Optional[Callable] = None,
    ) -> List[SnapshotData]:
        """
        Get market snapshots.
        """
        return self.api.snapshots(contracts, timeout=timeout, cb=cb)

    def subscribe_quote(
        self,
        contract: ContractData,
        quote_type: Optional[Any] = None,
        version: Optional[Any] = None,
        intraday_odd: bool = False,
    ) -> None:
        """
        Subscribe to real-time quotes.
        """
        return self.api.quote.subscribe(
            contract, quote_type=quote_type, version=version, intraday_odd=intraday_odd
        )

    def unsubscribe_quote(
        self,
        contract: ContractData,
        quote_type: Optional[Any] = None,
        version: Optional[Any] = None,
        intraday_odd: bool = False,
    ) -> None:
        """
        Unsubscribe from real-time quotes.
        """
        return self.api.quote.unsubscribe(
            contract, quote_type=quote_type, version=version, intraday_odd=intraday_odd
        )

    def settlements(
        self,
        account: Optional[AccountData] = None,
        timeout: int = 5000,
        cb: Optional[Callable] = None,
    ) -> List[Any]:
        """
        Query stock account settlements.
        """
        return self.api.settlements(account=account, timeout=timeout, cb=cb)

    def list_positions(
        self,
        account: Optional[AccountData] = None,
        unit: sc.Unit = sc.Unit.Common,
        timeout: int = 5000,
        cb: Optional[Callable] = None,
    ) -> List[PositionData]:
        """
        Queries unrealized gain or loss (positions).
        """
        return self.api.list_positions(
            account=account, unit=unit, timeout=timeout, cb=cb
        )

    def list_position_detail(
        self,
        account: Optional[AccountData] = None,
        detail_id: Optional[str] = None,
        timeout: int = 5000,
        cb: Optional[Callable] = None,
    ) -> List[Any]:
        """
        Queries detailed unrealized gain or loss for a specific position.
        """
        return self.api.list_position_detail(
            account=account, detail_id=detail_id, timeout=timeout, cb=cb
        )

    def list_profit_loss(
        self,
        account: Optional[AccountData] = None,
        begin_date: str = "",
        end_date: str = "",
        unit: sc.Unit = sc.Unit.Common,
        timeout: int = 5000,
        cb: Optional[Callable] = None,
    ) -> List[Any]:
        """
        Query realized profit and loss.
        """
        return self.api.list_profit_loss(
            account=account,
            begin_date=begin_date,
            end_date=end_date,
            unit=unit,
            timeout=timeout,
            cb=cb,
        )

    def list_profit_loss_detail(
        self,
        account: Optional[AccountData] = None,
        detail_id: Optional[str] = None,
        unit: sc.Unit = sc.Unit.Common,
        timeout: int = 5000,
        cb: Optional[Callable] = None,
    ) -> List[Any]:
        """
        Queries detailed realized profit and loss for a specific entry.
        """
        return self.api.list_profit_loss_detail(
            account=account, detail_id=detail_id, unit=unit, timeout=timeout, cb=cb
        )

    def list_profit_loss_summary(
        self,
        account: Optional[AccountData] = None,
        begin_date: str = "",
        end_date: str = "",
        timeout: int = 5000,
        cb: Optional[Callable] = None,
    ) -> List[Any]:
        """
        Queries a summary of profit and loss for a period.
        """
        return self.api.list_profit_loss_summary(
            account=account,
            begin_date=begin_date,
            end_date=end_date,
            timeout=timeout,
            cb=cb,
        )

    def credit_enquires(
        self,
        contracts: List[ContractData],
        timeout: int = 5000,
        cb: Optional[Callable] = None,
    ) -> Any:
        """
        Retrieve credit enquiries for stock contracts.
        """
        return self.api.credit_enquires(contracts, timeout=timeout, cb=cb)

    def short_stock_sources(
        self,
        contracts: List[ContractData],
        timeout: int = 5000,
        cb: Optional[Callable] = None,
    ) -> Any:
        """
        Get short stock sources.
        """
        return self.api.short_stock_sources(contracts, timeout=timeout, cb=cb)

    def scanners(
        self,
        scanner_type: Any,
        count: int = 100,
        date: Optional[str] = None,
        ascending: bool = True,
        timeout: int = 30000,
        cb: Optional[Callable] = None,
    ) -> Any:
        """
        Retrieve ranked stock data (scanners).
        """
        return self.api.scanners(
            scanner_type=scanner_type,
            count=count,
            date=date,
            ascending=ascending,
            timeout=timeout,
            cb=cb,
        )

    def punish(self, timeout: int = 5000, cb: Optional[Callable] = None) -> Any:
        """
        Retrieves information on disposition stocks.
        """
        return self.api.punish(timeout=timeout, cb=cb)

    def notice(self, timeout: int = 5000, cb: Optional[Callable] = None) -> Any:
        """
        Retrieves information on attention stocks.
        """
        return self.api.notice(timeout=timeout, cb=cb)

    def update_combostatus(
        self, timeout: int = 5000, cb: Optional[Callable] = None
    ) -> None:
        """
        Update the status of combo orders.
        """
        return self.api.update_combostatus(timeout=timeout, cb=cb)

    def list_combotrades(self) -> List[TradeData]:
        """
        List executed combo trades.
        """
        return self.api.list_combotrades()

    def margin(
        self,
        account: Optional[AccountData] = None,
        timeout: int = 5000,
        cb: Optional[Callable] = None,
    ) -> Any:
        """
        Queries futures account margin.
        """
        return self.api.margin(account=account, timeout=timeout, cb=cb)

    def trading_limits(
        self,
        account: Optional[AccountData] = None,
        timeout: int = 5000,
        cb: Optional[Callable] = None,
    ) -> Any:
        """
        Queries stock account trading limits.
        """
        return self.api.trading_limits(account=account, timeout=timeout, cb=cb)

    def activate_ca(self, ca_path: str, ca_passwd: str, person_id: str) -> Any:
        """
        Activates the CA certificate for trading.
        """
        return self.api.activate_ca(
            ca_path=ca_path, ca_passwd=ca_passwd, person_id=person_id
        )

    def get_ca_expiretime(self, person_id: str) -> str:
        """
        Checks the expiration time of the CA certificate.
        """
        return self.api.get_ca_expiretime(person_id=person_id)

    # Stock Reserve / Earmarking
    def stock_reserve_summary(self, account: Optional[AccountData] = None) -> Any:
        """
        Queries the reserve status of stocks.
        """
        return self.api.stock_reserve_summary(account=account)

    def reserve_stock(
        self, account: AccountData, contract: ContractData, share: int
    ) -> Any:
        """
        Applies for stock reservation (borrowing).
        """
        return self.api.reserve_stock(account=account, contract=contract, share=share)

    def stock_reserve_detail(self, account: Optional[AccountData] = None) -> Any:
        """
        Queries details of stock reservations.
        """
        return self.api.stock_reserve_detail(account=account)

    def reserve_earmarking(
        self, account: AccountData, contract: ContractData, share: int, price: float
    ) -> Any:
        """
        Applies for earmarking (pre-collection of funds).
        """
        return self.api.reserve_earmarking(
            account=account, contract=contract, share=share, price=price
        )

    def earmarking_detail(self, account: Optional[AccountData] = None) -> Any:
        """
        Queries details of earmarking applications.
        """
        return self.api.earmarking_detail(account=account)

    # Callbacks
    def set_order_callback(self, callback: Callable) -> None:
        """
        Sets a callback function to handle order and deal reports.
        """
        self.api.set_order_callback(callback)

    def set_on_tick_fop_v1_callback(
        self, callback: Callable, bind: bool = True
    ) -> None:
        self.api.quote.set_on_tick_fop_v1_callback(callback, bind=bind)

    def set_on_bidask_fop_v1_callback(
        self, callback: Callable, bind: bool = True
    ) -> None:
        self.api.quote.set_on_bidask_fop_v1_callback(callback, bind=bind)

    def set_on_quote_fop_v1_callback(
        self, callback: Callable, bind: bool = True
    ) -> None:
        self.api.quote.set_on_quote_fop_v1_callback(callback, bind=bind)

    def set_on_tick_stk_v1_callback(
        self, callback: Callable, bind: bool = True
    ) -> None:
        self.api.quote.set_on_tick_stk_v1_callback(callback, bind=bind)

    def set_on_bidask_stk_v1_callback(
        self, callback: Callable, bind: bool = True
    ) -> None:
        self.api.quote.set_on_bidask_stk_v1_callback(callback, bind=bind)

    def set_on_quote_stk_v1_callback(
        self, callback: Callable, bind: bool = True
    ) -> None:
        self.api.quote.set_on_quote_stk_v1_callback(callback, bind=bind)

    def on_event(self, callback: Callable) -> None:
        """
        Sets a callback for connection events.
        """
        self.api.quote.on_event(callback)

    # Decorators
    def on_tick_fop_v1(self, bind: bool = True) -> Callable:
        return self.api.on_tick_fop_v1(bind=bind)

    def on_tick_stk_v1(self, bind: bool = True) -> Callable:
        return self.api.on_tick_stk_v1(bind=bind)

    def on_bidask_fop_v1(self, bind: bool = True) -> Callable:
        return self.api.on_bidask_fop_v1(bind=bind)

    def on_bidask_stk_v1(self, bind: bool = True) -> Callable:
        return self.api.on_bidask_stk_v1(bind=bind)

    def on_quote_fop_v1(self, bind: bool = True) -> Callable:
        return self.api.on_quote_fop_v1(bind=bind)

    def on_quote_stk_v1(self, bind: bool = True) -> Callable:
        return self.api.on_quote_stk_v1(bind=bind)
