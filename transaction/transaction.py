from datetime import datetime, timedelta
import transaction.global_def as Trans
import calendar
from datetime import datetime as dt
from auth.global_def import User
from menu import menu as Mn
import os
import time


def recordDebit(user: User):
    """
    Mencatat pemasukan (debit) yang diinputkan oleh pengguna.

    Author
    -----
    - Farrel Zandra - 231524007 - @quack22
    - Satria Permata Sejati - 231524026 - @WeirdoKitten
    """
    # Input data transaksi berupa tanggal, debit, credit, dan outcome
    print("==== Tanggal Transaksi ====")
    print("1. Hari Ini")
    print("2. Input Manual")
    pilihTanggal = int(input("pilih tanggal :"))

    if pilihTanggal == 1:
        date = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    if pilihTanggal == 2:
        # Meminta pengguna memasukkan tanggal secara manual satu per satu
        year = input("Masukkan tahun (Format: YYYY): ")
        month = input("Masukkan bulan (Format: MM): ")
        day = input("Masukkan hari (Format: DD): ")

        # Mengambil jam, menit, dan detik dari waktu sekarang
        current_time = datetime.now()
        hour = current_time.strftime("%H")
        minute = current_time.strftime("%M")
        second = current_time.strftime("%S")

        # Mengonversi input tanggal menjadi objek datetime
        try:
            date = dt(
                int(year), int(month), int(day), int(hour), int(minute), int(second)
            )
        except ValueError:
            print("Format tanggal tidak valid.")
            return

    debit = int(input("Masukkan jumlah pemasukan: "))
    last_outcome = getLastOutcome(user)
    new_outcome = last_outcome + debit

    newTransaction = Trans.Transaction(date, debit, 0, new_outcome, "Uang Masuk")
    saveTransaction(newTransaction, user)


def recordCredit(user: User):
    """
    Mencatat pengeluaran (credit) yang diinputkan oleh pengguna.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    - Satria Permata Sejati - 231524026 - @WeirdoKitten
    """
    print("==== Tanggal Transaksi ====")
    print("1. Hari Ini")
    print("2. Input Manual")
    pilihTanggal = int(input("pilih tanggal :"))

    if pilihTanggal == 1:
        date = dt.now().strftime("%Y-%m-%d %H:%M:%S")
    if pilihTanggal == 2:
        # Meminta pengguna memasukkan tanggal secara manual satu per satu
        year = input("Masukkan tahun (Format: YYYY): ")
        month = input("Masukkan bulan (Format: MM): ")
        day = input("Masukkan hari (Format: DD): ")

        # Mengambil jam, menit, dan detik dari waktu sekarang
        current_time = datetime.now()
        hour = current_time.strftime("%H")
        minute = current_time.strftime("%M")
        second = current_time.strftime("%S")

        # Mengonversi input tanggal menjadi objek datetime
        try:
            date = dt(
                int(year), int(month), int(day), int(hour), int(minute), int(second)
            )
        except ValueError:
            print("Format tanggal tidak valid.")
            return
    credit = int(input("Masukkan jumlah pengeluaran: "))
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
            kategori = Trans.Transaction.category[i - 1]
            break

    newTransaction = Trans.Transaction(date, 0, credit, new_outcome, kategori)
    saveTransaction(newTransaction, user)


def saveTransaction(transaction, user: User):
    """
    Menyimpan transaksi ke dalam file user.fileName.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    """
    with open(user.fileName, "a") as file:
        file.write(
            f"{transaction.date} | {transaction.debit} | {transaction.credit} | {transaction.outcome} | {transaction.category}\n"
        )
        file.close()
    print("Transaksi berhasil disimpan!")
    sortTransaction(user)


