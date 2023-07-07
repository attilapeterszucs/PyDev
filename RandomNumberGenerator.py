import random
from time import sleep
import os

logo = """ 
     _   __                 _                _   _       _     
    | | / /                | |              | | | |     | |    
    | |/ / _ __ _   _ _ __ | |_ ___  _ __   | |_| |_   _| |__  
    |    \| '__| | | | '_ \| __/ _ \| '_ \  |  _  | | | | '_ \ 
    | |\  \ |  | |_| | |_) | || (_) | | | | | | | | |_| | |_) |
    \_| \_/_|   \__, | .__/ \__\___/|_| |_| \_| |_/\__,_|_.__/ 
                 __/ | |                                       
                |___/|_|                                       

                 <-- Random Number Generator -->
"""

def main():
    os.system("clear")
    szam = random.randint(0, 100000)
    print(logo)
    generate = input("Press ENTER to Generate a number! or (exit): ")
    if generate != "exit":
        os.system("clear")
        print(logo)
        print("\n   The Number is: ",szam)
        gen_new = input("\nPress ENTER to Generate a new number! or (exit): ")
        if gen_new != "exit":
            os.system("clear")
            main()
        elif gen_new == "exit":
            exit
        else:
            os.system("clear")
            print(logo)
            print("\nSomething went wrong!")
            sleep(1)
            main()
    elif generate == "exit":
        exit
    else:
        os.system("clear")
        print(logo)
        print("\nSomething went wrong!")
        sleep(1)
        main()


main()