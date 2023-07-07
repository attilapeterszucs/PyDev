import random

print("Welcome to [NGG] (Number Guessing Game)")
X = 0
Y = 30


def main():
    cpu = random.randint(X, Y)
    while True:
        usr = int(input(f"Guess the number between {X} and {Y}: "))
        if usr == cpu:
            print("You Guessed it!")
            exit()
        else:
            print("It's not it!")
            if usr > cpu:
                print("Lower")
            else:
                print("Higher")


main()

