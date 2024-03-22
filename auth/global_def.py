import auth.auth as auth


class User:
    name: str
    username: str
    password: str
    fileName: str

    def __init__(self, name: str, username: str, password: str, fileName: str):
        self.name = name
        self.username = username
        self.password = password
        self.fileName = fileName

    def register(self) -> bool:
        """
        Modul pendaftaran suatu akun

        Author
        -----
        - Thafa Fadillah Ramdani - 231524027 - @AllThaf

        Return
        -----
        Boolean yang menandakan keberhasilan registrasi
        """
        accFile = open("dataAkun.bin", "a")
        if accFile == None:
            print("File tidak dapat dibuka")
        print("==================REGISTER==================")
        name = input("Masukkan nama anda: ")
        username = input("Masukkan username anda: ")
        if auth.isRegisterValid(username):
            print("Username sudah terdaftar")
            print("Mohon masukkan username yang berbeda")

            return False
        else:
            password = input("Masukkan password anda: ")
            fileName = "data/" + username + ".txt"
            accFile.write(
                name + "#" + username + "#" + password + "#" + fileName + "#\n"
            )

        accFile.close()
        return True

    def login(self) -> bool:
        """
        Modul login suatu akun

        Author
        -----
        - Thafa Fadillah Ramdani - 231524027 - @AllThaf

        Return
        -----
        Boolean yang menandakan keberhasilan login
        """
        accFile = open("dataAkun.bin", "r")
        if accFile == None:
            print("File tidak dapat dibuka")
        print("==================LOGIN==================")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        log = False

        for account in accFile:
            account = account.split("#")
            if account[1] == username and account[2] == password:
                print("Login success!!")
                print(f"Welcome {account[0]}")
                log = True
                self.name = account[0]
                self.username = account[1]
                self.password = account[2]
                self.fileName = account[3]
                break

        if not log:
            print(
                "Username atau password salah\nMohon masukkan username / password yang benar"
            )

        accFile.close()
        return log
