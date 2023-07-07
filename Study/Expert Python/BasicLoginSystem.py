import getpass as gp
from time import sleep


def input_user():
    user_n = input("Username: ")
    if user_n is not None:
        user_p = gp.getpass(prompt="Password: ", stream=None)
        if user_p is not None:
            main(user_n, user_p)
        else:
            input_user()
    else:
        login_error()


def main(username, password):
    if (username == "krypton") & (password == "password"):
        print('Login Successful!')
    else:
        login_error()


def login_error():
    print("Error! Someting went wrong!")
    sleep(3)
    input_user()


input_user()
