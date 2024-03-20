import auth.auth as auth


class User:
    name: str
    username: str
    password: str
    fileName: str

    def __innit__(self, name: str, username: str, password: str, fileName: str):
        self.name = name
        self.username = username
        self.password = password
        self.fileName = fileName

    def register():
        """
        Modul pendaftaran suatu akun

        Author
        -----
        - Thafa Fadillah Ramdani - 231524027 - @AllThaf
        """
        accFile = open("dataAkun.bin", "a")
        if accFile == None:
            print("File tidak dapat dibuka")
        print("==================REGISTER==================")
        name = input("Masukkan nama anda: ")
        username = input("Masukkan username anda: ")
        if auth.registerValid(username):
            print("Username sudah terdaftar")
            print("Mohon masukkan username yang berbeda")
        else:
            password = input("Masukkan password anda: ")
            fileName = username + ".txt"
            accFile.write(name + " ")
            accFile.write(username + " ")
            accFile.write(password + " ")
            accFile.write(fileName)

        accFile.close()

    def login():
        """
        Modul login suatu akun

        Author
        -----
        - Thafa Fadillah Ramdani - 231524027 - @AllThaf
        """
        accFile = open("dataAkun.bin", "r")
        if accFile == None:
            print("File tidak dapat dibuka")
        print("==================LOGIN==================")
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        log = False

        for account in accFile:
            account = account.split()
            if account[1] == username and account[2] == password:
                print("Login succes!!")
                print(f"Welcome {account[0]}")
                log = True
                break

        if not log:
            print(
                "Username atau password salah\nMohon masukkan username / password yang benar"
            )
        accFile.close()
        return account
