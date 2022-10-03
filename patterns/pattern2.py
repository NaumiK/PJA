import datetime as dt
from datep import csd
from patterns.pattern import Pattern

class Pattern2(Pattern):
    def __init__(self, ta = dt.time(1, 0), tb = dt.time(6, 0)):
        super().__init__()
        self.ta = ta
        self.tb = tb

    def do_stuff(self, cards: list[str], transactions: dict, transaction_id: list[str]) -> None:
        super().do_stuff(cards, transactions, transaction_id)
        for i in transaction_id:
            if self.ta <= csd(transactions[i]["date"]).time() <= self.tb:
                self.printer(transactions[i])
