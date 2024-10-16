# Rock , Paper, Scissors Keith D. v3.0.


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

1) Rock Demolishes Scissors
2) Scissors Slices Paper
3)Paper Consumes Rock
""")

# MULTI-LINE STRINGS CAN BE USED AS COMMENTS






# MAIN GAME LOOP
while playerScore < 5 and cpuScore < 5:
    print(f"{playerName}you have {playerScore} points. \nThe AI has {cpuScore} points.\n")
    playerChoice = input("please enter rock paper, or scissors and enter. \n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("please enter rock paper, or scissors and enter. \n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print("you are not following directions. Please try again\n")
            exit()
        print(f"you have chosen {playerChoice}.")
    else:
        print(f"you have chosen {playerChoice}.")
    #Let cpu select choice at random
    cpuChoice = random.randint(0,2) # RANDOMLY SECTE 0,1, OR 2.
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice = "paper"
    elif cpuChoice == 2:
        cpuChoice = "scissors"
    else:
        print("unable to determine AI choice. \nPlease restart")
        exit()
    print(f"AI Choice: {cpuChoice}")
    # compare player choice to cpu choice
    if playerChoice == "rock" and cpuChoice == "paper":
        print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        print("The AI wins a point")
        cpuScore += 1
    # cpu wins
    elif playerChoice == "rock" and cpuChoice == "scissors":
        print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        print("You win a point")
        playerScore += 1
    #player wins
    elif playerChoice == "rock" and cpuChoice == "rock":
        print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        print("It's a draw")
    # draw
    elif playerChoice == "paper" and cpuChoice == "scissors":
        print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        print("The AI wins a point")
        cpuScore += 1
    elif playerChoice == "paper" and cpuChoice == "rock":
        print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        print("You win a point")
        playerScore += 1
    elif playerChoice == "paper" and cpuChoice == "paper":
        print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        print("It's a draw")
    elif playerChoice == "scissors" and cpuChoice == "rock":
        print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        print("The AI wins a point")
        cpuScore += 1
    elif playerChoice == "scissors" and cpuChoice == "paper":
        print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        print("You win a point")
        playerScore += 1
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        print("It's a draw")
    #print results to the
    #award point to winner
        
print(f"Your final score: {playerScore}\nAI final score: {cpuScore}.\n")
if playerScore > cpuScore:
    print(f"Congratulations {playerName},you win big dawg")
elif cpuScore > playerScore:
    print(f"The AI wins. you are really bad at this get better man")
else:
    print("unable to determine a winner. \n please restart")
    exit()