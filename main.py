# Create the 1/11/2021 by Benjamin Descours
class Pc:
    syt = "PyOS"


_1_ = Pc()
_1_.syt = 'Py_OS 0.01 alpha not graphic'


def sytem():
    _3_ = 5
    print("\nWelcome to Py_OS\n")
    login = input("login: ")
    exit_1 = "exit"
    calculator_1 = "calculator"
    password = input("password: ")
    password_1 = "0000"
    login_1 = "Descours"
    os_1 = "version"
    help_1 = "help"
    if password_1 == password and login == login_1:
        while _3_ == 5:
            co_1 = input("pc-of-Descours-Benjamin:~$ ")
            if co_1 == calculator_1:
                import clacutor
                clacutor
            elif co_1 == exit_1:
                exit()
            elif co_1 == os_1:
                print(_1_.syt)
            elif co_1 == help_1:
                print("\n calculator \n exit \n os \n")
    elif password != password_1 and login != login_1:
        print("\nIncorrect login or password \n")
        return sytem()


sytem()
