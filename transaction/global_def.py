from datetime import date
from auth.global_def import User
import transaction.transaction as tr

class Transaction():
    date
    debit: int
    credit: int
    outcome: int
    category = ["Makanan/Minuman", "Pendidikan", "Kesehatan", "Belanja", "Transportasi", "Lainnya"]

    def __init__(self, date, debit, credit, outcome, category):
        self.date = date
        self.debit = debit
        self.credit = credit
        self.outcome = outcome
        self.category = category

    def tampilTransaksi(self):
        print(f"{self.date} | {self.debit} | {self.credit} | {self.outcome}")

def recordDebit():
    tr.recordDebit()

def recordCredit():
    tr.recordCredit()