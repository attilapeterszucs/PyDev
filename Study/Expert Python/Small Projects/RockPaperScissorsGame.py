import random

User = str(input("Choose one, (rock, paper, scissors): "))

chooses = ["rock", "paper", "scissors"]
cpu_player = random.choice(chooses)

if User in chooses:
    if User == cpu_player:
        print(f"User Choice: {User}\nCPU Choice: {cpu_player}\n")
        print("Tie!")
    elif User == "rock":
        if cpu_player == "paper":
            print(f"User Choice: {User}\nCPU Choice: {cpu_player}\n")
            print("You lose!")
        else:
            print(f"User Choice: {User}\nCPU Choice: {cpu_player}\n")
            print("You win!")
    elif User == "paper":
        if cpu_player == "rock":
            print(f"User Choice: {User}\nCPU Choice: {cpu_player}\n")
            print("You win!")
        else:
            print(f"User Choice: {User}\nCPU Choice: {cpu_player}\n")
            print("You lose!")
    elif User == "scissors":
        if cpu_player == "rock":
            print(f"User Choice: {User}\nCPU Choice: {cpu_player}\n")
            print("You lose!")
        else:
            print(f"User Choice: {User}\nCPU Choice: {cpu_player}\n")
            print("You win!")
else:
    print("Please select one of the three options above")
    exit()



