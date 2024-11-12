# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time

def displayIntro():

    print('Greetings traveler you will be going on an Adventure through Adventure valley,') 
    print('You will encounter many things such as Dragons, Trolls, and Sandworms.')
    print('Your goal is to make to Far Far Away Land without dying.\n')
    time.sleep(2)

    print('You notice 2 paths one leading to a Dark and Scary Cave')
    print('while the other leads to a Dry and Hot Desert\n')
    time.sleep(1)

def chooseLocation():
    path = ''
    while path != '1' and path != '2':
        print('Which path will you go down (1 or 2)')
        path = input()
    return path

def checkPath(chosenpath):
    
    if path == '1':
        print('You walk down the path...\n')
    time.sleep(2)
    print('You go into the cave...\n')
    time.sleep(2)
    print('Its Dark and Spooky...\n')
    time.sleep(2)
    print('A Dragon apears out of nowhere and...\n')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenpath == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseLocation()
    checkPath(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()