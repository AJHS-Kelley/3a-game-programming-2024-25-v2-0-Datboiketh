# Data Types and operators, Keith Dinkins, v0.0

#Funamentals Data Types
#string- str - Sequence of letters, numbers, spaces, or other charaters
#strings in python are in side ' ' or " "

# Boolean - bool - True or False values.

# Float - float - any number value with a decimal, +/-, Including 0.

# Intergers - int - any whole number , +/-, including 0.

#data  that you stored in VARIBLES
#VARIABLES NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED
#VARIABLES CANNOT START WITH A NUMBER
#camelcasevariablenames
#snake_case_variables_names

# DECLARING VARIBALES AND ASSINGING VALUES



highScore =3 #int data types

carSpeed =420.69 #float data type mph

hasAxe = True #boolean data type
isPurple= False #boolean data type

playerName = "Ryomen Sukuna" #string data type

abilityName = "World Splitting Dismantle" 

# ASSIGN NEW VALUES
playerName = "Datboiketh"
carSpeed = 3.45

# DATATYPES CAN CHANGE, BE CARFUL
hasAxe = 4.0
# Printing data types

newInt = 3
newFloat = 4.0
newString = "Skibidi Toilet"
newBool = False

# print(type(newInt))
# print(type(newFloat))
# print(type(newString))
# print(type(newBool))
# printing Variables
# print(playerName)
# print(isPurple)
# print(highScore)
# print(carSpeed)

#printing expressions and variables
# print(highScore + 69000)
# print(4 * 12)
# print(highScore)

# PRINTING VARIABLES INSIDE OF 
# print(f"Hello {playerName}. Suprisingly you have a high score of {highScore}.\n")

#ARITHIMATIC OPERATIONS
myInt = 69
myFloat = 69.69
myNum = 0

#addition
myInt = 7 +10 
myFloat = 4.0 + 90

myInt = myInt + 5

myInt = myInt + -12

myNum = myInt +myFloat

# when ypu add an int and a float together, the answer becomes a float

#subtarcatcion 
myNum = myInt - myFloat
myInt = myFloat - 1.25

#multplication 

myNum = myInt *myFloat

#division

myNumber = myInt / myFloat # first is numerator, second num is demoninator

#Modulus (modulu) % -- REMAINDER after dividing.
# MOST COMMON USE FOR MODULUS IS DETERMINING EVEN / ODD NUMBER
numStudents = 6
numSlicesPizza = 35

leftOvers = numSlicesPizza % numStudents
# print(leftOvers)

#EXPONENTS **
numSquared = 5 ** 2 # 5 is the base, 2 is the experiment.

# Floor - Division // -- Divides, throws out any decimal.
myNum = myInt // myFloat

# Addition-Assignment operartor - Mostly used for counters

myNum = 5
myNum = myNum + 1 #oldschool method
myNum += 1 #new hotness

#COMPARISON OPERATORS

# IS EQUAL- TO == Are the two values equal to each other?
# Returns True or False based on evalulation
x = 12.0
#print(x == 5)

# NOT EQAUL-TO != are the two valuse not equal?
# retures true or false based on evalution
# print(x != 12)

# GREATER THAN / GREATER THAN OR EQAUL TO
# print(5 > 3) #greater than
# print (12 >= 2) # greater than equal to

# Less THAN / Less THAN OR EQAUL TO
# print(5 < 3) #Less than
# print (12 <= 2) # Less than equal to

# LOGICAL OPERATOR
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATMENT TO BE TRUE
age = 44
height = 73.5
eyeColor = "brown"
# In order to ride the teacups, you must be at 18 years old and 60" tall.
print(age >= 18 and height >= 60)
print(age >= 18 and height >= 60 and eyeColor == "Yellow")
#ALWAYS CHECK FOR THE LEAST LIKLEY TO BE FALSE CONTIONS FIRST!!!!!!!!
#print(defeatedBoss == True and level > 5 and hasBlueKey == True)


# or -- AT LEAST ONE CONDITION MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
print(age >= 18 or height >= 60)
print(age >= 18 or height >= 60 or eyeColor == "Yellow")
#ALWAYS CHECK FOR THE LEAST LIKLEY TO BE TRUE CONTIONS FIRST!!!!!!!!
#print(defeatedBoss == True or level > 5 or hasBlueKey == True)

# not -- RETURNS THE OPPOSITE VALUE OF THE STATMENT.
a = 34
print(a == 34)
print(not (not(a == 34)))

# COMBINING LOGICAL OPERATORS
#print(a == 5 and hasKey == True or isCloud == True)
#TRUE and

# IDENTITY OPERATORS
g = 1.0
h = 1.0
i = g
print(g is h)
print(i is h)
#print(i is not g 1.0)
print(i is not g)

# MEBERSHIP
fruits = ["apple", "banana", "tamato"]
print("banana" in fruits)
print("patato" in fruits)