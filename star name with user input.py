# trying with user input

import time
import sys
# every part is put into a function for easier calling

# welcome greetings
def welcome():
    greet = "\033[1;32mHi! Welcome to HF's \033[1;33mSTAR NAME\n \033[1;32mThis program prints your name in stars\n Let's try it with mine!\n My name is:"
    for i in greet: # this is to put a delay per letter in the printed output to give a typing effect
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.06),
    print()
    loading = " . \n .\n ."
    for i in loading: # loading dots with delay effect 
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.17),
    print()

# structuring the letters

def nameStars():  
    nameLetters = {"H": ["*   *", "*   *", "*****", "*   *", "*   *"], # listing the star structures of the letters in dictionary
        "A": [" *** ", "*   *", "*****", "*   *", "*   *"], # using this method makes it easier to form the name
        "N": ["*   *", "**  *", "* * *", "*  **", "*   *"] }
    strHanna = "hanna" 
    yellow = "\033[1;36m"
    for i in range(5):
        for char in range(len(strHanna)):
            name = strHanna[char].upper()

            #printing the output
            if char == len(strHanna)-1 :
                print(yellow, nameLetters[name][i])
            else :
                print(yellow, nameLetters[name][i],end="  ")

def userStar():
    letters = {
    'A': [' *** ', '*   *', '*****', '*   *', '*   *'],
    'B': ['**** ', '*   *', '**** ', '*   *', '**** '],
    'C': [' ****', '*    ', '*    ', '*    ', ' ****'],
    'D': ['**** ', '*   *', '*   *', '*   *', '**** '],
    'E': ['*****', '*    ', '*****', '*    ', '*****'],
    'F': ['*****', '*    ', '***  ', '*    ', '*    '],
    'G': [' ****', '*    ', '*  **', '*   *', ' ****'],
    'H': ['*   *', '*   *', '*****', '*   *', '*   *'],
    'I': ['*****', '  *  ', '  *  ', '  *  ', '*****'],
    'J': ['*****', '    *', '    *', '*   *', ' *** '],
    'K': ['*   *', '*  * ', '**   ', '*  * ', '*   *'],
    'L': ['*    ', '*    ', '*    ', '*    ', '*****'],
    'M': ['*   *', '** **', '* * *', '*   *', '*   *'],
    'N': ['*   *', '**  *', '* * *', '*  **', '*   *'],
    'O': [' *** ', '*   *', '*   *', '*   *', ' *** '],
    'P': ['**** ', '*   *', '**** ', '*    ', '*    '],
    'Q': [' *** ', '*   *', '*   *', '*  **', ' ** *'],
    'R': ['**** ', '*   *', '**** ', '*  * ', '*   *'],
    'S': [' ****', '*    ', '**** ', '    *', '**** '],
    'T': ['*****', '  *  ', '  *  ', '  *  ', '  *  '],
    'U': ['*   *', '*   *', '*   *', '*   *', ' *** '],
    'V': ['*   *', '*   *', '*   *', ' * * ', '  *  '],
    'W': ['*   *', '*   *', '* * *', '** **', '*   *'],
    'X': ['*   *', ' * * ', '  *  ', ' * * ', '*   *'],
    'Y': ['*   *', ' * * ', '  *  ', '  *  ', '  *  '],
    'Z': ['*****', '   * ', '  *  ', ' *   ', '*****'],
}
    userName = input("\n\033[1;32mEnter your name:\033[1;33m ")
    blue = "\033[1;36m"
    for i in range(5):
        for char in range(len(userName)):
            name = userName[char].upper()

            #printing the output
            if char == len(userName)-1 :
                print(blue, letters[name][i])
            else :
                print(blue, letters[name][i],end="  ")
def userChoice():
    userDisplay = "\n\033[1;32mType \033[1;33myes \033[1;32mif you want to try, Type \033[1;33mno \033[1;32mif you want to close the program:\n"
    for i in userDisplay:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.06),
    userInput=input("\033[1;33m")
    choice = userInput.upper()
    if choice=="YES":
        userStar()
        goodbye()
    else:
        goodbye()
    
def goodbye():
    bye = "\033[1;32mThank you for viewing \033[1;33mSTAR NAME\033[1;32m! \033[1;31m♡" # exit greeting
    for i in bye:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.06),
    print()


welcome()
nameStars()
userChoice()