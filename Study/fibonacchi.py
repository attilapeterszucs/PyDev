import math as m


def inputmodule():
    usr = int(input("Please select a number: "))
    if usr is not None:
        is_factorial = input("Exponential? (y/n): ")
        if is_factorial == "y":
            num = m.factorial(usr)
            main(num)
        elif is_factorial == "n":
            num = usr
            main(num)

    else:
        inputmodule()


def main(i):
    x = 0
    y = 1
    while x < i:
        z = x + y
        x = y
        y = z

        print("\n", x)


inputmodule()


