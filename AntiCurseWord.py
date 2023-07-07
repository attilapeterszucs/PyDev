import os
from time import sleep

logo = """ 
     _   __                 _                _   _       _     
    | | / /                | |              | | | |     | |    
    | |/ / _ __ _   _ _ __ | |_ ___  _ __   | |_| |_   _| |__  
    |    \| '__| | | | '_ \| __/ _ \| '_ \  |  _  | | | | '_ \ 
    | |\  \ |  | |_| | |_) | || (_) | | | | | | | | |_| | |_) |
    \_| \_/_|   \__, | .__/ \__\___/|_| |_| \_| |_/\__,_|_.__/ 
                 __/ | |                                       
                |___/|_|                                       

                     <-- Anti Curse Word -->
"""
def main():
    os.system("clear")
    print(logo)
    test_str = input("\nYour text: ")
    print("\nThe original string is : " + str(test_str))
    
    word_list = ['ass','Ass','stupid','Stupid','idiot','Idiot','retard','Retard', 'fucking','Fucking', 'damn','Damn',
     'bitch','Bitch', 'fuck','Fuck', 'shit', 'Shit', 'asshole','Asshole', 'faggot', 'Faggot', 'darn', 'Darn', 'cunt', 
     'Cunt', 'motherfucker', 'Motherfucker', 'gosh', 'Gosh',] 
    
    repl_wrd = '*****' 
    res = ' '.join([repl_wrd if idx in word_list else idx for idx in test_str.split()]) 
    print("\nAnti Curse Text: " + str(res))
    
    gen_new = input("\nPress ENTER for new text! or (exit): ")
    if gen_new == "":
        os.system("cls")
        main()
    elif gen_new == "exit":
        exit
    else:
        os.system("cls")
        print(logo)
        print("\nSomething went wrong!")
        sleep(1)
        main()
main()
