from datetime import datetime, timedelta
import transaction.global_def as Trans
import calendar
from datetime import datetime as dt
from auth.global_def import User
import os

def recordDebit(user : User):
    """
    Mencatat pemasukan (debit) yang diinputkan oleh pengguna.

    Author
    -----
    - Farrel Zandra - 231524007 - @quack22
    - Satria Permata Sejati - 231524026 - @WeirdoKitten
    """
    # Input data transaksi berupa tanggal, debit, credit, dan outcome
    pilihTanggal = int(input
    ("""
        pilih tanggal :
        1. hari ini
        2. input manual
    """))

    if pilihTanggal == 1:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if pilihTanggal == 2:
        # Meminta pengguna memasukkan tanggal secara manual satu per satu
        year = input("Masukkan tahun (Format: YYYY): ")
        month = input("Masukkan bulan (Format: MM): ")
        day = input("Masukkan hari (Format: DD): ")

        # Mengambil jam, menit, dan detik dari waktu sekarang
        current_time = datetime.datetime.now()
        hour = current_time.strftime("%H")
        minute = current_time.strftime("%M")
        second = current_time.strftime("%S")

        # Mengonversi input tanggal menjadi objek datetime
        try:
            date = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
        except ValueError:
            print("Format tanggal tidak valid.")
            return

    debit = int(input('Masukkan jumlah pemasukan: '))
    last_outcome = getLastOutcome(user)
    new_outcome = last_outcome + debit

    newTransaction = Trans.Transaction(date, debit, 0, new_outcome, "Uang Masuk")
    saveTransaction(newTransaction, user)

def recordCredit(user : User):
    """
    Mencatat pengeluaran (credit) yang diinputkan oleh pengguna.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    - Satria Permata Sejati - 231524026 - @WeirdoKitten
    """
    pilihTanggal = int(input
    ("""
        pilih tanggal :
        1. hari ini
        2. input manual
    """))

    if pilihTanggal == 1:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if pilihTanggal == 2:
        # Meminta pengguna memasukkan tanggal secara manual satu per satu
        year = input("Masukkan tahun (Format: YYYY): ")
        month = input("Masukkan bulan (Format: MM): ")
        day = input("Masukkan hari (Format: DD): ")

        # Mengambil jam, menit, dan detik dari waktu sekarang
        current_time = datetime.datetime.now()
        hour = current_time.strftime("%H")
        minute = current_time.strftime("%M")
        second = current_time.strftime("%S")

        # Mengonversi input tanggal menjadi objek datetime
        try:
            date = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
        except ValueError:
            print("Format tanggal tidak valid.")
            return
    credit = int(input('Masukkan jumlah pengeluaran: '))
    last_outcome = getLastOutcome(user)
    new_outcome = last_outcome - credit

    print("pilih kategori :")
    i = 1
    for kategori in Trans.Transaction.category:
        print(f"{i}. {kategori}")
        i += 1
    pilihKategori = int(input())

    for i in range(7):
        if pilihKategori == i:
            kategori = Trans.Transaction.category[i-1]
            break

    newTransaction = Trans.Transaction(date, 0, credit, new_outcome, kategori)
    saveTransaction(newTransaction, user)

def saveTransaction(transaction, user : User):
    """
    Menyimpan transaksi ke dalam file user.fileName.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    """
    with open(user.fileName, 'a') as file:
        file.write(f"{transaction.date} | {transaction.debit} | {transaction.credit} | {transaction.outcome} | {transaction.category}\n")
        file.close()
    print('Transaksi berhasil disimpan!')
    sortTransaction(user)

def showMonthlyRecap(user: User):
    """
    Menampilkan rekap transaksi bulanan.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    """
    year = int(input('Masukkan tahun (contoh: 2024): '))
    month = int(input('Masukkan bulan (contoh: 1 untuk Januari): '))
    totalDebit = 0
    totalCredit = 0
    with open(user.fileName,'r') as file:
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
    file.close()

def showDailyRecap(user: User):
    """
        Menampilkan rekap transaksi bulanan.

        Author
        ------
        - Farrel Zandra - 231524007 - @quack22
    """
    totalDebit = 0
    totalCredit = 0

    with open(user.fileName, 'r') as file:
        for line in file:
            data = line.split('|')
            transDateTime = data[0].strip() # mengambil elemen pertama dari array transDateTime.
            transDate = transDateTime.split()[0] # memisahkan tanggal dan waktu, kemudian mengambil tanggal saja.
            transYear, transMonth, transDay = transDate.split('-')
            if int(transYear) == year and int(transMonth) == month and int(transDay) == day:
                totalDebit += int(data[1].strip())
                totalCredit += int(data[2].strip())
    print(f"Rekap tanggal {day}/{month}/{year}")
    print('-----------------------------------')
    print(f"Total Pemasukan: {totalDebit}")
    print(f"Total Pengeluaran: {totalCredit}")
    file.close()

