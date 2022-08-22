# Libraries
import time
from time import sleep
import os
import sys
import ctypes
import random

# Change window title
ctypes.windll.kernel32.SetConsoleTitleW("Zerk The Assistant")

# Zerk Ascii
zerk = """                                
,-------.              ,--.     
`--.   /  ,---. ,--.--.|  |,-.  
  /   /  | .-. :|  .--'|     /  
 /   `--.\   --.|  |   |  \  \  
`-------' `----'`--'   `--'`--'                                                            
"""

# Random Username
randomusername = ['xXKittyGamerXx', 'KarinaRBLX01', 'Frekc', 'EasyGamerLol', 'TheMemeGuy', 'Sheepy Man']

# Replaces time.sleep()
def delay(seconds):
    time.sleep(seconds)

# Replaces os.system("cls")
def clean():
    os.system("cls")

# Typing Effect
def write(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)

# Greet
clean() 
write("Hello there!")
print("\n")
write("I'm Zerk\n")
print("\n")





# A main menu sequence
def mainmenu():
    # Menu option. All available actions
    print(zerk)
    write("[1] About\n[2] Random number generator\n[3] Random username generator\n[Q] Quit from Zerk\n")
    # Demands user input
    mainprompt = input("")
    # About option
    def submainmenuone():
        clean()
        write("Zerk is a virtual assistant created by ClamorBits")
        print("\n")
        # Give user option to either ask what feature Zerk currently have or quit back to menu
        write("[1] What are Zerk current features?\n[2] Return to menu\n")
        submainprompt = input("")
        # If they choose 1
        if submainprompt == "1":
            clean()
            write("Features implemented :\n1. Random number generator\n\n")
            input('Enter to return to "About" section : ')
            submainmenuone()
        # If they choose 2
        if submainprompt == "2":
            clean()
            mainmenu()
    
    # Random number generator option
    def submainmenutwo():
        clean()
        firstnum = str(random.randint(1, 9))
        secondnum = str(random.randint(1, 9))
        thirdnum = str(random.randint(1, 9))
        fourthnum = str(random.randint(1, 9))
        fifthnum = str(random.randint(1, 9))
        sixthnum = str(random.randint(1, 9))
        write("Your random 6 digit number is : " + firstnum + secondnum + thirdnum + fourthnum + fifthnum + sixthnum)
        # Return or regenerate
        write("\n\n[1] Regenerate\n[2] Return to main menu\n")
        submainmenutwoprompt = input("")
        
        # Regenerate
        if submainmenutwoprompt == "1":
            clean()
            submainmenutwo()
        
        # Return
        if submainmenutwoprompt == "2":
            clean()
            mainmenu()

    # Random username generator
    def submainmenuthree():
        clean()
        write("Your generated username : " + random.choice(randomusername))
        # Return or regenerate
        write("\n\n[1] Regenerate\n[2] Return to main menu\n")
        submainmenuthreeprompt = input("")

        # Regenerate
        if submainmenuthreeprompt == "1":
            clean()
            submainmenuthree()
        
        # Return
        if submainmenuthreeprompt == "2":
            clean()
            mainmenu()

    # Quit Zerk
    def QuitZerk():
        clean()
        write("Shutting down Zerk...\nDon't close the program\n")
        delay(5)
        clean()
        write("Thank you for using Zerk! :)\n")
        delay(3)
        exit

    # If they choose "About"
    if mainprompt == "1":
        submainmenuone()
    
    # If they choose "Random number generator"
    if mainprompt == "2":
        submainmenutwo()

    # If they choose "Random username generator"
    if mainprompt == "3":
        submainmenuthree()

    # If they want to quit Zerk
    if mainprompt == "Q" or mainprompt == "q":
        QuitZerk()
    
    # If the choices are invalid
    else:
        clean()
        write("\nInvalid choice! Try again.")
        clean()
        mainmenu()

# Startup menu
def startup():
    # Menu option. All available actions
    write("[1] About Zerk\n")
    # Demands user input
    startupprompt = input("")
    # About option
    def substartupone():
        clean()
        write("Zerk is a virtual assistant created by ClamorBits")
        print("\n")
        # Give user option to either ask what feature Zerk currently have or quit back to menu
        write("[1] What are Zerk current features?\n[2] Return to menu\n")
        substartupprompt = input("")
        # If they choose 1
        if substartupprompt == "1":
            clean()
            write("Features implemented :\n1. Random number generator\n\n")
            input('Enter to return to "About" section : ')
            substartupone()
        # If they choose 2
        if substartupprompt == "2":
            clean()
            mainmenu()
    # If they choose "About"
    if startupprompt == "1":
        substartupone()
    
    # If the choices are invalid
    else:
        clean()
        write("\nInvalid choice! Try again.")
        clean()
        startup()

def loginprocess():
    write("Please enter your Zerk ID or type 'Guest' in order to access Zerk : \n")
    loginprocessinput = input("")
    if loginprocessinput == "[REDACTED]":
        clean()
        write("Code accepted, welcome, [REDACTED]\n")
        write("How can I help you today?\n")
        delay(2)
        clean()
        mainmenu()
    elif loginprocessinput == "[REDACTED]":
        clean()
        write("Code accepted, welcome, [REDACTED]\n")
        write("How can I help you today?\n")
        delay(2)
        clean()
        mainmenu()
    elif loginprocessinput == "[REDACTED]":
        clean()
        write("Code accepted, you're signed as an [REDACTED] member\n")
        write("How can I help you today?\n")
        delay(2)
        clean()
        mainmenu()
    elif loginprocessinput == "Guest" or loginprocessinput == "guest":
        clean()
        write("You're using Zerk as guest, for better features, have a Zerk Account. Contact ClamorBits for registration")
        delay(3)
        clean()
        write("How can I help you today?\n\n")
        startup()
    else:
        clean()
        write("Invalid code! Try again.")
        delay(2)
        clean()
        loginprocess()

# Start the main menu for the first time, initially a system startup
loginprocess()