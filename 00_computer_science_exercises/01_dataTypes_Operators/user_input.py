# User Input practice, Keith Dinkins, v0.0

# input() is the built-in funtion to get information from the keyboard
# Basic example
#variableName = input("Scale of the dragon, Recoil, Twin meteors, World Cutting Slash.\n")
#print(variableName)

# input() saves all input to string data types by default
# input() saves all input to string data types by default
# input() saves all input to string data types by default
# input() saves all input to string data types by default

# incorect, causes a concatentation error
#myNumber =  input("please type an interger number and press enter")
#print(myNumber + 5)

# Correct -- Use a wrapper.
myNumber =  input(input("please type an interger number and press enter"))
print(myNumber + 5)

# Wrapper Functions
# int() will covert the data to an interger if possiable.
newNumber = input("Please type a value and press enter. \n")
print(int(newNumber))
print(float(newNumber))
print(str(newNumber))

# float() will convert the data to a float if possible.
newNumber = input("Please type a value and press enter. \n")
#print(int(newNumber)) <-- cannot FLOAT to INTERGER.
print(float(newNumber)) # can convert STRRING to float
print(str(newNumber)) # can convert float to string.

# str() will convert  the data to a String if possible.
newNumber = input("Please type a value and press enter. \n")
print(float(newNumber))
print(str(newNumber))

