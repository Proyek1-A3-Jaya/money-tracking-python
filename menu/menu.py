import os
from auth import global_def
from auth.global_def import User
import transaction.global_def as tr
import time


def clearScreen():
    """
    Menghapus teks dari terminal

    Referensi
    ---------
    - https://stackoverflow.com/questions/2084508/clear-the-terminal-in-python

    Author
    ---------
    - Yobel El'Roy Doloksaribu - 231524029 - @k31p
    """
    os.system("cls" if os.name == "nt" else "clear")


def getChoice(message: str) -> (int, bool):
    """
    Mengambil opsi dari user, jika input bukan int maka akan menghasilkan pesan error

    Contoh pemakaian:
    print("Masukkan input: ")
    result, error = getChoice()

    Parameter
    ---------
    - message - Pesan yang akan ditampilkan

    Returns
    ---------
    - int  - Input yang user berikan
    - bool - False jika berhasil, True ketika input tidak valid

    Author
    ---------
    - Yobel El'Roy Doloksaribu - 231524029 - @k31p
    """

    choice = input(message)

    # Memeriksa apakah input adalah integer positif, dan bukan negatif atau selain integer
    if not choice.isnumeric():
        return 0, True

    return int(choice), False


def showInvalidInputMessage():
    """
    Menampilkan pesan jika input yang diterima oleh getChoice invalid

    Author
    ------
    - Yobel El'Roy Doloksaribu - 231524029 - @k31p
    """

    clearScreen()
    print("Pilihan tidak valid, coba lagi...")
    time.sleep(2)


def showMainMenu():
    """
    Menampilkan halaman awal ke layar.

    Author
    ------
    - Yobel El'Roy Doloksaribu - 231524029 - @k31p
    """
    print(" ______________________________________________________")
    print("|                                                      |")
    print("|      SELAMAT DATANG DI APLIKASI MONEY TRACKING       |")
    print("|              DIBUAT OLEH TEAM A3 PROYEK 1            |")
    print("|______________________________________________________|")
    print("|                                                      |")
    print("|                   1. Login                           |")
    print("|                   2. Registrasi                      |")
    print("|                   3. Keluar                          |")
    print("|                                                      |")
    print("|                                                      |")
    print("|______________________________________________________|")


def showHomeMenu():
    """
    Menampilkan menu setelah berhasil melakukan registrasi ataupun login.

    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    """
    print(" ______________________________________________________ ")
    print("|                                                      |")
    print("|           HALO! Ada yang bisa kami bantu?            |")
    print("|______________________________________________________|")
    print("|                                                      |")
    print("|                1. Lihat Rekap                        |")
    print("|                2. Lihat Riwayat Transaksi            |")
    print("|                3. Lihat Saldo & Mutasi Terakhir      |")
    print("|                4. Catat Keuangan                     |")
    print("|                5. Nabung Yuk!                        |")
    print("|                6. Log Out                            |")
    print("|                                                      |")
    print("|______________________________________________________|")


def showTransactionMenu():
    """


    Author
    ------
    - Farrel Zandra - 231524007 - @quack22
    """
    print(" ______________________________________________________ ")
    print("|                                                      |")
    print("|                   Jenis Transaksi                    |")
    print("|______________________________________________________|")
    print("|                                                      |")
    print("|              1. Catat Pemasukan (Debit)              |")
    print("|              2. Catat Pengeluaran (Credit)           |")
    print("|                                                      |")
    print("|______________________________________________________|")


def showRecapMenu():
    """
    Menampilkan menu setelah memilih opsi 'Lihat Rekap'.

    Author
    ------
    - Thafa Fadillah Ramdani - 231524027 - @AllThaf
    """
    print(" ______________________________________________________ ")
    print("|                                                      |")
    print("|             Pilih Rekap yang Diinginkan              |")
    print("|______________________________________________________|")
    print("|                                                      |")
    print("|              1. Rekap Harian                         |")
    print("|              2. Rekap Mingguan                       |")
    print("|              3. Rekap Bulanan                        |")
    print("|                                                      |")
    print("|______________________________________________________|")


def handleHomeMenu(user: User):
    """
    Men-handle home menu.

    Author
    ------
    - Thafa Fadillah Ramdani - 231524027 - @AllThaf
    - Yobel El'Roy Doloksaribu - 231524029 - @k31p
    """
    while True:
        clearScreen()
        showHomeMenu()
        option, retError = getChoice("Masukkan pilihan: ")

        if retError:
            showInvalidInputMessage()
            continue

        if option == 1:
            clearScreen()
            showRecapMenu()
            choice, err = getChoice("Pilih: ")
            if err:
                showInvalidInputMessage()
                continue

            if choice == 1:
                tr.showDailyRecap(user)
                input("Tekan enter untuk melanjutkan...")
            elif choice == 2:
                tr.showWeeklyRecap(user)
                input("Tekan enter untuk melanjutkan...")
            elif choice == 3:
                tr.showMonthlyRecap(user)
                input("Tekan enter untuk melanjutkan...")
            else:
                showInvalidInputMessage()
                continue
        elif option == 2:
            tr.printTransactions(user)
            input("Tekan enter untuk melanjutkan...")
        elif option == 3:
            tr.lastTransaction(user)
            input("Tekan enter untuk melanjutkan...")
        elif option == 4:
            clearScreen()
            showTransactionMenu()
            choice, err = getChoice("Pilih: ")
            if err:
                showInvalidInputMessage()
                continue

            if choice == 1:
                tr.recordDebit(user)
            elif choice == 2:
                tr.recordCredit(user)
            else:
                showInvalidInputMessage()
                continue
        elif option == 5:
            clearScreen()
            tr.createGoal()
            clearScreen()
        elif option == 6:
            break
        else:
            showInvalidInputMessage()
            continue
