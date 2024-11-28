#Flow control Structures, Ryan Kelly, v0.0
#Making Computer Programs Make Decisions

temperature = 30
color = "Blue"
height = 6
likesPineappleOnPizza = False

#SINGLE DECISION POINT - if statement
#if CONDITIONAL_EXPRESSION: <-- this will use a comparsion operator 99% of the time
   #runthiscode if the CONDITIONAL_EXPRESSION is true

if temperature > 100:
   print("Bring a hat and water")

#cheat code for if statments that use booleans.
#if likesPineappleOnPizza:
 #  ("Nasty")

   #what if we want something different to happen?
if color == "Red" : #COMMON ERROR FOR STUDENTS IS UNSING = INSTEAD OF ==.
 
 
 if height >= 5:
   print("You're tall enough to ride the Hulk coaster!\n")
elif height >= 8:
  print("You're too tall to ride the Hulk coaster\n")
else: #"oh no sometinhs wrong!"
  print("Error, height not detected. Do not ride.\n")
# when writing if-elif-else blocks check HIGHEST VALUE first when unsing > or >=




# when writing if-elif-else blocks check LOWEST VALUE first when unsing < or <=
if height <= 5:
   print("You're not tall enough to ride the Hulk coaster!\n")
elif height < 8:
  print("You're tall enough to ride the Hulk coaster\n")
else: #"oh no sometinhs wrong!"
  print("Error, height not detected. Do not ride.\n")


if temperature >= 100:
  print("Too hot no recess\n")
elif temperature >= 50:
  print("recess is allowed\n")
elif temperature > 0:
  print("recess will be in gym")
else:
  print("Error, Temp not detected. no recess\n")