# Functions practice, Keith DInkins, v0.1

import random

def helloWorldMulti(): # FUNCTION SIGNATURE
    """This Funtion will output Hello, world! in a language the user choose. """ # DoCSTRING 
    # print a list of languages to the screen, at least three but no more than five.
    # allow the use to selct input a choice for the languauge.
    print("""Hello User you will have the option to pick three languages from what I have avalaible
          These are the languages the are available
          [S]panish
          [J]apanese
          [F]rench
          [C]hinese
          [E]nglish
            """)
    
    language = input("Please put the first letter of What language would you like to pick?\n").lower()

    if language == "s":
        print("Hola Mund")
    elif language == "j":
        print("Kon'nichiwa sekai")
    elif language == "f":
        print("Bonjour le monde")
    elif language == "c":
        print("Nǐ hǎo shìjiè")
    elif language == "e":
        print("Hello world")    
    else:
        print("unable to find langauge")
        exit()

helloWorldMulti()


argument1 = random.randint(-1000, 1000)
    
def isEven(argument1: int) -> bool: 
    """Determines if interger value is even or odd."""
    if argument1 % 2 == 0:
        return True
    else:
        return False

print(isEven(argument1))

#Function with multiple arguments
def canRideRollerCoaster(age: int, height: int) -> bool:
    if age > 10 and height > 4:
        print("you can ride.\n")
        return True
    else:
        print("you cannot ride.\n")
        return False
canRideRollerCoaster(4,10) #arguments must be passed in the dame order as the function signature indicates.



