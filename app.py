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
    while True: 
        print(f"{Fore.MAGENTA}Welcome to the Quiz Game ! :) ")
        player = input(f"{Fore.BLUE}Enter your Player Name : ")
        if(len(player)!=0):
            while True:
                # displays all the available menu
                displayMenu.showMenu()
                # takes user input 
                userInput = getMenuOptions()
                spinner(1)
                # adding logic for showing questions and taking answer 
                if(userInput == "1"):
                    print(f"{Fore.CYAN} The questions are loading...")
                    spinner(1)
                    # displaying the question 
                    displayQuestions(database, scorePath, player)
                elif(userInput == "2"):
                    print(f"Fetching data from the database")
                    spinner(1)
                    # displaying the score 
                    showScore(player, scorePath)
                elif(userInput == "3"):
                    # displaying the top player 
                    showTopPlayer(scorePath)
                elif(userInput == '4'):
                    break
                else:
                    print(f"{Fore.RED}Invalid input option")
            break
        else:
            print("player name cannot be empty")