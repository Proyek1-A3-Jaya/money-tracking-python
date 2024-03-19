import auth.global_def as AuthDef
import transaction.global_def as TransactionDef
import menu.menu as Menu
import auth.auth as Auth

if __name__ == '__main__':
    print("Tampil menu")
    # Testing showMainMenu()
    Menu.showMainMenu()
    """
    Apabila registrasi berhasil dilakukan, maka tampilkan home menu.
    Sementara menggunakan None sebagai username untuk pengetesan.
    """
    Menu.showHomeMenu(username=None)