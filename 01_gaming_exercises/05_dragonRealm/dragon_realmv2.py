# Dragon Realm, <STUDENT_NAME>, v0.0 <-- UPDATE YOUR NAME AND VERSION NUMBER 
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# Good progress so far, keep going on the project.  
import random, time, datetime

# SAVEING A FILE
# Step 1 creating the file name to use
logFileName = "dragonRealmlog.txt"
# logFileName = "dragoRealmlog.txt"
# example dragonRealmLog 11:32.txt

# step 2 -- create /. open the file to save data.
saveData = open(logFileName, "a") 
# FILE MODES
# "x" CREATES FILE, IF FILE EXIST, EXIT WITH MESSAGE.
# "w" CREATES FILE, IF FILE EXIST, ERASE AND OVERWRITE FILE CONTENTS
# "a" CREATES FILE, IF FILE EXIST, APPEND DATA TO THE FILE.

saveData.write("GAME STARTED" + " " + str(datetime.datetime.now()) + "\n")

itemsChosen = 0
hasWaterBottle = False
hasSheild = False
hasSword = False
hasOnion = False

while itemsChosen < 2:
    itemsChosen = input('Before you go out on a adventure you have to have your gear, Please select 2 items you would like to take.\n [1]Waterbottle \n [2]Sheild \n [3]Sword \n')
    if itemsChosen == '1':
        hasWaterBottle = True
    elif itemsChosen == '2':
        hasSheild = True
    elif itemsChosen == '3':
        hasSword = True
    elif itemsChosen == '4':
        hasOnion = True
    else
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
    print('Its Dark and Scary, so scary that youre shivering in your boots\n')
    time.sleep(2)
    print('A Dragon apears out of nowhere and...\n')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenPath == str(friendlyCave): # If this is the friendly cave, why am I getting burned to death?
        print('Burns you with his fire breath')

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


# CLOSE THE FILE
saveData.write("END OF GAME LOG\n\n")
saveData.close()


