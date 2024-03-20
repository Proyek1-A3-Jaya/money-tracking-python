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

def showMonthlyRecap(year, month):
    """
    Menampilkan rekap transaksi bulanan.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    """
    totalDebit = 0
    totalCredit = 0
    with open('money.txt','r') as file:
        for line in file:
            data = line.split('|')
            transDate = data[0].strip()
            transYear, transMonth, _ = transDate.split('-')
            if int(transYear) == year and int(transMonth) == month:
                totalDebit += int(data[1].strip())
                totalCredit += int(data[2].strip())
    print(f"Rekap Bulan {month}/{year}:")
    print(f"Total Pemasukan {totalDebit}")
    print(f"Total Pengeluaran {totalCredit}")
