import random as r

guess = 1
number = r.randint(0, 20)

while True:
    num = input("Give me a guess: ")

    if int(num) > number:
        print("\nLower\n")
        guess += 1
    elif int(num) < number:
        print("\nHigher\n")
        guess += 1
    else:
        break

print(f"You guessed it in {guess} guesses!")
