import json
import datetime as dt
from pprint import pprint
from datep import csd
from patterns import *


if __name__ == "__main__":
    pat: Pattern
    pat = Pattern3()
    
    pat.printer = pprint

    with open("jsonf/transactions.json") as f:
        transactions = json.load(f)["transactions"]
        transaction_id = transactions.keys()
        cards = []
        for i in transaction_id:
            if transactions[i]["card"] not in cards:
                cards.append(transactions[i]["card"])
        pat.do_stuff(cards=cards, transactions=transactions, transaction_id=transaction_id)
