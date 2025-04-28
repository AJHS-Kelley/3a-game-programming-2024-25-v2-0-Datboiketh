# Rock , Paper, Scissors Keith D. v0.4

# MODULE IMPORTS
import random, time

# DATA STRUCURES -- Player
playerScore = 0
playerChoice = None
numDraws = 0

# DATA STRUCURES
cpuScore = 0
cpuChoice = None

# MAIN GAME LOOP
loopCount = 0
loopsReq = int(input("how many loops do you want? \nEnter an interger, no commas, and press ENTER.\n"))
#req is universal abbreviation for request
rpsTimeStart = time.time() # returns the number of seconds sinsce Jan. 01, 1970 @ 12:00AM
while loopCount < loopsReq:
    
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
    #let PLAYER choice at random
    playerChoice = random.randint(0,2) # RANDOMLY SECTE 0,1, OR 2.
    if playerChoice == 0:
        playerChoice = "rock"
    elif playerChoice == 1:
        playerChoice = "paper"
    elif playerChoice == 2:
        playerChoice = "scissors"
    else:
        print("unable to determine AI choice. \nPlease restart")
        exit()
    # compare player choice to cpu choice
    if playerChoice == "rock" and cpuChoice == "paper":
        # print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        # print("The AI wins a point")
        cpuScore += 1
        #cpuScore = cpuScore + 1
    # cpu wins
    elif playerChoice == "rock" and cpuChoice == "scissors":
        # print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        # print("You win a point")
        playerScore += 1
        #playerScore = playerScore + 1
    #player wins
    # draw
    elif playerChoice == "paper" and cpuChoice == "scissors":
        # print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        # print("The AI wins a point")
        cpuScore += 1
        #cpuScore = cpuScore + 1
    elif playerChoice == "paper" and cpuChoice == "rock":
        # print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        # print("You win a point")
        playerScore += 1
        #playerScore = playerScore + 1
        numDraws += 1
    elif playerChoice == "scissors" and cpuChoice == "rock":
        # print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        # print("The AI wins a point")
        cpuScore += 1
        #cpuScore = cpuScore + 1
    elif playerChoice == "scissors" and cpuChoice == "paper":
        # print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        # print("You win a point")
        playerScore += 1
        #playerScore = playerScore + 1
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        # print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        # print("It's a draw")
        numDraws += 1
    elif playerChoice == "paper" and cpuChoice == "paper":
        # print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        # print("It's a draw")
        numDraws += 1
    elif playerChoice == "rock" and cpuChoice == "rock":
        # print(f"The AI chose {cpuChoice} and you chose {playerChoice}. \n")
        # print("It's a draw")
        numDraws += 1
    loopCount += 1
    #print results to the
    #award point to winner
        
print(f"Your final score: {playerScore}\nAI final score: {cpuScore}.\nDraws: {numDraws}")
if playerScore > cpuScore:
    print(f"Congratulations, you win big dawg")
elif cpuScore > playerScore:
    print(f"The AI wins. you are really bad at this get better man")
else:
    print("unable to determine a winner. \n please restart")
    exit()
rpsTimeStop = time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f"Number of loops : {loopCount}\n")
print(f"Exucution Time {rpsTime: .2F} seconds . \n")