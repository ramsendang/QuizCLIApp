from colorama import Fore, Style, init
from Controller.spinner import spinner
from Controller.userInput import *
from Controller.questions import *
from Controller.scores import showScore
from Controller.scores import showTopPlayer
init()
from Controller.menu import menu
if __name__ == "__main__":
    database = "database.json"
    scorePath ="score.json"
    displayMenu = menu()
    print(f"{Fore.MAGENTA}Welcome to the Quiz Game ! :) ")
    player = input(f"{Fore.BLUE}Enter your Player Name : ")
    while True:
        print(f"{Fore.GREEN} Menus are loading ..")
        spinner(2) #displays the spinner for 2 sec
        # displays all the available menu
        displayMenu.showMenu()
        # takes user input 
        userInput = getMenuOptions()
        spinner(1)
        # adding logic for showing questions and taking answer 
        if(userInput == "1"):
            print(f"{Fore.CYAN} The questions are loading...")
            spinner(1)  
            displayQuestions(database, scorePath, player)
        elif(userInput == "2"):
            print(f"Fetching data from the database")
            spinner(1)
            showScore(player, scorePath)
        elif(userInput == "3"):
            showTopPlayer(scorePath)
        elif(userInput == '4'):
            break
        else:
            print(f"{Fore.RED}Invalid input option")