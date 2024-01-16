import random
from Model.json import *
from Controller.userInput import *
from colorama import Fore, Style, init
init()

def displayQuestions(database):
    questions = readJson(database)
    
    score = 0
    numberOfQuestion = 3
    questionDisplayed = 0
    while questionDisplayed < numberOfQuestion:
        randomQuestions = random.choice(questions)
        print("Question:", randomQuestions['question'])
        print("Options:", ", ".join(randomQuestions["options"]))
        answer = getUserAnswer()
        if(answer == randomQuestions["answer"]):
            score += 1
        questionDisplayed += 1
    print(f"Your score is ", score)
