# Dragon Realm, <Keith Dinkins>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart

import random
import time

def displayIntro():

    print('You are in a land full of dragons and trolls. In front of you,')
    print('you see two caves, and a path leading to a desert. In one cave, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print('The desert contains trolls that will assist you, and some that will attack you.')
    time.sleep(2)

def chooseLocation():
    playerChoice = ''
    while playerChoice != '1' and playerChoice != '2'and playerChoice != '3':
        print('Will go into cave 1, cave 2 or the desert (1, 2, or 3)')
        playerChoice = input()
    return playerChoice

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')

def choseDesert(chosenDesert):
    print('You walked to the desert.')
    time.sleep(2)
    print('Its very hot and dry')
    time.sleep(2)

    chosenDesert = random.randint(1,2)

    if chosenDesert == str()

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseLocation()
    checkCave(caveNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()