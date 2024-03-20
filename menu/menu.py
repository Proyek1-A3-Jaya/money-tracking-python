import os
from auth import global_def

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
    os.system('cls' if os.name == 'nt' else 'clear')

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
        - bool - True jika berhasil, False ketika input tidak valid

        Author
        ---------
        - Yobel El'Roy Doloksaribu - 231524029 - @k31p
    """

    choice = input(message)

    # Memeriksa apakah input adalah integer positif, dan bukan negatif atau selain integer
    if not choice.isnumeric():
        return 0, False 
    
    return int(choice), True


def showMainMenu():
    """
        Menampilkan halaman awal ke layar.
        
        Author
        ------
        - Yobel El'Roy Doloksaribu - 231524029 - @k31p
    """
    print(" ______________________________________________________");
    print("|                                                      |");
    print("|      SELAMAT DATANG DI APLIKASI MONEY TRACKING       |");
    print("|              DIBUAT OLEH TEAM A3 PROYEK 1            |");
    print("|______________________________________________________|");
    print("|                                                      |");
    print("|                   1. Login                           |");
    print("|                   2. Registrasi                      |");
    print("|                   3. Keluar                          |");
    print("|                                                      |");
    print("|                                                      |");
    print("|______________________________________________________|");

def showHomeMenu(username):
    """
        Menampilkan menu setelah berhasil melakukan registrasi ataupun login.

        Author
        ------
        - Farrel Zandra - 231524007 - @quack22
    """
    print(" ______________________________________________________ ");
    print("|                                                      |");
    print("|           HALO! Apa yang bisa kami bantu?            |");
    print("|______________________________________________________|");
    print("|                                                      |");
    print("|                1. Lihat Rekap                        |");
    print("|                2. Lihat Riwayat Transaksi            |");
    print("|                3. Lihat Saldo & Mutasi Terakhir      |");
    print("|                4. Catat Keuangan                     |");
    print("|                5. Log Out                            |");
    print("|                                                      |");
    print("|______________________________________________________|");

def showTransactionMenu():
    """
        Menampilkan menu setelah berhasil melakukan registrasi ataupun login.

        Author
        ------
        - Farrel Zandra - 231524007 - @quack22
    """
    print(" ______________________________________________________ ");
    print("|                                                      |");
    print("|                   Jenis Transaksi                    |");
    print("|______________________________________________________|");
    print("|                                                      |");
    print("|              1. Catat Pemasukan (Debit)              |");
    print("|              2. Catat Pengeluaran (Credit)           |");
    print("|                                                      |");
    print("|______________________________________________________|");