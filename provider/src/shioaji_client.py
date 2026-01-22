"""
provider.src.shioaji_client -.
"""

from datetime import date as dt_date
from datetime import datetime
from typing import Any, Callable, List, Union

import shioaji as sj
from shioaji.account import Account
from shioaji.constant import ScannerType
from shioaji.contracts import (
    BaseContract,
    ComboContract,
    Contract,
    Future,
    Index,
    Option,
    Stock,
)
from shioaji.data import (
    CreditEnquire,
    DailyQuotes,
    Kbars,
    Notice,
    Punish,
    ScannerItem,
    ShortStockSource,
    Snapshot,
    Ticks,
    UsageStatus,
)
from shioaji.order import ComboOrder, ComboTrade, Order, OrderDealRecords, Trade
from shioaji.position import (
    AccountBalance,
    FuturePosition,
    FuturePositionDetail,
    FutureProfitDetail,
    FutureProfitLoss,
    FutureProfitLossSummary,
    Margin,
    Settlement,
    StockPosition,
    StockPositionDetail,
    StockProfitDetail,
    StockProfitLoss,
    StockProfitLossSummary,
    TradingLimits,
)
from shioaji.reserve import (
    EarmarkStocksDetailResponse,
    ReserveEarmarkingResponse,
    ReserveStockResponse,
    ReserveStocksDetailResponse,
    ReserveStocksSummaryResponse,
)