def showMonthlyRecap(user: User):
    """
    Menampilkan rekap transaksi bulanan.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    - (Update) Thafa Fadillah Ramdani - 231524027 - @AllThaf
    """
    year = int(input("Masukkan tahun (contoh: 2024): "))
    month = int(input("Masukkan bulan (contoh: 1 untuk Januari): "))
    totalDebit = 0
    totalCredit = 0
    totalMakananMinuman = 0
    totalPendidikan = 0
    totalKesehatan = 0
    totalBelanja = 0
    totalTransportasi = 0
    totalLainnya = 0
    with open(user.fileName, "r") as file:
        for line in file:
            data = line.split("|")
            transDate = data[0].strip()
            transYear, transMonth, _ = transDate.split("-")
            if int(transYear) == year and int(transMonth) == month:
                totalDebit += int(data[1].strip())
                totalCredit += int(data[2].strip())
                if data[4].strip() == Trans.Transaction.category[0]:
                    totalMakananMinuman += int(data[2].strip())
                elif data[4].strip() == Trans.Transaction.category[1]:
                    totalPendidikan += int(data[2].strip())
                elif data[4].strip() == Trans.Transaction.category[2]:
                    totalKesehatan += int(data[2].strip())
                elif data[4].strip() == Trans.Transaction.category[3]:
                    totalBelanja += int(data[2].strip())
                elif data[4].strip() == Trans.Transaction.category[4]:
                    totalTransportasi += int(data[2].strip())
                else:
                    totalLainnya += int(data[2].strip())
    print(f"Rekap Bulan {month}/{year}:")
    print("----------------------------")
    print(f"Total Pemasukan: Rp{totalDebit:,}")
    print(f"Total Pengeluaran Keseluruhan: Rp{totalCredit:,}")
    print("Pengeluaran perkategori")
    print(f"1. Makanan/Minuman: Rp{totalMakananMinuman:,}")
    print(f"2. Pendidikan: Rp{totalPendidikan:,}")
    print(f"3. Kesehatan: Rp{totalKesehatan:,}")
    print(f"4. Belanja: Rp{totalBelanja:,}")
    print(f"5. Transportasi: Rp{totalTransportasi:,}")
    print(f"6. Lainnya: Rp{totalLainnya:,}")
    file.close()


def showDailyRecap(user: User):
    """
    Menampilkan rekap transaksi harian.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    - (Update) Thafa Fadillah Ramdani - 231524027 - @AllThaf
    """
    year = int(input("Masukkan tahun (contoh: 2024): "))
    month = int(input("Masukkan bulan (contoh: 1 untuk Januari): "))
    day = int(input("Masukkan tanggal: "))
    totalDebit = 0
    totalCredit = 0
    totalMakananMinuman = 0
    totalPendidikan = 0
    totalKesehatan = 0
    totalBelanja = 0
    totalTransportasi = 0
    totalLainnya = 0

    with open(user.fileName, "r") as file:
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
                if data[4].strip() == Trans.Transaction.category[0]:
                    totalMakananMinuman += int(data[2].strip())
                elif data[4].strip() == Trans.Transaction.category[1]:
                    totalPendidikan += int(data[2].strip())
                elif data[4].strip() == Trans.Transaction.category[2]:
                    totalKesehatan += int(data[2].strip())
                elif data[4].strip() == Trans.Transaction.category[3]:
                    totalBelanja += int(data[2].strip())
                elif data[4].strip() == Trans.Transaction.category[4]:
                    totalTransportasi += int(data[2].strip())
                else:
                    totalLainnya += int(data[2].strip())
    print(f"Rekap tanggal {day}/{month}/{year}")
    print("-----------------------------------")
    print(f"Total Pemasukan: Rp{totalDebit:,}")
    print(f"Total Pengeluaran Keseluruhan: Rp{totalCredit:,}")
    print("Pengeluaran perkategori")
    print(f"1. Makanan/Minuman: Rp{totalMakananMinuman:,}")
    print(f"2. Pendidikan: Rp{totalPendidikan:,}")
    print(f"3. Kesehatan: Rp{totalKesehatan:,}")
    print(f"4. Belanja: Rp{totalBelanja:,}")
    print(f"5. Transportasi: Rp{totalTransportasi:,}")
    print(f"6. Lainnya: Rp{totalLainnya:,}")
    file.close()


