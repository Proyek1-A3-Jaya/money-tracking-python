from datetime import date
from auth.global_def import User

class Transaction():
    date
    debit: int
    credit: int
    outcome: int

    def __init__(self, date, debit: int, credit: int, outcome: int):
        self.date = date
        self.debit = debit
        self.credit = credit
        self.outcome = outcome

    def tampilTransaksi(self):
        print(f"{self.date} | {self.debit} | {self.credit} | {self.outcome}")

# def showTransactions():