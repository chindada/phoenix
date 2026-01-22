"""
provider.src.shioaji_client -.
"""

from typing import Any, Callable, List

import shioaji as sj
from shioaji.account import Account
from shioaji.data import CreditEnquire, ShortStockSource, Snapshot, Ticks, UsageStatus
from shioaji.order import Order, Trade


class ShioajiClient:
    """
    ShioajiClient -.
    """

    def __init__(self, simulation: bool = False):
        self.api = sj.Shioaji(simulation=simulation)

    def login(self, api_key: str, secret_key: str):
        """
        Login to the Shioaji API.

        Args:
            api_key (str): Your API key.
            secret_key (str): Your secret key.
        """
        self.api.login(api_key, secret_key)

    def logout(self) -> bool:
        """
        Logout from the Shioaji API.

        Returns:
            bool: True if logout was successful.
        """
        return self.api.logout()

    def usage(self) -> UsageStatus:
        """
        Retrieve usage information.

        Returns:
            UsageStatus: Object containing usage statistics.
        """
        return self.api.usage()

    def list_accounts(self) -> List[Account]:
        """
        List all available trading accounts.

        Returns:
            List[Account]: A list of trading accounts.
        """
        return self.api.list_accounts()

    def set_default_account(self, account: Account):
        """
        Set the default account for trading.

        Args:
            account (Account): The account to set as default.
        """
        return self.api.set_default_account(account)

    def account_balance(self) -> Any:
        """
        Get the account balance.

        Returns:
            Any: The account balance object (e.g., AccountBalance).
        """
        return self.api.account_balance()

    def place_order(self, contract: Any, order: Order) -> Trade:
        """
        Place a new order.

        Args:
            contract (Any): The contract to trade.
            order (Order): The order details.

        Returns:
            Trade: The placed trade object.
        """
        return self.api.place_order(contract, order)

    def place_comboorder(self, combo_contract: Any, order: Any) -> Trade:
        """
        Place a combination order.

        Args:
            combo_contract (Any): The combination contract to trade.
            order (Any): The combination order details (ComboOrder).

        Returns:
            Trade: The placed combo trade object.
        """
        return self.api.place_comboorder(combo_contract, order)

    def update_order(self, trade: Trade, price: float, qty: int) -> Trade:
        """
        Update an existing order.

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

        Args:
            trade (Trade): The trade to cancel.

        Returns:
            Trade: The canceled trade object.
        """
        return self.api.cancel_order(trade)

    def cancel_comboorder(self, combotrade: Any) -> Any:
        """
        Cancel a combination order.

        Args:
            combotrade (Any): The combination trade to cancel.

        Returns:
            Any: The canceled combo trade object.
        """
        return self.api.cancel_comboorder(combotrade)

    def update_status(self, account: Account):
        """
        Update the status of orders and trades for an account.

        Args:
            account (Account): The account to update status for.
        """
        return self.api.update_status(account)

    def update_combostatus(self, account: Account):
        """
        Update the status of combination orders for an account.

        Args:
            account (Account): The account to update status for.
        """
        return self.api.update_combostatus(account)

    def list_trades(self) -> List[Trade]:
        """
        List all trades.

        Returns:
            List[Trade]: A list of all trades.
        """
        return self.api.list_trades()

    def list_combotrades(self) -> List[Any]:
        """
        List all combination trades.

        Returns:
            List[Any]: A list of all combination trades (ComboTrade).
        """
        return self.api.list_combotrades()

    def order_deal_records(self, account: Account) -> List[Any]:
        """
        Get order deal records.

        Args:
            account (Account): The account to query.

        Returns:
            List[Any]: A list of order deal records.
        """
        return self.api.order_deal_records(account)

    def list_positions(self, account: Account) -> List[Any]:
        """
        List current positions for an account.

        Args:
            account (Account): The account to query.

        Returns:
            List[Any]: A list of positions (StockPosition or FuturePosition).
        """
        return self.api.list_positions(account)

    def list_position_detail(self, account: Account, detail_id: int) -> List[Any]:
        """
        Get detailed information for a specific position.

        Args:
            account (Account): The account to query.
            detail_id (int): The ID of the position.

        Returns:
            List[Any]: A list of position details (StockPositionDetail or FuturePositionDetail).
        """
        return self.api.list_position_detail(account, detail_id)

    def list_profit_loss(self, account: Account) -> List[Any]:
        """
        List realized profit and loss.

        Args:
            account (Account): The account to query.

        Returns:
            List[Any]: A list of profit and loss entries.
        """
        return self.api.list_profit_loss(account)

    def list_profit_loss_detail(self, account: Account, detail_id: int) -> List[Any]:
        """
        Get detailed realized profit and loss for a specific entry.

        Args:
            account (Account): The account to query.
            detail_id (int): The ID of the profit/loss entry.

        Returns:
            List[Any]: A list of profit and loss details.
        """
        return self.api.list_profit_loss_detail(account, detail_id)

    def list_profit_loss_summary(self, account: Account) -> List[Any]:
        """
        Get a summary of profit and loss.

        Args:
            account (Account): The account to query.

        Returns:
            List[Any]: A list of profit and loss summaries.
        """
        return self.api.list_profit_loss_summary(account)

    def settlements(self, account: Account) -> List[Any]:
        """
        Get settlement information.

        Args:
            account (Account): The account to query.

        Returns:
            List[Any]: A list of settlement objects (SettlementV1).
        """
        return self.api.settlements(account)

    def list_settlements(self, account: Account) -> List[Any]:
        """
        List settlement information (alias for settlements in some contexts or versions).

        Args:
            account (Account): The account to query.

        Returns:
            List[Any]: A list of settlement objects.
        """
        return self.api.list_settlements(account)

    def margin(self, account: Account) -> Any:
        """
        Get margin information for a futures account.

        Args:
            account (Account): The account to query.

        Returns:
            Any: The margin information object (Margin).
        """
        return self.api.margin(account)

    def trading_limits(self, account: Account) -> Any:
        """
        Get trading limits for a stock account.

        Args:
            account (Account): The account to query.

        Returns:
            Any: The trading limits object (TradingLimits).
        """
        return self.api.trading_limits(account)

    def stock_reserve_summary(self, account: Account) -> Any:
        """
        Get stock reserve summary.

        Args:
            account (Account): The account to query.

        Returns:
            Any: The stock reserve summary response.
        """
        return self.api.stock_reserve_summary(account)

    def stock_reserve_detail(self, account: Account) -> Any:
        """
        Get stock reserve details.

        Args:
            account (Account): The account to query.

        Returns:
            Any: The stock reserve detail response.
        """
        return self.api.stock_reserve_detail(account)

    def reserve_stock(self, account: Account, contract: Any, share: int) -> Any:
        """
        Reserve stock for borrowing.

        Args:
            account (Account): The account to use.
            contract (Any): The contract to reserve.
            share (int): The number of shares to reserve.

        Returns:
            Any: The reserve stock response.
        """
        return self.api.reserve_stock(account, contract, share)

    def earmarking_detail(self, account: Account) -> Any:
        """
        Get earmarking details.

        Args:
            account (Account): The account to query.

        Returns:
            Any: The earmarking detail response.
        """
        return self.api.earmarking_detail(account)

    def reserve_earmarking(
        self, account: Account, contract: Any, share: int, price: float
    ) -> Any:
        """
        Apply for earmarking.

        Args:
            account (Account): The account to use.
            contract (Any): The contract involved.
            share (int): The number of shares.
            price (float): The price per share.

        Returns:
            Any: The reserve earmarking response.
        """
        return self.api.reserve_earmarking(account, contract, share, price)

    def snapshots(self, contracts: List[Any]) -> List[Snapshot]:
        """
        Get market snapshots for a list of contracts.

        Args:
            contracts (List[Any]): List of contracts to query.

        Returns:
            List[Snapshot]: A list of snapshot objects.
        """
        return self.api.snapshots(contracts)

    def ticks(self, contract: Any, date: str) -> Ticks:
        """
        Get tick data for a specific contract and date.

        Args:
            contract (Any): The contract to query.
            date (str): The date in YYYY-MM-DD format.

        Returns:
            Ticks: The tick data object.
        """
        return self.api.ticks(contract, date)

    def kbars(self, contract: Any, start: str, end: str) -> Any:
        """
        Get K-bar (candlestick) data for a specific contract and date range.

        Args:
            contract (Any): The contract to query.
            start (str): The start date in YYYY-MM-DD format.
            end (str): The end date in YYYY-MM-DD format.

        Returns:
            Any: The K-bar data object (Kbars).
        """
        return self.api.kbars(contract, start, end)

    def daily_quotes(self, date: str) -> Any:
        """
        Get daily quotes.

        Args:
            date (str): The date to query.

        Returns:
            Any: The daily quotes object (DailyQuotes).
        """
        return self.api.daily_quotes(date)

    def credit_enquires(self, contracts: List[Any]) -> List[CreditEnquire]:
        """
        Enquire about credit for a list of contracts.

        Args:
            contracts (List[Any]): List of contracts to query.

        Returns:
            List[CreditEnquire]: A list of credit enquiry results.
        """
        return self.api.credit_enquires(contracts)

    def short_stock_sources(self, contracts: List[Any]) -> List[ShortStockSource]:
        """
        Get short stock sources for a list of contracts.

        Args:
            contracts (List[Any]): List of contracts to query.

        Returns:
            List[ShortStockSource]: A list of short stock sources.
        """
        return self.api.short_stock_sources(contracts)

    def scanners(
        self, scanner_type: Any, ascending: bool, date: str, count: int
    ) -> List[Any]:
        """
        Get scanner results (ranked stocks).

        Args:
            scanner_type (Any): The type of scanner to run.
            ascending (bool): Whether to sort in ascending order.
            date (str): The date for the scan.
            count (int): The number of results to return.

        Returns:
            List[Any]: A list of scanner items.
        """
        return self.api.scanners(
            scanner_type, ascending=ascending, date=date, count=count
        )

    def punish(self) -> Any:
        """
        Get punishment information (disposition stocks).

        Returns:
            Any: The punish information object (Punish).
        """
        return self.api.punish()

    def notice(self) -> Any:
        """
        Get notice information (attention stocks).

        Returns:
            Any: The notice information object (Notice).
        """
        return self.api.notice()

    def fetch_contracts(self, contract_download: bool):
        """
        Manually fetch contracts.

        Args:
            contract_download (bool): Whether to download contracts.
        """
        return self.api.fetch_contracts(contract_download)

    def set_context(self, context: Any):
        """
        Set the context for the API.

        Args:
            context (Any): The context object.
        """
        self.api.set_context(context)

    def activate_ca(self, ca_path: str, ca_passwd: str, person_id: str) -> bool:
        """
        Activate the Certificate Authority (CA).

        Args:
            ca_path (str): Path to the CA file.
            ca_passwd (str): Password for the CA.
            person_id (str): Person ID associated with the CA.

        Returns:
            bool: True if activation was successful.
        """
        return self.api.activate_ca(ca_path, ca_passwd, person_id)

    def get_ca_expiretime(self, person_id: str) -> str:
        """
        Get the CA expiration time.

        Args:
            person_id (str): Person ID to check.

        Returns:
            str: The expiration time string.
        """
        return self.api.get_ca_expiretime(person_id)

    def subscribe_trade(self, account: Account) -> bool:
        """
        Subscribe to trade updates for an account.

        Args:
            account (Account): The account to subscribe to.

        Returns:
            bool: True if subscription was successful.
        """
        return self.api.subscribe_trade(account)

    def unsubscribe_trade(self, account: Account) -> bool:
        """
        Unsubscribe from trade updates for an account.

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

        Args:
            func (Callable): The callback function.

        Returns:
            Callable: The registered callback function.
        """
        return self.api.on_event(func)

    def on_quote(self, func: Callable) -> Callable:
        """
        Decorator to register a callback for quotes.

        Args:
            func (Callable): The callback function.

        Returns:
            Callable: The registered callback function.
        """
        return self.api.on_quote(func)

    def on_session_down(self, func: Callable) -> Callable:
        """
        Decorator to register a callback for session down events.

        Args:
            func (Callable): The callback function.

        Returns:
            Callable: The registered callback function.
        """
        return self.api.on_session_down(func)

    def set_order_callback(self, func: Callable):
        """
        Set a callback for order updates.

        Args:
            func (Callable): The callback function.
        """
        self.api.set_order_callback(func)

    def set_session_down_callback(self, func: Callable):
        """
        Set a callback for session down events.

        Args:
            func (Callable): The callback function.
        """
        self.api.set_session_down_callback(func)

    def on_bidask_fop_v1(self, bind: bool = False) -> Callable:
        """
        Decorator for FOP v1 bid/ask updates.

        Args:
            bind (bool): Whether to bind the callback.

        Returns:
            Callable: The decorator function.
        """
        return self.api.on_bidask_fop_v1(bind)

    def on_bidask_stk_v1(self, bind: bool = False) -> Callable:
        """
        Decorator for stock v1 bid/ask updates.

        Args:
            bind (bool): Whether to bind the callback.

        Returns:
            Callable: The decorator function.
        """
        return self.api.on_bidask_stk_v1(bind)

    def on_quote_fop_v1(self, bind: bool = False) -> Callable:
        """
        Decorator for FOP v1 quote updates.

        Args:
            bind (bool): Whether to bind the callback.

        Returns:
            Callable: The decorator function.
        """
        return self.api.on_quote_fop_v1(bind)

    def on_quote_stk_v1(self, bind: bool = False) -> Callable:
        """
        Decorator for stock v1 quote updates.

        Args:
            bind (bool): Whether to bind the callback.

        Returns:
            Callable: The decorator function.
        """
        return self.api.on_quote_stk_v1(bind)

    def on_tick_fop_v1(self, bind: bool = False) -> Callable:
        """
        Decorator for FOP v1 tick updates.

        Args:
            bind (bool): Whether to bind the callback.

        Returns:
            Callable: The decorator function.
        """
        return self.api.on_tick_fop_v1(bind)

    def on_tick_stk_v1(self, bind: bool = False) -> Callable:
        """
        Decorator for stock v1 tick updates.

        Args:
            bind (bool): Whether to bind the callback.

        Returns:
            Callable: The decorator function.
        """
        return self.api.on_tick_stk_v1(bind)
