from datetime import date
from auth.global_def import User
import transaction.transaction as tr


class Transaction:
    date
    debit: int
    credit: int
    outcome: int
    category = [
        "Makanan/Minuman",
        "Pendidikan",
        "Kesehatan",
        "Belanja",
        "Transportasi",
        "Lainnya",
    ]

    def __init__(self, date, debit, credit, outcome, category):
        self.date = date
        self.debit = debit
        self.credit = credit
        self.outcome = outcome
        self.category = category

    def tampilTransaksi(self):
        print(f"{self.date} | {self.debit} | {self.credit} | {self.outcome}")


def recordDebit(user: User):
    tr.recordDebit(user)


def recordCredit(user: User):
    tr.recordCredit(user)


def showMonthlyRecap(user: User):
    tr.showMonthlyRecap(user)


def showWeeklyRecap(user: User):
    tr.showWeeklyRecap(user)


def showDailyRecap(user: User):
    tr.showDailyRecap(user)


def readTransaction(user: User):
    tr.readTransaction(user)


def printTransactions(user: User):
    tr.printTransactions(user)


def lastTransaction(user: User):
    tr.lastTransaction(user)


def createGoal():
    tr.createGoal()