def showWeeklyRecap(user: User):
    """
    Menampilkan rekap transaksi mingguan dalam satu bulan.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    - (Update) Thafa Fadillah Ramdani - 231524027 - @AllThaf
    """

    year = int(input("Masukkan tahun (contoh: 2024): "))
    month = int(input("Masukkan bulan (contoh: 1 untuk Januari): "))
    countDay = calendar.monthrange(year, month)[1]
    startDate = dt(year, month, 1)
    endDate = dt(year, month, countDay)

    currentDate = startDate
    while currentDate <= endDate:
        nextWeek = currentDate + timedelta(
            days=(6 - currentDate.weekday())
        )  # penghitungan tanggal akhir minggu
        if nextWeek > endDate:
            nextWeek = endDate  # tanggal akhir minggu tidak boleh melebihi tanggal akhir bulan.

        nextWeek += timedelta(days=1)

        totalDebit = 0
        totalCredit = 0
        totalMakananMinuman = 0
        totalPendidikan = 0
        totalKesehatan = 0
        totalBelanja = 0
        totalTransportasi = 0
        totalLainnya = 0

        with open(user.fileName, "r") as file:
            for line in file:
                data = line.split("|")
                transDate = datetime.strptime(data[0].strip(), "%Y-%m-%d %H:%M:%S")
                if currentDate <= transDate <= nextWeek:
                    debit = int(data[1].strip())
                    credit = int(data[2].strip())
                    totalDebit += debit
                    totalCredit += credit
                    if data[4].strip() != "Uang Masuk":
                        if data[4].strip() == Trans.Transaction.category[0]:
                            totalMakananMinuman += int(data[2].strip())
                        elif data[4].strip() == Trans.Transaction.category[1]:
                            totalPendidikan += int(data[2].strip())
                        elif data[4].strip() == Trans.Transaction.category[2]:
                            totalKesehatan += int(data[2].strip())
                        elif data[4].strip() == Trans.Transaction.category[3]:
                            totalBelanja += int(data[2].strip())
                        elif data[4].strip() == Trans.Transaction.category[4]:
                            totalTransportasi += int(data[2].strip())
                        else:
                            totalLainnya += int(data[2].strip())
        print(
            f"Rekap minggu {currentDate.strftime('%d %B %Y')} - {nextWeek.strftime('%d %B %Y')}:"
        )
        print("----------------------------------")
        print(f"Total Pemasukan: Rp{totalDebit:,}")
        print(f"Total Pengeluaran: Rp{totalCredit:,}")
        print("Pengeluaran perkategori")
        print(f"1. Makanan/Minuman: Rp{totalMakananMinuman:,}")
        print(f"2. Pendidikan: Rp{totalPendidikan:,}")
        print(f"3. Kesehatan: Rp{totalKesehatan:,}")
        print(f"4. Belanja: Rp{totalBelanja:,}")
        print(f"5. Transportasi: Rp{totalTransportasi:,}")
        print(f"6. Lainnya: Rp{totalLainnya:,}\n")

        currentDate = nextWeek  # lompat ke minggu selanjutnya.
    file.close()


def readTransaction(user: User) -> Trans:
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
        with open(user.fileName, "r") as file:
            for line in file:
                data = line.strip().split("|")
                trans_date = data[0].strip()
                debit = int(data[1].strip())
                credit = int(data[2].strip())
                outcome = int(data[3].strip())
                category = data[4].strip()

                # Membuat objek Transaction dari data yang dibaca
                newtransaction = Trans.Transaction(
                    trans_date, debit, credit, outcome, category
                )
                transactions.append(newtransaction)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan saat membaca file:", str(e))

    file.close()
    return transactions


def sortTransaction(user: User):
    """
    Mengurutkan data transaksi dalam file berdasarkan tanggal.

    Author
    ------
    Satria Permata Sejati - 231524026 - @WeirdoKitten

    """
    try:
        # Baca data transaksi menggunakan fungsi readTransaction
        transactions = readTransaction(user)

        # Urutkan data berdasarkan tanggal
        sorted_transactions = sorted(transactions, key=lambda x: x.date)

        # Simpan data yang telah diurutkan kembali ke file
        with open(user.fileName, "w") as file:
            for transaction in sorted_transactions:
                line = f"{transaction.date} | {transaction.debit} | {transaction.credit} | {transaction.outcome} | {transaction.category}\n"
                file.write(line)
        print("Data berhasil diurutkan berdasarkan tanggal.")
        input("Tekan enter untuk melanjutkan...")
        file.close()
    except Exception as e:
        print("Terjadi kesalahan saat mengurutkan data:", str(e))
        input("Tekan enter untuk melanjutkan...")


def getLastOutcome(user: User) -> int:
    """
    Mendapatkan nilai outcome terakhir dari file transaksi.

    Author
    ------
    - Satria Permata Sejati - 231524026 - @WeirdoKitten
    """
    try:
        with open(user.fileName, "r") as file:
            lines = file.readlines()
            if lines:
                last_line = lines[-1].strip()
                data = last_line.split("|")
                last_outcome = int(
                    data[3].strip()
                )  # Ambil nilai outcome terakhir dari baris terakhir
            else:
                last_outcome = 0  # Jika file kosong, maka outcome terakhir adalah 0
            file.close()
    except FileNotFoundError:
        print("File tidak ditemukan.")
        last_outcome = 0
    return last_outcome


def printTransactions(user: User):
    """
    Mencetak informasi transaksi untuk user.

    Author
    ------
    Farras Ahmad Rasyid - 231524006 - @bamoebin

    Parameter:
        user : User: Pengguna
    """
    transactions = readTransaction(user)
    if transactions:
        print(f"Transaksi untuk pengguna {user.name}:")
        for transaction in transactions:
            print("=========================")
            print(f"Tanggal\t: {transaction.date}")
            print(f"Debit\t: {transaction.debit}")
            print(f"Credit\t: {transaction.credit}")
            print(f"Outcome\t: {transaction.outcome}")
            print(f"Category\t: {transaction.category}")
            print()
    else:
        print("Tidak ada transaksi untuk pengguna", user.name)


