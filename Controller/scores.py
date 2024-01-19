from Model.json import insertJson
def saveScore(playerName, score, filePath):
    # storing the player information in a dictionary
    scoreData = {"playerName": playerName, "score": score}
    print(scoreData)
    #calling a function to store the created dictionary scoreData
    insertJson(filePath, scoreData)