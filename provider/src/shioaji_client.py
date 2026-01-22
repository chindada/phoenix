"""
provider.src.shioaji_client -.
"""

from typing import Any, Callable, List

import shioaji as sj
from shioaji.account import Account
from shioaji.order import Order, Trade


class ShioajiClient:
    """
    ShioajiClient -.
    """

    def __init__(self, simulation: bool = False):
        self.api = sj.Shioaji(simulation=simulation)

    def login(self, api_key: str, secret_key: str):
        self.api.login(api_key, secret_key)

    def logout(self):
        return self.api.logout()

    def usage(self):
        return self.api.usage()

    def list_accounts(self):
        return self.api.list_accounts()

    def set_default_account(self, account: Account):
        return self.api.set_default_account(account)

    def account_balance(self):
        return self.api.account_balance()

    def place_order(self, contract: Any, order: Order):
        return self.api.place_order(contract, order)

    def place_comboorder(self, combo_contract: Any, order: Any):
        return self.api.place_comboorder(combo_contract, order)

    def update_order(self, trade: Trade, price: float, qty: int):
        return self.api.update_order(trade, price=price, qty=qty)

    def cancel_order(self, trade: Trade):
        return self.api.cancel_order(trade)

    def cancel_comboorder(self, combotrade: Any):
        return self.api.cancel_comboorder(combotrade)

    def update_status(self, account: Account):
        return self.api.update_status(account)

    def update_combostatus(self, account: Account):
        return self.api.update_combostatus(account)

    def list_trades(self):
        return self.api.list_trades()

    def list_combotrades(self):
        return self.api.list_combotrades()

    def order_deal_records(self, account: Account):
        return self.api.order_deal_records(account)

    def list_positions(self, account: Account):
        return self.api.list_positions(account)

    def list_position_detail(self, account: Account, detail_id: int):
        return self.api.list_position_detail(account, detail_id)

    def list_profit_loss(self, account: Account):
        return self.api.list_profit_loss(account)

    def list_profit_loss_detail(self, account: Account, detail_id: int):
        return self.api.list_profit_loss_detail(account, detail_id)

    def list_profit_loss_summary(self, account: Account):
        return self.api.list_profit_loss_summary(account)

    def settlements(self, account: Account):
        return self.api.settlements(account)

    def list_settlements(self, account: Account):
        return self.api.list_settlements(account)

    def margin(self, account: Account):
        return self.api.margin(account)

    def trading_limits(self, account: Account):
        return self.api.trading_limits(account)

    def stock_reserve_summary(self, account: Account):
        return self.api.stock_reserve_summary(account)

    def stock_reserve_detail(self, account: Account):
        return self.api.stock_reserve_detail(account)

    def reserve_stock(self, account: Account, contract: Any, share: int):
        return self.api.reserve_stock(account, contract, share)

    def earmarking_detail(self, account: Account):
        return self.api.earmarking_detail(account)

    def reserve_earmarking(
        self, account: Account, contract: Any, share: int, price: float
    ):
        return self.api.reserve_earmarking(account, contract, share, price)

    def snapshots(self, contracts: List[Any]):
        return self.api.snapshots(contracts)

    def ticks(self, contract: Any, date: str):
        return self.api.ticks(contract, date)

    def kbars(self, contract: Any, start: str, end: str):
        return self.api.kbars(contract, start, end)

    def daily_quotes(self, date: str):
        return self.api.daily_quotes(date)

    def credit_enquires(self, contracts: List[Any]):
        return self.api.credit_enquires(contracts)

    def short_stock_sources(self, contracts: List[Any]):
        return self.api.short_stock_sources(contracts)

    def scanners(
        self, scanner_type: Any, ascending: bool, date: str, count: int
    ):
        return self.api.scanners(
            scanner_type, ascending=ascending, date=date, count=count
        )

    def punish(self):
        return self.api.punish()

    def notice(self):
        return self.api.notice()

    def fetch_contracts(self, contract_download: bool):
        return self.api.fetch_contracts(contract_download)

    def set_context(self, context: Any):
        self.api.set_context(context)

    def activate_ca(self, ca_path: str, ca_passwd: str, person_id: str):
        return self.api.activate_ca(ca_path, ca_passwd, person_id)

    def get_ca_expiretime(self, person_id: str):
        return self.api.get_ca_expiretime(person_id)

    def subscribe_trade(self, account: Account):
        return self.api.subscribe_trade(account)

    def unsubscribe_trade(self, account: Account):
        return self.api.unsubscribe_trade(account)

    # Callbacks and Decorators
    def on_event(self, func: Callable):
        return self.api.on_event(func)

    def on_quote(self, func: Callable):
        return self.api.on_quote(func)

    def on_session_down(self, func: Callable):
        return self.api.on_session_down(func)

    def set_order_callback(self, func: Callable):
        self.api.set_order_callback(func)

    def set_session_down_callback(self, func: Callable):
        self.api.set_session_down_callback(func)

    def on_bidask_fop_v1(self, bind: bool):
        return self.api.on_bidask_fop_v1(bind)

    def on_bidask_stk_v1(self, bind: bool):
        return self.api.on_bidask_stk_v1(bind)

    def on_quote_fop_v1(self, bind: bool):
        return self.api.on_quote_fop_v1(bind)

    def on_quote_stk_v1(self, bind: bool):
        return self.api.on_quote_stk_v1(bind)

    def on_tick_fop_v1(self, bind: bool):
        return self.api.on_tick_fop_v1(bind)

    def on_tick_stk_v1(self, bind: bool):
        return self.api.on_tick_stk_v1(bind)