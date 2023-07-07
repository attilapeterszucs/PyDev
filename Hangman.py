import os
import random
from collections import Counter

logo = """ 
     _   __                 _                _   _       _     
    | | / /                | |              | | | |     | |    
    | |/ / _ __ _   _ _ __ | |_ ___  _ __   | |_| |_   _| |__  
    |    \| '__| | | | '_ \| __/ _ \| '_ \  |  _  | | | | '_ \ 
    | |\  \ |  | |_| | |_) | || (_) | | | | | | | | |_| | |_) |
    \_| \_/_|   \__, | .__/ \__\___/|_| |_| \_| |_/\__,_|_.__/ 
                 __/ | |                                       
                |___/|_|                                       

                        <-- Hangman -->
                        
"""
  
Words = '''apple banana mango strawberry 
orange grape pineapple apricot lemon coconut watermelon
cherry papaya berry peach lychee muskmelon krypton cat monster 
dog negro watermelon night sun horse'''
  
Words = Words.split(' ')

word = random.choice(Words)         
  
if __name__ == '__main__':
    os.system('clear')
    print(logo,'\n\nGuess the word!')
      
    for i in word:
        print('_', end = ' ')        
    print()
  
    playing = True
    letterGuessed = ''                
    chances = len(word) + 2
    correct = 0
    flag = 0
    try:
        while (chances != 0) and flag == 0:
            print()
            chances -= 1
  
            try:
                guess = str(input('Enter a letter to guess: '))
            except:
                print('Enter only a letter!')
                continue
  
            if not guess.isalpha():
                print('Enter only a LETTER')
                continue
            elif len(guess) > 1:
                print('Enter only a SINGLE letter')
                continue
            elif guess in letterGuessed:
                print('\nYou have already guessed that letter')
                continue
  
  
            if guess in word:
                k = word.count(guess)
                for _ in range(k):    
                    letterGuessed += guess
  
            for char in word:
                if char in letterGuessed and (Counter(letterGuessed) != Counter(word)):
                    print(char, end = ' ')
                    correct += 1
                elif (Counter(letterGuessed) == Counter(word)): 
                    print("The word is: ", end=' ')
                    print(word)
                    flag = 1
                    print('\n\nCongratulations, You won!')
                    break
                else:
                    print('_', end = ' ')
  
              
  
        if chances <= 0 and (Counter(letterGuessed) != Counter(word)):
            print()
            print('\nYou lost! Try again..')
            print('\n     The word was: {}'.format(word))
  
    except KeyboardInterrupt:
        print()
        print('Bye! Try again.')
        exit()