from Model.json import insertJson
from Model.json import readJson
from datetime import datetime

def saveScore(playerName, score, filePath):
    # creating a date and time string to record the score according to date and time
    date = datetime.now()
    year = date.year
    month = date.month
    day = date.day
    hour = date.hour
    min = date.minute
    sec = date.second

    currentDatetime = f"{year}-{month}-{day}-{hour}-{min}-{sec}"
    # storing the player information in a dictionary
    scoreData = {"playerName": playerName, "score": score, "date": currentDatetime}
    #calling a function to store the created dictionary scoreData
    insertJson(filePath, scoreData)

def showScore(name, filePath):
    # fetching data from the score.json file 
    data = readJson(filePath)
    allInfo = []
    # Searching the data using the playerName
    for playerInfo in data:
        if(playerInfo["playerName"] == name):
            allInfo.append(playerInfo)
    
    if allInfo: #checks if allInfo is empty or not
            for entry in allInfo:
                print(f"{entry['playerName']} your score on {entry['date']} was {entry['score']}")


def showTopPlayer(filePath):
    # fetching the data from score.js
    data = readJson(filePath)

    # creating an empty dictionary to store the information of the highest score player
    topPlayer = {}

    for player in data:
        score = player['score']
        playerName = player['playerName']
        
        # checking if player is already in the dictionary and if the new score is greater or equal
        if playerName in topPlayer:
            if score < topPlayer[playerName]['score']:
                continue  # skip this entry if the new score is not greater
            elif score == topPlayer[playerName]['score']:
                # If scores are equal, compare dates and update if the new entry is more recent
                if player['date'] <= topPlayer[playerName]['date']:
                    continue  # skip this entry if the new entry is not more recent

        # adding the playerName, score, and date in topPlayer dictionary
        topPlayer[playerName] = {'score': score, 'date': player['date']}
    print(f"The top Players are as follows")
    # printing the player with the highest score and their corresponding score
    for playerName, playerData in topPlayer.items():
        print(f"{playerName} scored {playerData['score']} on {playerData['date']}")

