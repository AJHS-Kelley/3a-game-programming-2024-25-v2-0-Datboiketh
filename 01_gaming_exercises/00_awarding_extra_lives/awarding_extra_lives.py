# Award extra lives, Keith Dinkins, V0.0

lives = 3
score = 1000000

# allow the user to input the score as an integer

# allow user to input score
if score <= 10000:
    print("lose a life")
elif score < 100001:
    print("Give 1 extra life")
elif score > 100000: 
    print("Give 2 extra lives")

# Output the score and number of lives to the screen.