class ShioajiClient:
    """
    ShioajiClient -.
    """

    def __init__(self, simulation: bool = False):
        self.api = sj.Shioaji(simulation=simulation)

    def login(self, api_key: str, secret_key: str) -> List[Account]:
        """
        Login to the Shioaji API.
        登入

        Args:
            api_key (str): Your API key.
            secret_key (str): Your secret key.

        Returns:
            List[Account]: A list of trading accounts.
        """
        return self.api.login(api_key, secret_key)

    def logout(self) -> bool:
        """
        Logout from the Shioaji API.
        登出

        Returns:
            bool: True if logout was successful.
        """
        return self.api.logout()

    def usage(self) -> UsageStatus:
        """
        Retrieve usage information.
        使用量

        Returns:
            UsageStatus: Object containing usage statistics.
        """
        return self.api.usage()

    def list_accounts(self) -> List[Account]:
        """
        List all available trading accounts.
        帳號列表

        Returns:
            List[Account]: A list of trading accounts.
        """
        return self.api.list_accounts()

    def set_default_account(self, account: Account):
        """
        Set the default account for trading.
        設定預設帳號

        Args:
            account (Account): The account to set as default.
        """
        return self.api.set_default_account(account)

    def account_balance(self) -> AccountBalance:
        """
        Get the account balance.
        帳戶餘額

        Returns:
            AccountBalance: The account balance object.
        """
        return self.api.account_balance()

    def place_order(self, contract: Contract, order: Order) -> Trade:
        """
        Place a new order.
        下單

        Args:
            contract (Contract): The contract to trade.
            order (Order): The order details.

        Returns:
            Trade: The placed trade object.
        """
        return self.api.place_order(contract, order)

    def place_comboorder(
        self, combo_contract: ComboContract, order: ComboOrder
    ) -> ComboTrade:
        """
        Place a combination order.
        組合單下單

        Args:
            combo_contract (ComboContract): The combination contract to trade.
            order (ComboOrder): The combination order details.

        Returns:
            ComboTrade: The placed combo trade object.
        """
        return self.api.place_comboorder(combo_contract, order)

    def update_order(self, trade: Trade, price: float, qty: int) -> Trade:
        """
        Update an existing order.
        修改委託單

        Args:
            trade (Trade): The trade to update.
            price (float): The new price.
            qty (int): The new quantity.

        Returns:
            Trade: The updated trade object.
        """
        return self.api.update_order(trade, price=price, qty=qty)

    def cancel_order(self, trade: Trade) -> Trade:
        """
        Cancel an existing order.
        撤銷委託單

        Args:
            trade (Trade): The trade to cancel.

        Returns:
            Trade: The canceled trade object.
        """
        return self.api.cancel_order(trade)

    def cancel_comboorder(self, combotrade: ComboTrade) -> ComboTrade:
        """
        Cancel a combination order.
        撤銷組合單委託

        Args:
            combotrade (ComboTrade): The combination trade to cancel.

        Returns:
            ComboTrade: The canceled combo trade object.
        """
        return self.api.cancel_comboorder(combotrade)

    def update_status(self, account: Account):
        """
        Update the status of orders and trades for an account.
        更新委託單狀態

        Args:
            account (Account): The account to update status for.
        """
        return self.api.update_status(account)

    def update_combostatus(self, account: Account):
        """
        Update the status of combination orders for an account.
        更新組合單狀態

        Args:
            account (Account): The account to update status for.
        """
        return self.api.update_combostatus(account)

    def list_trades(self) -> List[Trade]:
        """
        List all trades.
        委託列表

        Returns:
            List[Trade]: A list of all trades.
        """
        return self.api.list_trades()

    def list_combotrades(self) -> List[ComboTrade]:
        """
        List all combination trades.
        組合單委託列表

        Returns:
            List[ComboTrade]: A list of all combination trades.
        """
        return self.api.list_combotrades()

    def order_deal_records(self, account: Account) -> List[OrderDealRecords]:
        """
        Get order deal records.
        委託成交紀錄

        Args:
            account (Account): The account to query.

        Returns:
            List[OrderDealRecords]: A list of order deal records.
        """
        return self.api.order_deal_records(account)

    def list_positions(
        self, account: Account
    ) -> List[Union[StockPosition, FuturePosition]]:
        """
        List current positions for an account.
        查詢部位

        Args:
            account (Account): The account to query.

        Returns:
            List[Union[StockPosition, FuturePosition]]: A list of positions.
        """
        return self.api.list_positions(account)

    def list_position_detail(
        self, account: Account, detail_id: int
    ) -> List[Union[StockPositionDetail, FuturePositionDetail]]:
        """
        Get detailed information for a specific position.
        查詢部位詳細資訊

        Args:
            account (Account): The account to query.
            detail_id (int): The ID of the position.

        Returns:
            List[Union[StockPositionDetail, FuturePositionDetail]]: A list of position details.
        """
        return self.api.list_position_detail(account, detail_id)

    def list_profit_loss(
        self, account: Account
    ) -> List[Union[StockProfitLoss, FutureProfitLoss]]:
        """
        List realized profit and loss.
        查詢損益

        Args:
            account (Account): The account to query.

        Returns:
            List[Union[StockProfitLoss, FutureProfitLoss]]: A list of profit and loss entries.
        """
        return self.api.list_profit_loss(account)

    def list_profit_loss_detail(
        self, account: Account, detail_id: int
    ) -> List[Union[StockProfitDetail, FutureProfitDetail]]:
        """
        Get detailed realized profit and loss for a specific entry.
        查詢損益詳細資訊

        Args:
            account (Account): The account to query.
            detail_id (int): The ID of the profit/loss entry.

        Returns:
            List[Union[StockProfitDetail, FutureProfitDetail]]: A list of profit and loss details.
        """
        return self.api.list_profit_loss_detail(account, detail_id)

    def list_profit_loss_summary(
        self, account: Account
    ) -> List[Union[StockProfitLossSummary, FutureProfitLossSummary]]:
        """
        Get a summary of profit and loss.
        查詢損益匯總

        Args:
            account (Account): The account to query.

        Returns:
            List[Union[StockProfitLossSummary, FutureProfitLossSummary]]: A list of profit and loss summaries.
        """
        return self.api.list_profit_loss_summary(account)

    def settlements(self, account: Account) -> List[Settlement]:
        """
        Get settlement information.
        查詢結算資訊

        Args:
            account (Account): The account to query.

        Returns:
            List[Settlement]: A list of settlement objects.
        """
        return self.api.settlements(account)

    def list_settlements(self, account: Account) -> List[Settlement]:
        """
        List settlement information.
        結算清單

        Args:
            account (Account): The account to query.

        Returns:
            List[Settlement]: A list of settlement objects.
        """
        return self.api.list_settlements(account)

    def margin(self, account: Account) -> Margin:
        """
        Get margin information for a futures account.
        查詢保證金

        Args:
            account (Account): The account to query.

        Returns:
            Margin: The margin information object.
        """
        return self.api.margin(account)

    def trading_limits(self, account: Account) -> TradingLimits:
        """
        Get trading limits for a stock account.
        交易限額

        Args:
            account (Account): The account to query.

        Returns:
            TradingLimits: The trading limits object.
        """
        return self.api.trading_limits(account)

    def stock_reserve_summary(self, account: Account) -> ReserveStocksSummaryResponse:
        """
        Get stock reserve summary.
        股票券源彙總

        Args:
            account (Account): The account to query.

        Returns:
            ReserveStocksSummaryResponse: The stock reserve summary response.
        """
        return self.api.stock_reserve_summary(account)

    def stock_reserve_detail(self, account: Account) -> ReserveStocksDetailResponse:
        """
        Get stock reserve details.
        股票券源明細

        Args:
            account (Account): The account to query.

        Returns:
            ReserveStocksDetailResponse: The stock reserve detail response.
        """
        return self.api.stock_reserve_detail(account)

    def reserve_stock(
        self, account: Account, contract: Contract, share: int
    ) -> ReserveStockResponse:
        """
        Reserve stock for borrowing.
        預約借券

        Args:
            account (Account): The account to use.
            contract (Contract): The contract to reserve.
            share (int): The number of shares to reserve.

        Returns:
            ReserveStockResponse: The reserve stock response.
        """
        return self.api.reserve_stock(account, contract, share)

    def earmarking_detail(self, account: Account) -> EarmarkStocksDetailResponse:
        """
        Get earmarking details.
        圈存明細

        Args:
            account (Account): The account to query.

        Returns:
            EarmarkStocksDetailResponse: The earmarking detail response.
        """
        return self.api.earmarking_detail(account)

    def reserve_earmarking(
        self, account: Account, contract: Contract, share: int, price: float
    ) -> ReserveEarmarkingResponse:
        """
        Apply for earmarking.
        預約圈存

        Args:
            account (Account): The account to use.
            contract (Contract): The contract involved.
            share (int): The number of shares.
            price (float): The price per share.

        Returns:
            ReserveEarmarkingResponse: The reserve earmarking response.
        """
        return self.api.reserve_earmarking(account, contract, share, price)

    def snapshots(
        self, contracts: List[Union[Option, Future, Stock, Index]]
    ) -> List[Snapshot]:
        """
        Get market snapshots for a list of contracts.
        行情快照

        Args:
            contracts (List[Union[Option, Future, Stock, Index]]): List of contracts to query.

        Returns:
            List[Snapshot]: A list of snapshot objects.
        """
        return self.api.snapshots(contracts)

    def ticks(self, contract: BaseContract, date: str) -> Ticks:
        """
        Get tick data for a specific contract and date.
        獲取逐筆報價

        Args:
            contract (BaseContract): The contract to query.
            date (str): The date in YYYY-MM-DD format.

        Returns:
            Ticks: The tick data object.
        """
        return self.api.ticks(contract, date)

    def kbars(self, contract: BaseContract, start: str, end: str) -> Kbars:
        """
        Get K-bar (candlestick) data for a specific contract and date range.
        獲取K線資料

        Args:
            contract (BaseContract): The contract to query.
            start (str): The start date in YYYY-MM-DD format.
            end (str): The end date in YYYY-MM-DD format.

        Returns:
            Kbars: The K-bar data object.
        """
        return self.api.kbars(contract, start, end)

    def daily_quotes(self, date_query: dt_date) -> DailyQuotes:
        """
        Get daily quotes.
        每日報價

        Args:
            date_query (dt_date): The date to query.

        Returns:
            DailyQuotes: The daily quotes object.
        """
        return self.api.daily_quotes(date_query)

    def credit_enquires(self, contracts: List[Stock]) -> List[CreditEnquire]:
        """
        Enquire about credit for a list of contracts.
        信用交易查詢

        Args:
            contracts (List[Stock]): List of contracts to query.

        Returns:
            List[CreditEnquire]: A list of credit enquiry results.
        """
        return self.api.credit_enquires(contracts)

    def short_stock_sources(self, contracts: List[Stock]) -> List[ShortStockSource]:
        """
        Get short stock sources for a list of contracts.
        借券水源

        Args:
            contracts (List[Stock]): List of contracts to query.

        Returns:
            List[ShortStockSource]: A list of short stock sources.
        """
        return self.api.short_stock_sources(contracts)

    def scanners(
        self, scanner_type: ScannerType, ascending: bool, date_str: str, count: int
    ) -> List[ScannerItem]:
        """
        Get scanner results (ranked stocks).
        選股器

        Args:
            scanner_type (ScannerType): The type of scanner to run.
            ascending (bool): Whether to sort in ascending order.
            date_str (str): The date for the scan.
            count (int): The number of results to return.

        Returns:
            List[ScannerItem]: A list of scanner items.
        """
        return self.api.scanners(
            scanner_type, ascending=ascending, date=date_str, count=count
        )

    def punish(self) -> Punish:
        """
        Get punishment information (disposition stocks).
        處置股

        Returns:
            Punish: The punish information object.
        """
        return self.api.punish()

    def notice(self) -> Notice:
        """
        Get notice information (attention stocks).
        注意股

        Returns:
            Notice: The notice information object.
        """
        return self.api.notice()

    def fetch_contracts(self, contract_download: bool):
        """
        Manually fetch contracts.
        下載商品檔

        Args:
            contract_download (bool): Whether to download contracts.
        """
        return self.api.fetch_contracts(contract_download)

    def set_context(self, context: Any):
        """
        Set the context for the API.
        設定上下文

        Args:
            context (Any): The context object.
        """
        self.api.set_context(context)

    def activate_ca(self, ca_path: str, ca_passwd: str, person_id: str) -> bool:
        """
        Activate the Certificate Authority (CA).
        憑證開通

        Args:
            ca_path (str): Path to the CA file.
            ca_passwd (str): Password for the CA.
            person_id (str): Person ID associated with the CA.

        Returns:
            bool: True if activation was successful.
        """
        return self.api.activate_ca(ca_path, ca_passwd, person_id)

    def get_ca_expiretime(self, person_id: str) -> datetime:
        """
        Get the CA expiration time.
        憑證過期時間

        Args:
            person_id (str): Person ID to check.

        Returns:
            datetime: The expiration time.
        """
        return self.api.get_ca_expiretime(person_id)

    def subscribe_trade(self, account: Account) -> bool:
        """
        Subscribe to trade updates for an account.
        訂閱交易回報

        Args:
            account (Account): The account to subscribe to.

        Returns:
            bool: True if subscription was successful.
        """
        return self.api.subscribe_trade(account)

    def unsubscribe_trade(self, account: Account) -> bool:
        """
        Unsubscribe from trade updates for an account.
        取消訂閱交易回報

        Args:
            account (Account): The account to unsubscribe from.

        Returns:
            bool: True if unsubscription was successful.
        """
        return self.api.unsubscribe_trade(account)

    # Callbacks and Decorators
    def on_event(self, func: Callable) -> Callable:
        """
        Decorator to register a callback for events.
        事件回報

        Args:
            func (Callable): The callback function.

        Returns:
            Callable: The registered callback function.
        """
        return self.api.on_event(func)

    def on_quote(self, func: Callable) -> Callable:
        """
        Decorator to register a callback for quotes.
        行情回報

        Args:
            func (Callable): The callback function.

        Returns:
            Callable: The registered callback function.
        """
        return self.api.on_quote(func)

    def on_session_down(self, func: Callable) -> Callable:
        """
        Decorator to register a callback for session down events.
        連線中斷

        Args:
            func (Callable): The callback function.

        Returns:
            Callable: The registered callback function.
        """
        return self.api.on_session_down(func)

    def set_order_callback(self, func: Callable):
        """
        Set a callback for order updates.
        設定委託回報回呼

        Args:
            func (Callable): The callback function.
        """
        self.api.set_order_callback(func)

    def set_session_down_callback(self, func: Callable):
        """
        Set a callback for session down events.
        設定連線中斷回呼

        Args:
            func (Callable): The callback function.
        """
        self.api.set_session_down_callback(func)

    def on_bidask_fop_v1(self, bind: bool = False) -> Callable:
        """
        Decorator for FOP v1 bid/ask updates.
        期權五檔報價

        Args:
            bind (bool): Whether to bind the callback.

        Returns:
            Callable: The decorator function.
        """
        return self.api.on_bidask_fop_v1(bind)

    def on_bidask_stk_v1(self, bind: bool = False) -> Callable:
        """
        Decorator for stock v1 bid/ask updates.
        股票五檔報價

        Args:
            bind (bool): Whether to bind the callback.

        Returns:
            Callable: The decorator function.
        """
        return self.api.on_bidask_stk_v1(bind)

    def on_quote_fop_v1(self, bind: bool = False) -> Callable:
        """
        Decorator for FOP v1 quote updates.
        期權行情報價

        Args:
            bind (bool): Whether to bind the callback.

        Returns:
            Callable: The decorator function.
        """
        return self.api.on_quote_fop_v1(bind)

    def on_quote_stk_v1(self, bind: bool = False) -> Callable:
        """
        Decorator for stock v1 quote updates.
        股票行情報價

        Args:
            bind (bool): Whether to bind the callback.

        Returns:
            Callable: The decorator function.
        """
        return self.api.on_quote_stk_v1(bind)

    def on_tick_fop_v1(self, bind: bool = False) -> Callable:
        """
        Decorator for FOP v1 tick updates.
        期權逐筆報價

        Args:
            bind (bool): Whether to bind the callback.

        Returns:
            Callable: The decorator function.
        """
        return self.api.on_tick_fop_v1(bind)

    def on_tick_stk_v1(self, bind: bool = False) -> Callable:
        """
        Decorator for stock v1 tick updates.
        股票逐筆報價

        Args:
            bind (bool): Whether to bind the callback.

        Returns:
            Callable: The decorator function.
        """
        return self.api.on_tick_stk_v1(bind)