def showWeeklyRecap(year, month, user : User):
    """
        Menampilkan rekap transaksi mingguan dalam satu bulan.

        Author
        ------
        - Farrel Zandra - 231524007 - @quack22
        """
    countDay = calendar.monthrange(year, month)[1]
    startDate = dt(year, month, 1)
    endDate = dt(year, month, countDay)

    currentDate = startDate
    while currentDate <= endDate:
        nextWeek = currentDate + timedelta(days=(6-currentDate.weekday())) # penghitungan tanggal akhir minggu
        if nextWeek > endDate:
            nextWeek = endDate # tanggal akhir minggu tidak boleh melebihi tanggal akhir bulan.

        totalDebit = 0
        totalCredit = 0

        with open(user.fileName, 'r') as file:
            for line in file:
                data = line.split('|')
                transDate = datetime.strptime(data[0].strip(), "%Y-%m-%d %H:%M:%S")
                if currentDate <= transDate <= nextWeek:
                    debit = int(data[1].strip())
                    credit = int(data[2].strip())
                    totalDebit += debit
                    totalCredit += credit

        print(f"Rekap minggu {currentDate.strftime('%d %B %Y')} - {nextWeek.strftime('%d %B %Y')}:")
        print('----------------------------------')
        print(f"Total Pemasukan  : Rp{totalDebit}")
        print(f"Total Pengeluaran  : Rp{totalCredit}")
        print()
        file.close()

        currentDate = nextWeek + timedelta(days=1) # lompat ke minggu selanjutnya.

def readTransaction(user : User):
    """
    Membaca transaksi dari file dan mengembalikan daftar transaksi.

    Author
    ------
    Farras Ahmad Rasyid - 231524006 - @bamoebin
    
    Parameter:
        user : User: Nama file yang berisi data transaksi.
    """
    transactions = []
    try:
        with open(user.fileName, 'r') as file:
            for line in file:
                data = line.strip().split('|')
                trans_date = data[0].strip()
                debit = int(data[1].strip())
                credit = int(data[2].strip())
                outcome = int(data[3].strip())
                category = (data[4].strip())
                print(f"=========================\nTanggal : {trans_date}\nDebit : {debit}\nCredit : {credit}\nOutcome : {outcome}\n Category : {category}\n")
                
                # Membuat objek Transaction dari data yang dibaca
                newtransaction = Trans.Transaction(trans_date, debit, credit, outcome, category)
                transactions.append(newtransaction)
            file.close()
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan saat membaca file:", str(e))


def sortTransaction(user : User):
    """
    Mengurutkan data transaksi dalam file berdasarkan tanggal.

    Author
    ------
    Satria Permata Sejati - 231524026 - @WeirdoKitten

    """
    try:
        # Baca data transaksi menggunakan fungsi readTransaction
        transactions = readTransaction(user.fileName)

        # Urutkan data berdasarkan tanggal
        sorted_transactions = sorted(transactions, key=lambda x: x.date)

        # Simpan data yang telah diurutkan kembali ke file
        with open(user.fileName, 'w') as file:
            for transaction in sorted_transactions:
                line = f"{transaction.date} | {transaction.debit} | {transaction.credit} | {transaction.outcome} | {transaction.category}\n"
                file.write(line)
        print("Data berhasil diurutkan berdasarkan tanggal.")
        file.close()
    except Exception as e:
        print("Terjadi kesalahan saat mengurutkan data:", str(e))

def getLastOutcome(user : User):
    """
    Mendapatkan nilai outcome terakhir dari file transaksi.

    Author
    ------
    - Satria Permata Sejati - 231524026 - @WeirdoKitten
    """
    try:
        with open(user.fileName, 'r') as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                data = last_line.split('|')
                last_outcome = int(data[3].strip())  # Ambil nilai outcome terakhir dari baris terakhir
            else:
                last_outcome = 0  # Jika file kosong, maka outcome terakhir adalah 0
            file.close()
    except FileNotFoundError:
        print("File tidak ditemukan.")
        last_outcome = 0
    return last_outcome