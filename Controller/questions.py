import random
from Model.json import *
from Controller.userInput import *
from colorama import Fore, Style, init
from Controller.spinner import *
init()

def displayQuestions(database):
    player = input("Enter your Player Name")
    questions = readJson(database)
    score = 0
    numberOfQuestion = 3
    questionDisplayed = 0
    while questionDisplayed < numberOfQuestion:
        randomQuestions = random.choice(questions)
        spinner(1)
        print("Question:", randomQuestions['question'])
        print("Options:", ", ".join(randomQuestions["options"]))
        answer = getUserAnswer()
        spinner(1)
        if(answer == randomQuestions["answer"]):
            score += 1
        questionDisplayed += 1
    print(player, f"your score is ", score)
    print(f"Returning to the main menu")
    spinner(1)
