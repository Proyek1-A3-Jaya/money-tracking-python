def isRegisterValid(username: str):
    """
    Pengecekan username yang sama saat register

    Author
    -----
    - Thafa Fadillah Ramdani - 231524027 - @AllThaf
    """

    accFile = open("dataAkun.bin", "r")
    if accFile == None:
        print("File tidak dapat dibuka")
        return False

    for login in accFile:
        login = login.split()
        if login[1] == username:
            return True
            break
    accFile.close()
    return False
