import json

# Read the JSON data from the file using filePath
def readJson(filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)
    return data