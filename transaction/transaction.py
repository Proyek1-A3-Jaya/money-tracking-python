from datetime import datetime, timedelta
import transaction.global_def as Trans
import calendar


def recordDebit():
    """
    Mencatat pemasukan (debit) yang diinputkan oleh pengguna.

    Author
    -----
    - Farrel Zandra - 231524007 - @quack22
    """
    # Input data transaksi berupa tanggal, debit, credit, dan outcome
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    debit = int(input("Masukkan jumlah pemasukan: "))

    newTransaction = Trans.Transaction(date, debit, 0, 0)
    saveTransaction(newTransaction)


def recordCredit():
    """
    Mencatat pengeluaran (credit) yang diinputkan oleh pengguna.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    """
    date = datetime.now().strptime("%Y-%m-%d %H-%M-%S")
    credit = int(input("Masukkan jumlah pengeluaran: "))

    newTransaction = Trans.Transaction(date, 0, credit, 0)
    saveTransaction(newTransaction)


def saveTransaction(transaction):
    """
    Menyimpan transaksi ke dalam file 'money.txt'.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    """
    with open("money.txt", "a") as file:
        file.write(
            f"{transaction.date} | {transaction.debit} | {transaction.credit} | {transaction.outcome}\n"
        )
    print("Transaksi berhasil disimpan!")


def showMonthlyRecap(year, month):
    """
    Menampilkan rekap transaksi bulanan.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    """
    year = int(input("Masukkan tahun (contoh: 2024): "))
    month = int(input("Masukkan bulan (contoh: 1 untuk Januari): "))
    totalDebit = 0
    totalCredit = 0
    with open("money.txt", "r") as file:
        for line in file:
            data = line.split("|")
            transDate = data[0].strip()
            transYear, transMonth, _ = transDate.split("-")
            if int(transYear) == year and int(transMonth) == month:
                totalDebit += int(data[1].strip())
                totalCredit += int(data[2].strip())
    print(f"Rekap Bulan {month}/{year}:")
    print(f"Total Pemasukan {totalDebit:,}")
    print(f"Total Pengeluaran {totalCredit:,}")


def showDailyRecap(year, month, day):
    """
    Menampilkan rekap transaksi bulanan.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    """
    year = int(input("Masukkan tahun (contoh: 2024): "))
    month = int(input("Masukkan bulan (contoh: 1 untuk Januari): "))
    day = int(input("Masukkan tanggal: "))
    totalDebit = 0
    totalCredit = 0

    with open("money.txt", "r") as file:
        for line in file:
            data = line.split("|")
            transDateTime = data[
                0
            ].strip()  # mengambil elemen pertama dari array transDateTime.
            transDate = transDateTime.split()[
                0
            ]  # memisahkan tanggal dan waktu, kemudian mengambil tanggal saja.
            transYear, transMonth, transDay = transDate.split("-")
            if (
                int(transYear) == year
                and int(transMonth) == month
                and int(transDay) == day
            ):
                totalDebit += int(data[1].strip())
                totalCredit += int(data[2].strip())
    print(f"Rekap tanggal {day}/{month}/{year}")
    print("-----------------------------------")
    print(f"Total Pemasukan: {totalDebit:,}")
    print(f"Total Pengeluaran: {totalCredit:,}")


def showWeeklyRecap(year, month):
    """
    Menampilkan rekap transaksi mingguan dalam satu bulan.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    """
    countDay = calendar.monthrange(year, month)[1]
    startDate = datetime(year, month, 1)
    endDate = datetime(year, month, countDay)

    currentDate = startDate
    while currentDate <= endDate:
        nextWeek = currentDate + timedelta(
            days=(6 - currentDate.weekday())
        )  # penghitungan tanggal akhir minggu
        if nextWeek > endDate:
            nextWeek = endDate  # tanggal akhir minggu tidak boleh melebihi tanggal akhir bulan.

        totalDebit = 0
        totalCredit = 0

        with open("money.txt", "r") as file:
            for line in file:
                data = line.split("|")
                transDate = datetime.strptime(data[0].strip(), "%Y-%m-%d %H:%M:%S")
                if currentDate <= transDate <= nextWeek:
                    debit = int(data[1].strip())
                    credit = int(data[2].strip())
                    totalDebit += debit
                    totalCredit += credit

        print(
            f"Rekap minggu {currentDate.strftime('%d %B %Y')} - {nextWeek.strftime('%d %B %Y')}:"
        )
        print("----------------------------------")
        print(f"Total Pemasukan  : Rp{totalDebit:,}")
        print(f"Total Pengeluaran  : Rp{totalCredit:,}")
        print()

        currentDate = nextWeek + timedelta(days=1)  # lompat ke minggu selanjutnya.


def readTransaction(file_name: str):
    """
    Membaca transaksi dari file dan mengembalikan daftar transaksi.

    Author
    ------
    Farras Ahmad Rasyid - 231524006 - @bamoebin

    Parameter:
        file_name (str): Nama file yang berisi data transaksi.

    Return:
        list: Daftar transaksi yang dibaca dari file.
    """
    transactions = []

    try:
        with open(file_name, "r") as file:
            for line in file:
                data = line.strip().split("|")
                trans_date = data[0].strip()
                debit = int(data[1].strip())
                credit = int(data[2].strip())
                outcome = int(data[3].strip())

                # Membuat objek Transaction dari data yang dibaca
                newtransaction = Trans.Transaction(trans_date, debit, credit, outcome)
                transactions.append(newtransaction)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan saat membaca file:", str(e))

    return transactions
