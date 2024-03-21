import auth.global_def as Auth
import transaction.transaction as Tr
import menu.menu as Menu
import time

if __name__ == "__main__":
    user = Auth.User("", "", "", "")

    while True:
        Menu.clearScreen()
        Menu.showMainMenu()
        option, retError = Menu.getChoice("Masukkan pilihan: ")

        if retError:
            Menu.clearScreen()
            print("Pilihan tidak valid, coba lagi...")
            time.sleep(2)
            continue

        if option == 1:
            # Handle login
            Menu.clearScreen()
            success = user.login()
            while not success:
                time.sleep(2)
                Menu.clearScreen()
                success = user.login()

            time.sleep(3)
            Menu.clearScreen()
            Menu.handleHomeMenu(user)
            break
        elif option == 2:
            # Handle registrasi
            Menu.clearScreen()
            success = user.register()
            while not success:
                print("Registrasi gagal, coba lagi...")
                time.sleep(2)
                Menu.clearScreen()
                success = user.register()
            break
        elif option == 3:
            print("Selamat tinggal...")
            break
        else:
            print("Pilihan tidak ada, coba lagi...")
            time.sleep(2)
