import auth.global_def as AuthDef
import transaction.transaction as Tr
import menu.menu as Menu
import auth.auth as Auth

if __name__ == '__main__':
    print("Tampil menu")
    # Testing showMainMenu()
    Menu.showMainMenu()

    # Apabila registrasi berhasil dilakukan, maka tampilkan home menu.
    # Sementara menggunakan None sebagai username untuk pengetesan.
    Menu.showHomeMenu()

    # Testing input dan simpan transaksi.
    # Udah dulu mas, pen turu.
    Tr.recordDebit()

    # Testing rekap bulanan
    # Tr.showMonthlyRecap(year=None, month=None)

    # Testing rekap harian
    # Bug fixed.
    Tr.showDailyRecap(year=None, month=None, day=None)

    # Testing rekap mingguan
    # bug, output 0.
    Tr.showWeeklyRecap(2024, 3)