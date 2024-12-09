# Dragon Realm, <STUDENT_NAME>, v0.0 <-- UPDATE YOUR NAME AND VERSION NUMBER 
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# Good progress so far, keep going on the project.  
# Great job Keith!  This was a tough project and you buckled down to complete it.  
# I hope you find it challenging yet fun to complete. 
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

numItems = 0
hasWaterBottle = False
hasSheild = False
hasSword = False
hasOnion = False

while numItems < 2:
        itemsChosen = input('Before you go out on a adventure you have to have your gear, Please select 2 items you would like to take.\n [1]Waterbottle \n [2]Sheild \n [3]Sword \nEnter Choice Here:')
        if itemsChosen == '1':
            hasWaterBottle = True
            print('You now have the waterbottle now you can hydrate\n')
            time.sleep(1) 
            numItems += 1
        elif itemsChosen == '2':
            hasSheild = True
            print('Good now you can parry attacks\n')
            time.sleep(1) 
            numItems+= 1
        elif itemsChosen == '3':
            hasSword = True
            print('Now you can ruthlesly kill innocents\n')
            time.sleep(1) 
            numItems += 1
        elif itemsChosen == '4':
            hasOnion = True
            print('You got an onion idk how that will help but sure\n')
            time.sleep(1) 
            numItems += 1
        else:
            print('you gotta take something or else you might die man\n')
            time.sleep(2)



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

def pathDesert(hasWaterBottle, hasOnion:bool ) -> bool:
    
    print('You walk down the path to the desert, it is very hot and dry.\n')
    time.sleep(1)
    print('As you continue to walk through the heat, you start to feel dizzy.\n')
    time.sleep(1)
    print('You notice a town in the far distance.\n')
    time.sleep(2)
    choice = input('Will you walk to the Town? (yes or no)\n')
    if choice == 'yes' and hasWaterBottle:
        print('You walk to the Town')
        time.sleep(2)
        print('While you walk to the town, you remember your waterbottle and you take a sip.\n')
        time.sleep(2)
        print('The town slowly fades away, it turned out to be a mirage.\n')
        time.sleep(2)
        print("Aren't you glad you chose the waterbottle, anyways you continue throught the hot desert.\n")
        time.sleep(2)
        print('As you walk you feel the ground begin to rumble.\n')
        time.sleep(2)
        print('All of a sudden a sandworm leaps over your head, you see a sign that say "Worm Valley"\n')
        time.sleep(2)
        print("You now trembling begin to realize the adventure you're taking, but then you rember your goal\n")
        time.sleep(2)
        print('You stop your trembling and contiue along the path\n')
        time.sleep(2)
        print('As you continue you see your destination in the distance\n')
        time.sleep(2)
        print('you walk to the kingdom gates but you notice dont have the secret item to get in looks like all you troubles were for nothing oh well\n')
        time.sleep(1)
        print('THE END\n')
        time.sleep(2)
    elif choice == 'yes' and hasWaterBottle and hasOnion:
        print('You walk to the Town')
        time.sleep(2)
        print('While you walk to the town, you remember your waterbottle and you take a sip.\n')
        time.sleep(2)
        print('The town slowly fades away, it turned out to be a mirage.\n')
        time.sleep(2)
        print("Aren't you glad you chose the waterbottle, anyways you continue throught the hot desert.\n")
        time.sleep(2)
        print('As you walk you feel the ground begin to rumble.\n')
        time.sleep(2)
        print('All of a sudden a sandworm leaps over your head, you see a sign that say "Worm Valley"\n')
        time.sleep(2)
        print("You start trembling and begin to realize the adventure you're taking, but then you rember your goal\n")
        time.sleep(2)
        print('You stop your trembling and contiue along the path\n')
        time.sleep(2)
        print('As you continue you see your destination in the distance\n')
        time.sleep(2)
        print('you walk to the kingdom gates and They notice you have the secret item which was the onion?\n')
        time.sleep(2)
        print('I guess the onion did come in handy. Well you made to your goal congrats')
        time.sleep(2)
        print('THE END\n')
        time.sleep(2)
    elif choice == 'yes' and  not hasWaterBottle:
        print('You walk to the Town\n')
        time.sleep(2)
        print('You make it to the you thought to yourself its very empty\n')
        time.sleep(2)
        print('You see a well, and you rush to it...\n')
        time.sleep(2)
        print("it turns out to be a mirage. Really shouldve gotten that waterbottle is what you're thinking now\n")
        time.sleep(2)
        print('As the sun sets, you feel the ground starts to rumble\n')
        time.sleep(2)
        print('You think nothing of it and continue along the path\n')
        time.sleep(2)
        print('You pass out from dehydration and you wake in the stomach of a sandworm')
        print("should've drunk some water man\n")
        time.sleep(2)
        print('THE END\n')
    elif choice == 'no':
        print('You continue along the path, but its taking longer than intended')
        time.sleep(2)
        print('As the sun sets, you feel the ground starts to rumble\n')
        time.sleep(2)
        print('You think nothing of it and continue along the path\n')
        time.sleep(2)
        print('You pass out from dehydration and you wake in the stomach of a sandworm')
        print("should've drunk some water man\n")
        time.sleep(2)
        print('THE END\n')


playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    chosenPath = chooseLocation()
    if chosenPath == '1': #cave
        pathCave()
    else:
        pathDesert(hasWaterBottle, hasOnion)
        
    print('Do you want to play again? (yes or no)')
    playAgain = input()


# CLOSE THE FILE
saveData.write("END OF GAME LOG\n\n")
saveData.close()


