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
        accFile = open("dataAkun.bin", "a")
        if accFile == None:
            print("File tidak dapat dibuka")
        print("==================REGISTER==================")
        name = input("Masukkan nama anda: ")
        username = input("Masukkan username anda: ")
        password = input("Masukkan password anda: ")
        fileName = username + ".txt"

        accFile.write(name + " ")
        accFile.write(username + " ")
        accFile.write(password + " ")
        accFile.write(fileName + " ")
