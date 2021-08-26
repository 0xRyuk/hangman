import random
from os import system, name

def clear():
  
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

banner = ['''
                      +---+
      Wrong!          |   |
    You have 8/20         |
more guesses left         |
                          |
                          |
=============================''', '''
                      +---+
      Wrong!          |   |
    You have 7/20     O   |
more guesses left         |
                          |
                          |
=============================''', '''
                      +---+
      Wrong!          |   |
    You have 6/20     O   |
more guesses left     |   |
                          |
                          |
=============================''', '''
                      +---+
      Wrong!          |   |
    You have 5/20     O   |
more guesses left    /|   |
                          |
                          |
=============================''', '''
                      +---+
      Wrong!          |   |
    You have 4/20     O   |
more guesses left    /|\  |
                          |
                          |
=============================''','''
                      +---+
      Wrong!          |   |
    You have 3/20     O   |
more guesses left    /|\  |
                          |
                          |
=============================''','''
                      +---+
      Wrong!          |   |
    You have 2/20     O   |
more guesses left    /|\  |
                          |
                          |
=============================''', '''
                      +---+
      Wrong!          |   |
    You have 1/20     O   |
more guesses left    /|\  |
                     /    |
                          |
=============================''','''
                           +---+
                           |   |
      H A N G M A N        O   |
            by            /|\  |
     Rishi Choudhary      / \  |
                               |
==================================
You have total 20 guess points.
==================================''']

level = 1
def random_word():
    """
    This function will genrate choose random word from the file 'words.txt'.
    """
    level = int(input('Choose a dificulty level : '))
    if level == 1:
        print('Setting dicifulty level : \'Easy\'.')
        print('Default dicifulty level : \'Easy\' is already set.')
        wordlist = 'easy.txt'
    elif level == 2:
        print('Setting dicifulty level : \'Medium\'.')
        wordlist = 'medium.txt'
    elif level == 3:
        print('Setting dicifulty level : \'Hard\'.')
        wordlist = 'hard.txt'
    else:
        print('Default dicifulty level is : \'easy\'.')
        level = 1
    try:
        with open('wordlist/'+wordlist) as file:
            content = file.readlines()
    except Exception as e:
        print(e,'\n Error opening in file.')
    
    return random.choice(content)
print(banner[8])
word = random_word()
guess = ''
failed = 0
count = 20
n = 3
try:
    while count > 0:
        failed = 0
        win = f"""
                           
                              
       YOU WIN!                  +---+
                          \O/   /    \\
The word is :{word}!\t   |    \    /
Thankyou for playing      / \   |  
==================================
"""
        lose = f'''
                  +---+
                  |   |
    GAME-OVER!    O   |
    You loose    /|\  |
    this game!   / \  |
                      |
=========================
Word is : {word}
=========================
'''
        for letter in word:
            if letter in guess:
                print(letter+' ',end='')
            else:
                print('_ ',end='')
                failed += 1
        if failed == 0:
            clear()
            print(win)
            break
        g = input('\n\nGuess the letter : ').lower()
        guess += g

        
        if guess not in word:
            clear()
            count -= 1
            if count == 8:
                print(banner[0])
            elif count == 7:
                print(banner[1])
            elif count == 6:
                print(banner[2])
            elif count == 5:
                print(banner[3])
            elif count == 4:
                print(banner[4])
            elif count == 3:
                print(banner[5])
            elif count == 2:
                print(banner[6])
            elif count == 1:
                print(banner[7])
            elif count == 0:
                print(lose)
            else:
                print(f'''

      Wrong!          
    You have {count}/20     
more guesses left


==================================''')

except EOFError as e:
    print('Please provide an valid input!')
except KeyboardInterrupt:
    print('\nExiting...')