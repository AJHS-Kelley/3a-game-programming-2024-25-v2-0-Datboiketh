# Rock , Paper, Scissors Keith D. v0.4

# MODULE IMPORTS
import random

# DATA STRUCURES -- Player
playerName = "Test Player"
playerScore = 0
playerChoice = None

# DATA STRUCURES
cpuScore = 0
cpuChoice = None

#PLAYER NAME INPUT
playerName = input("Type name and press enter.\n")
print(f"Hello {playerName}!")
isCorrect = input("Is this correct? Type yes or no and press enter. \n").lower()

# .lower() turns all into lower case
# .upper() turns all into upper case

if isCorrect == "yes": 
    print(f"Ok {playerName}, let's play, Rock, Paper, Scissors!")
else:
    playerName = input("Type your name and press enter.\n")

# THE RULES
print(f"""
Welcome {playerName} to the Rock, Paper, Scissors Robot!
It's time to play  Rock, Paper, Scissors!

You will play agasint an AI. the first one to score 5 points wins.
You will select from Rock, Paper or scissors.
The CPU will select Rock, Paper, or Scissors.

1) Rock beats Scissors
2) Scissors beats Paper
3)Paper beats Rock
""")

# MULTI-LINE STRINGS CAN BE USED AS COMMENTS






# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName}you have {playerScore} points. \nThe AI has {cpuScore} points.\n")
    playerChoice = input("please enter rock paper, or scissors and enter. \n").lower()
    if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
        playerChoice = input("please enter rock paper, or scissors and enter. \n").lower()
        if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
            print("you are not following directions. Please try again\n")
            exit()
        print(f"you have chosen {playerChoice}.")
    else:
        print(f"you have chosen {playerChoice}.")



    #Let cpu select choice at random
    #compare player choice to cpu choice
    #print results to the screen
    #award point to winner