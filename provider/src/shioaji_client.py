"""
provider.src.shioaji_client -.
"""

from typing import Any, List

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

    def place_order(self, contract: Any, order: Order):
        return self.api.place_order(contract, order)

    def update_order(self, trade: Trade, price: float, qty: int):
        return self.api.update_order(trade, price=price, qty=qty)

    def cancel_order(self, trade: Trade):
        return self.api.cancel_order(trade)

    def update_status(self, account: Account):
        return self.api.update_status(account)

    def list_trades(self):
        return self.api.list_trades()

    def list_positions(self, account: Account):
        return self.api.list_positions(account)

    def snapshots(self, contracts: List[Any]):
        return self.api.snapshots(contracts)

    def ticks(self, contract: Any, date: str):
        return self.api.ticks(contract, date)

    def kbars(self, contract: Any, start: str, end: str):
        return self.api.kbars(contract, start, end)

    def settlements(self, account: Account):
        return self.api.settlements(account)

    def margin(self, account: Account):
        return self.api.margin(account)

    def list_profit_loss(self, account: Account):
        return self.api.list_profit_loss(account)

    def list_profit_loss_detail(self, account: Account):
        return self.api.list_profit_loss_detail(account)

    def list_profit_loss_summary(self, account: Account):
        return self.api.list_profit_loss_summary(account)

