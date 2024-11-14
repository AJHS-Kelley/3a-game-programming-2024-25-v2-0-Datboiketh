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
        path = input('Will go down path 1 to the cave or path 2 to the desert?\n (Enter 1 or 2):') # Add a description for 1 and 2 
    return path

def pathCave():
    
    print('You walk down the path to the cave\n')
    time.sleep(2)
    print('You enter the cave with the little bit of courage you have.\n')
    time.sleep(2)
    print('Its Dark and Scary...\n')
    time.sleep(2)
    print('A Dragon apears out of nowhere and...\n')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenPath == str(friendlyCave):
        print('Gives you a sword')

    else:
        print('Gobbles you down in one bite!')
    return friendlyCave

def pathDesert():
    
    print('You walk down the path to the desert, it is very hot and dry.\n')
    time.sleep(1)
    print('As you continue to walk through the heat, you start to feel dizzy.\n')
    time.sleep(1)
    print('You notice a town in the far distance.\n')
    time.sleep(2)
    choice = input('Do you walk to the village or Keep going along the path\n')



playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    chosenPath = chooseLocation()
    if chosenPath == '1': #cave
        pathCave()
    else:
        pathDesert()
        
    print('Do you want to play again? (yes or no)')
    playAgain = input()





