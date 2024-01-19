import json

# Read the JSON data from the file using filePath
def readJson(filePath):
    with open(filePath, 'r') as file:
        data = json.load(file)
    return data

def insertJson(filePath, newData):
    # fetching the already available data from the json file using file path
    try:
        with open(filePath, 'r') as file:
            data = json.load(file)
    # if no json fle is found then the creating an empty list
    except:
        data = []
        print(f"file not found")

    # adding new dictionary data to the list 
    data.append(newData)
    # now finally inserting the data into the json file 
    try:
        with open(filePath, 'w') as file:
            json.dump(data, file, indent=2)
    except:
        print(f"Your score is not saved, Thank you ")