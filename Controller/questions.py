from rich.console import Console
from rich.table import Table
import random
from Model.json import *
from Controller.userInput import *
from colorama import Fore, Style, init
from Controller.spinner import *
from Controller.scores import saveScore
init()
console = Console()
def displayQuestions(database, scorePath):
    player = input("Enter your Player Name")
    questions = readJson(database)
    score = 0
    numberOfQuestion = 3
    questionDisplayed = 0
    while questionDisplayed < numberOfQuestion:
        randomQuestions = random.choice(questions)
        # displaying spinner before the question load
        spinner(1)
        # printing the quiz questions one by one in each loop
        print("Question:", randomQuestions['question'])
        # printing the answer option in a table
        option = 1
        i = 0
        answer = randomQuestions['options']
        table = Table(title="Select you answer")
        table.add_column("Options", style="cyan", justify="center")
        table.add_column("Answer", style="yellow")
        while i < len(randomQuestions['options']):
            # displaying the answer in the table. rich table do not support the intiger value so converting int to str 
            table.add_row(str(option), answer[i])
            option += 1
            i += 1
        console.print(table)
        #adding validation to the user input 
        while True:
            try:
                #getting the user Answer.
                answer = int(getUserAnswer())
                break
            except:
                print(f"Please enter the option for the answer")
        #displaying spinner after each Questions
        spinner(1)
        if(randomQuestions['options'][answer-1] == randomQuestions["answer"]):
            score += 1
        questionDisplayed += 1
    print(f"Calculationg the score")
    spinner(2)
    print(player, f"your score is ", score)
    saveScore(player, score, scorePath)
    print(f"Returning to the main menu")
    spinner(1)