def lastTransaction(user: User):
    """
    Mencetak informasi terakhir yang dilakukan user.

    Author
    ------
    Farras Ahmad Rasyid - 231524006 - @bamoebin

    Parameter:
        user : User: Pengguna
    """
    try:
        with open(user.fileName, "r") as file:
            lines = file.readlines()
            last_line = lines[-1].strip()
            data = last_line.split("|")
            trans_date = data[0].strip()
            debit = int(data[1].strip())
            credit = int(data[2].strip())
            outcome = int(data[3].strip())
            category = data[4].strip()
            print(
                f"=========================\nTanggal : {trans_date}\nDebit : {debit}\nCredit : {credit}\nCategory : {category}\nRemains : {outcome}\n"
            )
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print("Terjadi kesalahan saat membaca file:", str(e))


def calculateNominal(total: int, targetDate: str, frequency: str):
    """
    Menghitung nominal yang harus ditabung oleh pengguna per frekuensi waktunya.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22

    Parameter
    ---------
    :param total
    :param targetDate
    :param frequency
    """
    currentDate = dt.now()
    if targetDate:
        targetDate = dt.strptime(targetDate, "%Y-%m-%d")
        if targetDate < currentDate:
            print(
                "Tanggal target tidak boleh kurang dari tanggal hari ini! Ulangi input..."
            )
            print()
            return createGoal()
    else:
        targetDate = currentDate + timedelta(days=365)

    if frequency.lower() == "tahun":
        nominal = total / (targetDate.year - currentDate.year)
    elif frequency.lower() == "bulan":
        monthsDiff = (targetDate.year - currentDate.year) * 12 + (
            targetDate.month - currentDate.month
        )
        nominal = total - monthsDiff
    elif frequency.lower() == "minggu":
        weeksDiff = (targetDate - currentDate).days // 7
        nominal = total / weeksDiff
    elif frequency.lower() == "hari":
        daysDiff = (targetDate - currentDate).days
        nominal = total / daysDiff
    else:
        print("Frekuensi yang dimasukkan tidak valid!")
        return

    print(f"\nNominal yang harus ditabung per {frequency}: Rp{nominal}")
    print()


def calculateTargetDate(total: int, frequency: str, nominal: int):
    """
    Menghitung tanggal yang memungkinkan sebagai target apabila pengguna memilih rentang waktu fleksibel.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22

    Parameter
    ---------
    :param total
    :param frequency
    :param nominal
    """
    currentDate = dt.now()
    if frequency.lower() == "tahun":
        targetDate = currentDate + timedelta(days=365 * (total / nominal))
    elif frequency.lower() == "bulan":
        targetDate = currentDate + timedelta(days=30 * (total / nominal))
    elif frequency.lower() == "minggu":
        targetDate = currentDate + timedelta(days=7 * (total / nominal))
    elif frequency.lower() == "hari":
        targetDate = currentDate + timedelta(days=(total / nominal))
    else:
        print("Frekuensi tidak valid!")
        return

    print(
        f"\nDengan Rp{nominal} per {frequency.lower()}, target anda akan tercapai pada {targetDate.strftime('%d %B %Y')}"
    )


def isValidDate(date_str: str) -> bool:
    """
    Memeriksa apakah tanggal yang diinputkan user bernilai valid sesuai dengan format.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22

    Parameter
    ---------
    :param date_str
    """
    try:
        dt.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def createGoal():
    """
    Menampilkan halaman untuk membuat tujuan dan target menabung.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22

    no param
    """
    print("\n=== Buat Tujuan Keuanganmu ===")
    goal = input("| Halo, apa tujuan keuanganmu? | \nBeri tahu kami: ")
    total = int(input("| Berapa total uang yang ingin kamu tabung |\nInput: (Rp) "))

    print("\n=== Pilih Target Keuanganmu ===")
    print("| 1. Custom tanggal |")
    print("| 2. Fleksibel      |")
    choice = input("Pilih opsi (1/2): ")

    if choice == "1":
        targetDate = input("Masukkan tanggal (YYYY-MM-DD): ")
        if isValidDate(targetDate):
            frequency = input("Frekuensi tabungan (Tahun/Bulan/Minggu/Hari): ")
            calculateNominal(total, targetDate, frequency)
        else:
            print("Format tanggal tidak valid! Ulangi input...")
            print()

        input("Ketik 1 untuk kembali ke halaman utama: ")
    elif choice == "2":
        frequency = input("Frekuensi tabungan (Tahun/Bulan/Minggu/Hari): ")
        nominal = int(input("Nominal (Rp): "))
        calculateTargetDate(total, frequency, nominal)

        input("Ketik 1 untuk kembali ke halaman utama: ")
