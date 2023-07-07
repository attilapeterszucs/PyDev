import subprocess
import platform
import os
from time import sleep

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

                <-- Wifi Password Stealer -->

"""

def main():
    clear_screen()
    print(logo)
    print("-------------------------------------------")
    print("| Show IP address (0)")
    print("| Show Wifi Passwords (1)")
    print("-------------------------------------------")
    print("| Exit (99)")
    print("-------------------------------------------")
    inputs()

def inputs():

    cmd = input("\nCommand: ")

    if cmd != "":
        if cmd == "0":
            clear_screen()
            os.system("ipconfig")
            input("\n\nPress ENTER to continue:")
            main()

        if cmd == "1":
            clear_screen()
            print(logo)
            core()
            input("\n\nPress ENTER to continue:")
            main()

        if cmd == "99":
            print("\nExiting...")
            sleep(2)
            clear_screen()
            exit
    else:
        print("\n[!] Wrong Command..")
        sleep(1)
        main()

def core():
    completed_process = subprocess.run(["netsh","wlan","show","profiles"], shell=True, capture_output=True)

    output = completed_process.stdout.decode()
    output = output.split("\n")

    access_points = []
    for line in output:
        if "All User Profile" in line:
            split_line = line.split(":")
            ap = split_line[1][1:-1]
            access_points.append(ap)

    for access_point in access_points:
        ap_result = subprocess.run(["netsh","wlan","show","profiles",access_point,"key=clear"], shell=True, capture_output=True)
        ap_result = ap_result.stdout.decode()
        ap_result_list = ap_result.split("\n")
        for line_result in ap_result_list:
            if "SSID name" in line_result:
                print(line_result)
            
            if "Key Content" in line_result:
                print(line_result)

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
        print("\nYou have to run this program on Windows, you currently trying to run it on: ", sysOS)
        print("\nExiting...")
        sleep(1)
        exit
    else:
        main()

diagnostic()
