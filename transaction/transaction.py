from datetime import datetime
import transaction.global_def as Trans

def recordDebit():
    """
    Mencatat pemasukan (debit) yang diinputkan oleh pengguna.

    Author
    -----
    - Farrel Zandra - 231524007 - @quack22
    """
    # Input data transaksi berupa tanggal, debit, credit, dan outcome
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    debit = int(input('Masukkan jumlah pemasukan: '))

    newTransaction = Trans.Transaction(date, debit, 0, 0)
    saveTransaction(newTransaction)

def recordCredit():
    """
    Mencatat pengeluaran (credit) yang diinputkan oleh pengguna.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    """
    date = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    credit = int(input('Masukkan jumlah pengeluaran: '))

    newTransaction = Trans.Transaction(date, 0, credit, 0)
    saveTransaction(newTransaction)

def saveTransaction(transaction):
    """
    Menyimpan transaksi ke dalam file.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    """
    with open('money.txt', 'a') as file:
        file.write(f"{transaction.date} | {transaction.debit} | {transaction.credit} | {transaction.outcome}\n")
    print('Transaksi berhasil disimpan!')