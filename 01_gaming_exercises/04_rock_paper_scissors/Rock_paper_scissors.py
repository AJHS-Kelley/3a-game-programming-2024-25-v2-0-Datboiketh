# Rock , Paper, Scissors Keith D. v0.2

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
if isCorrect == "yes": 
    print(f"ok {playerName}, let's play, Rock, Paper, Scissors!")
else:
    playerName = input("Type your name and press enter.\n")