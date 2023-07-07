import os
from time import sleep
import platform

sysOS = platform.system()

logo = """ 
     _   __                 _                _   _       _     
    | | / /                | |              | | | |     | |    
    | |/ / _ __ _   _ _ __ | |_ ___  _ __   | |_| |_   _| |__  
    |    \| '__| | | | '_ \| __/ _ \| '_ \  |  _  | | | | '_ \ 
    | |\  \ |  | |_| | |_) | || (_) | | | | | | | | |_| | |_) |
    \_| \_/_|   \__, | .__/ \__\___/|_| |_| \_| |_/\__,_|_.__/ 
                 __/ | |                                       
                |___/|_|                                       

                        <-- Mac Changer -->

"""


def main():
    clear_screen()
    print(logo)
    print("-------------------------------------------")
    print("| Show IP address (0)                     |")
    print("| Show Wireless Network Devices (1)       |")
    print("| Change Mac Adress (2)                   |")
    print("-------------------------------------------")
    print("| Exit (99)                               |")
    print("-------------------------------------------")
    inputs()

def clear_screen():
    if sysOS == "Linux":
        os.system("clear")
    if sysOS == "Windows":
        os.system("cls")


def diagnostic():
    clear_screen()
    print(logo)
    print("Detecting System...")
    sleep(1)
    if sysOS == "Linux":
        main()
    else:
        print("\nYou have to run this program on Linux, you currently trying to run it on: ", sysOS)
        print("\nExiting...")
        sleep(1)
        exit


def inputs():

    cmd = input("\nCommand: ")

    if cmd != "":
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
            macchanger()
        if cmd == "99":
            print("\nExiting...")
            sleep(2)
            exit
    else:
        print("\n[!] Wrong Command..")
        sleep(1)
        main()


def macchanger():
    clear_screen()
    print(logo)
    print("-------------------------------------------")
    print("| Manual Mac (0)                          |")
    print("| Random Mac (1)                          |")
    print("-------------------------------------------")
    print("| Back (99)                               |")
    print("-------------------------------------------")
    macinputs()


def macinputs():

    Mcmd = input("\nCommand: ")
    
    if Mcmd != "":
        if Mcmd == "0":
            NetworkAdapterChooseManual()
        if Mcmd == "1":
            NetworkAdapterChooseRandom()
        if Mcmd == "99":
            main()
    else:
        print("\n[!] Wrong Command..")
        sleep(1)
        macchanger()


def wlan0down():
    clear_screen()
    print(logo)
    os.system("sudo ifconfig wlan0 down")


def eth0down():
    clear_screen()
    print(logo)
    os.system("sudo ifconfig eth0 down")


def wlan0up():
    os.system("sudo ifconfig wlan0 up")


def eth0up():
    os.system("sudo ifconfig eth0 up")


def NetworkAdapterChooseManual():
    clear_screen()
    print(logo)
    print("Manual Mac Adress")
    print("-------------------------------------------")
    print("| eth0 (0)                                |")
    print("| wlan0 (1)                               |")
    print("-------------------------------------------")
    print("| Back (99)                               |")
    print("-------------------------------------------")
    
    NetMCmd = input("\nCommand: ")

    if NetMCmd != "":
        if NetMCmd == "0":
            eth0down()
            mac = input("\nMac: ")
            clear_screen()
            print(logo)
            os.system("sudo macchanger -m eth0 {}", mac)
            sleep(1)
            eth0up()
            input("Press ENTER to go back:")
            main()
        if NetMCmd == "1":
            wlan0down()
            mac = input("\nMac: ")
            clear_screen()
            print(logo)
            os.system("sudo macchanger -m wlan0 {}", mac)
            sleep(1)
            wlan0up()
            input("Press ENTER to go back:")
            main()
        if NetMCmd == "99":
            macchanger()
    else:
        print("\n[!] Wrong Command..")
        sleep(1)
        NetworkAdapterChooseManual()


def NetworkAdapterChooseRandom():
    clear_screen()
    print(logo)
    print("Random Mac Adress")
    print("-------------------------------------------")
    print("| eth0 (0)                                |")
    print("| wlan0 (1)                               |")
    print("-------------------------------------------")
    print("| Back (99)                               |")
    print("-------------------------------------------")
    
    NetRCmd = input("\nCommand: ")

    if NetRCmd != "":
        if NetRCmd == "0":
            eth0down()
            os.system("sudo macchanger -r eth0")
            sleep(1)
            eth0up()
            input("Press ENTER to go back:")
            main()
        if NetRCmd == "1":
            wlan0down()
            os.system("sudo macchanger -r wlan0")
            sleep(1)
            wlan0up()
            input("Press ENTER to go back:")
            main()
            
        if NetRCmd == "99":
            macchanger()
    else:
        print("\n[!] Wrong Command..")
        sleep(1)
        NetworkAdapterChooseRandom()


diagnostic()
