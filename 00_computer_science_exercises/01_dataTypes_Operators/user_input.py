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
# float() will convert the data to a float if possible.
# str() will convert  the data to a String if possible.
er