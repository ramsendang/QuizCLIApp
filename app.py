from colorama import Fore, Style, init
from Controller.spinner import spinner
from Controller.userInput import *
from Controller.questions import *
init()
from Controller.menu import menu
if __name__ == "__main__":
    database = "database.json"
    displayMenu = menu()
    while True:
        print(f"{Fore.MAGENTA}Welcome to the Quiz Game ! :) ")
        print(f"{Fore.GREEN} Menus are loading ..")
        spinner(2) #displays the spinner for 2 sec
        # displays all the available menu
        displayMenu.showMenu()
        # takes user input 
        userInput = getMenuOptions()
        spinner(1)
        if(userInput == "1"):
            print(f"{Fore.GREEN} The questions are loading...")
            spinner(1)
            displayQuestions(database)
        elif(userInput == "4"):
            break