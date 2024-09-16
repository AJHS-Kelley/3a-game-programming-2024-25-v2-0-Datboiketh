# Award extra lives, Keith Dinkins, V0.0

lives = 5
score = 100
name = "Keith"
print(f"Hello{name}! You scored {score} points.\n")

# allow the user to input the score as an integer

# allow user to input score
if score < 10000:
    print("lose a life")
    lives -= 1
elif score < 100001:
    print("Give 1 extra life")
    lives += 1
elif score > 100000: 
    print("Give 2 extra lives")
    lives += 2 

print("live: " + str(lives))
print("score: " + str(score))
# Output the score and number of lives to the screen.