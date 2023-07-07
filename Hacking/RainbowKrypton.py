import os
from time import sleep
import platform

sysOS = platform.system()
fpath = "/usr/share/rainbowcrack/"

logo = """ 
     _   __                 _                _   _       _     
    | | / /                | |              | | | |     | |    
    | |/ / _ __ _   _ _ __ | |_ ___  _ __   | |_| |_   _| |__  
    |    \| '__| | | | '_ \| __/ _ \| '_ \  |  _  | | | | '_ \ 
    | |\  \ |  | |_| | |_) | || (_) | | | | | | | | |_| | |_) |
    \_| \_/_|   \__, | .__/ \__\___/|_| |_| \_| |_/\__,_|_.__/ 
                 __/ | |                                       
                |___/|_|                                       

                    <-- RainbowTables -->
         <-- This Script is useing rainbowcrack -->

"""

def main():
    clear_screen()
    print(logo)
    print("-------------------------------------------")
    print("| Show IP address (0)")
    print("| Show Wireless Network Devices (1)")
    print("-------------------------------------------")
    print("| List Rainbow Tables (2)")
    print("| Generate Rainbow Table (3)")
    print("| Crack Hash With rainbowcrack (4)")
    print("-------------------------------------------")
    print("| Exit (99)")
    print("-------------------------------------------")
    inputs()

def clear_screen():
    if sysOS == "Linux":
        os.system("clear")
    if sysOS == "Windows":
        os.system("cls")

def inputs():

    cmd = input("\nCommand: ")

    if cmd is not "":
        if cmd == "0":
            clear_screen()
            os.system("ifconfig")
            input("\n\nPress ENTER to continue:")
            main()
        if cmd == "1":
            clear_screen()
            os.system("iwconfig")
            input("\n\nPress ENTER to continue:")
            main()
        if cmd == "2":
            listtables()
        if cmd == "3":
            gentable()
        if cmd == "4":
            crackhash()
        if cmd == "99":
            print("\nExiting...")
            sleep(2)
            exit
    else:
        print("\n[!] Wrong Command..")
        sleep(1)
        main()

def diagnostic():
    clear_screen()
    print(logo)

    print("Detecting System...")
    sleep(1)

    if sysOS == "Linux":
        update()
    else:
        print("\nYou have to run this program on Linux, you currently trying to run it on: ", sysOS)
        print("\nExiting...")
        sleep(1)
        exit

def update():
    clear_screen()
    print(logo)

    print("Updateing...\n")
    os.system("sudo apt-get update && sudo apt-get upgrade -y")
    print("\nSystem up to date!")
    sleep(1)
    checkdep()

def checkdep():
    if not os.path.exists(fpath):
        clear_screen()
        print(logo)
        print("Installing depedencies...")
        os.system("sudo apt-get install rainbowcrack")
        print("All depedencies installed!")
        sleep(1)
        main()
    else:
        main()

def listtables():
    clear_screen()
    print(logo)
    
    print("Listing Rainbow Tables!\n")
    os.system("rtsort .")
    input("Press ENTER to go back!")
    main()

def gentable():
    clear_screen()
    print(logo)

    print("Hash algorithms implemented:")
    print("--------------------------------------------------")
    print("| (lm) - HashLen = 8; PlaintextLen = 0-7")
    print("| (ntlm) - HashLen = 16; PlaintextLen = 0-15")
    print("| (md5) - HashLen = 16; PlaintextLen = 0-15")
    print("| (sha1) - HashLen = 20; PlaintextLen = 0-20")
    print("| (sha256) - HashLen = 32; PlaintextLen = 0-20")
    print("--------------------------------------------------")
    print("\nCharsets:")
    print("--------------------------------------------------------------------------------------------")
    print("| numeric            = [0123456789]")
    print("| loweralpha         = [abcdefghijklmnopqrstuvwxyz]")
    print("| loweralpha-numeric = [abcdefghijklmnopqrstuvwxyz0123456789]")
    print("| mixalpha-numeric   = [abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789]")
    print("| ascii-32-95        = [mixalpha-numeric + all the symbols]")
    print("--------------------------------------------------------------------------------------------\n")

    hash_algorithm = input("Hash algorithm: ")
    charset = input("Charset: ")
    plaintext_len_min = input("Plain Text Lenght (Minimum): ")
    plaintext_len_max = input("Plain Text Lenght (Maximum): ")
    table_index = input("Table Index: ")
    chain_len = input("Chain Lenght: ")
    chain_num = input("Chain Number: ")
    part_index = input("Part Index: ")
    
    sleep(1)
    clear_screen()
    print(logo)
    print("--------------------------------------------------------")
    print("| Choosen algorithm: ", hash_algorithm)
    print("| Choosen charset: ", charset)
    print("| Choosen plaintext min - max: " + plaintext_len_min + " - " + plaintext_len_max)
    print("| Choosen table index: ", table_index)
    print("| Choosen chain lenght: ", chain_len)
    print("| Choosen chain number: ", chain_num)
    print("| Choosen part index: ", part_index)
    print("--------------------------------------------------------\n")

    command = input("You sure you want to generate the rainbow table with this parameters? (y/n): ")
    if command is not "":
        if command == "y":
            clear_screen()
            print(logo)
            print("Generating Raimbow Table!")
            sleep(1)
            print("---------------------------------------------------------------------------------")
            os.system("rtgen {} {} {} {} {} {} {} {}".format(hash_algorithm, charset, plaintext_len_min, plaintext_len_max, table_index, chain_len, chain_num, part_index))
            print("---------------------------------------------------------------------------------")
            input("\nPress ENTER to go back!")
            main()
        if command == "n":
            main()

def crackhash():
    clear_screen()
    print(logo)

    print("Hash Cracker")
    print("--------------------------------------------------")
    print("| (h) - Load single hash")
    print("| (l) - Load hashes from a file")
    print("--------------------------------------------------\n")
    crackmethod = input("Choose method: ")
    if crackmethod is not "":
        if crackmethod == "h":
            singlehash = input("Single hash: ")
            crackingWS(singlehash)
        if crackmethod == "l":
            hashfromfile = input("Path: ")
            crackingWM(hashfromfile)

def crackingWS(single):
    clear_screen()
    print(logo)

    print("Cracking started!\n")
    print("---------------------------------------------------------------------------------")
    os.system("rcrack . -h {}".format(single))
    print("---------------------------------------------------------------------------------")
    input("\nPress ENTER to go back!")
    main()

def crackingWM(multi):
    clear_screen()
    print(logo)

    print("Cracking started!\n")
    print("---------------------------------------------------------------------------------")
    os.system("rcrack . -l {}".format(multi))
    print("---------------------------------------------------------------------------------")
    input("\nPress ENTER to go back!")
    main()


diagnostic()