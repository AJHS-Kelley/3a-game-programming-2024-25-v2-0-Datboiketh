#loops, Keith D. v0.0
import random # import random module for us to use.
# generally put all your import statments at the top.

# TWO TYPES OF LOOPS
# for <-- Used when you know how many loops you'll need.
# while <-- Used when you do not know how many loops you'll need.'

# for loops like Go Fish, you search each card for what the player asked.
# while loop is like musicals chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENTIRE LOOP IS CALLED AN iteration
# "iterate through the list" means use a loop

# for loops Example -- Iterating
# fruits = ["tamato", "banana", "blueberry", "mango"]
# for eachfruit in fruits:
#     print(eachfruit)

# continue Keyword -- Skips the current iterartion and then finishes the loop
# fruits = ["tamato", "banana", "blueberry", "mango"]
# for eachfruit in fruits:
#     if eachfruit == "banana":
#         continue
#     print(eachfruit)

# break Keyword -- Immediately exit loop
# fruits = ["tamato", "banana", "blueberry", "mango"]
# for eachfruit in fruits:
#     if eachfruit == "banana":
#         break
#     print(eachfruit)

# for loops using range(). range(x) is EXCLUSIVE, it starte at 0 ends at x - 1
# for i in range(10): #range is 0-9
#     print(i)

# Might not alway want to start at 0
# for i in range(10, 100): #
#     print(i)

# Not wan to count by 1
# for i in range(10, 100, 5): # 10 = start, 100 - 1 = stop, 5 # to countby
#    print(i)

# Sometimes ypure not done writint the loops
#for x in range(10):
#    pass #tell python this loop is being worked on, calm down

# while loops -- musical chairs
playerscore = 0
counter = 0
while playerscore < 100: #run as long as this is true.
     print(f"Starting: {playerscore}")
     playerscore += random.randint(1,100)
     print(f"After: {playerscore}")
     counter += 1
print(counter)
