import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy import spatial
import re

MAX_INT = 100

vecFile = open("cmudict-0.7b-simvecs", "r")
fileLines = vecFile.readlines()
global vectorDict 
vectorDict = {}

global commandDict
commandDict = {}
    
for line in fileLines:
    elements = line.split(" ")
    lable = elements[0]
    vectorDict[lable] = np.array([])
    elements.remove(lable)
    elements.remove("")
    for vecValue in elements:
        vectorDict[lable] = np.append(vectorDict[lable], float(vecValue))
        
#debug
commandDict["HEAL ME"] = vectorDict["HEAL"] + vectorDict["ME"]
commandDict["SHIELD ME"] = vectorDict["SHIELD"] + vectorDict["ME"]
commandDict["Q ONE"] = vectorDict["Q"] + vectorDict["ONE"]
commandDict["Q TWO"] = vectorDict["Q"] + vectorDict["TWO"]
commandDict["Q THREE"] = vectorDict["Q"] + vectorDict["THREE"]
commandDict["Q FOUR"] = vectorDict["Q"] + vectorDict["FOUR"]
commandDict["Q FIVE"] = vectorDict["Q"] + vectorDict["FIVE"]
commandDict["Q SIX"] = vectorDict["Q"] + vectorDict["SIX"]
commandDict["Q SEVEN"] = vectorDict["Q"] + vectorDict["SEVEN"]
commandDict["Q EIGHT"] = vectorDict["Q"] + vectorDict["EIGHT"]
commandDict["Q NINE"] = vectorDict["Q"] + vectorDict["NINE"]
commandDict["Q TEN"] = vectorDict["Q"] + vectorDict["TEN"]
commandDict["Q ELEVEN"] = vectorDict["Q"] + vectorDict["ELEVEN"]
commandDict["Q TWELVE"] = vectorDict["Q"] + vectorDict["TWELVE"]
commandDict["R ONE"] = vectorDict["R"] + vectorDict["ONE"]
commandDict["R TWO"] = vectorDict["R"] + vectorDict["TWO"]
commandDict["R THREE"] = vectorDict["R"] + vectorDict["THREE"]
commandDict["R FOUR"] = vectorDict["R"] + vectorDict["FOUR"]
commandDict["R FIVE"] = vectorDict["R"] + vectorDict["FIVE"]
commandDict["R SIX"] = vectorDict["R"] + vectorDict["SIX"]
commandDict["R SEVEN"] = vectorDict["R"] + vectorDict["SEVEN"]
commandDict["R EIGHT"] = vectorDict["R"] + vectorDict["EIGHT"]
commandDict["R NINE"] = vectorDict["R"] + vectorDict["NINE"]
commandDict["R TEN"] = vectorDict["R"] + vectorDict["TEN"]
commandDict["R ELEVEN"] = vectorDict["R"] + vectorDict["ELEVEN"]
commandDict["R TWELVE"] = vectorDict["R"] + vectorDict["TWELVE"]
commandDict["ALT ONE"] = vectorDict["ALT"] + vectorDict["ONE"]
commandDict["ALT TWO"] = vectorDict["ALT"] + vectorDict["TWO"]
commandDict["ALT THREE"] = vectorDict["ALT"] + vectorDict["THREE"]
commandDict["ALT FOUR"] = vectorDict["ALT"] + vectorDict["FOUR"]
commandDict["ALT FIVE"] = vectorDict["ALT"] + vectorDict["FIVE"]
commandDict["ALT SIX"] = vectorDict["ALT"] + vectorDict["SIX"]
commandDict["ALT SEVEN"] = vectorDict["ALT"] + vectorDict["SEVEN"]
commandDict["ALT EIGHT"] = vectorDict["ALT"] + vectorDict["EIGHT"]
commandDict["ALT NINE"] = vectorDict["ALT"] + vectorDict["NINE"]
commandDict["ALT TEN"] = vectorDict["ALT"] + vectorDict["TEN"]
commandDict["ALT ELEVEN"] = vectorDict["ALT"] + vectorDict["ELEVEN"]
commandDict["ALT TWELVE"] = vectorDict["ALT"] + vectorDict["TWELVE"]
commandDict["FOLLOW ME"] = vectorDict["FOLLOW"] + vectorDict["ME"]
commandDict["STOP FOLLOWING"] = vectorDict["STOP"] + vectorDict["FOLLOWING"]
commandDict["RECALL"] = vectorDict["RECALL"]
commandDict["BASE"] = vectorDict["BASE"]
commandDict["BACK"] = vectorDict["BACK"]
commandDict["WARD HERE"] = vectorDict["WARD"] + vectorDict["HERE"]
commandDict["BE TOXIC"] = vectorDict["BE"] + vectorDict["TOXIC"]
commandDict["CHIT CHAT"] = vectorDict["CHIT"] + vectorDict["CHAT"]
commandDict["SAY SOMETHING"] = vectorDict["SAY"] + vectorDict["SOMETHING"]
commandDict["LEVEL UP Q"] = vectorDict["LEVEL"] + vectorDict["UP"] + vectorDict["Q"]
commandDict["LEVEL UP W"] = vectorDict["LEVEL"] + vectorDict["UP"] + vectorDict["W"]
commandDict["LEVEL UP E"] = vectorDict["LEVEL"] + vectorDict["UP"] + vectorDict["E"]
commandDict["LEVEL UP R"] = vectorDict["LEVEL"] + vectorDict["UP"] + vectorDict["R"]
commandDict["LEVEL ALT"] = vectorDict["LEVEL"] + vectorDict["ALT"]
commandDict["LEVEL UP"] = vectorDict["LEVEL"] + vectorDict["UP"]
commandDict["IGNITE"] = vectorDict["IGNITE"]
commandDict["EXHAUST"] = vectorDict["EXHAUST"]
commandDict["LOCK SCREEN"] = vectorDict["LOCK"] + vectorDict["SCREEN"]

#QoL - Null commands
commandDict["ONE"] = vectorDict["ONE"]
commandDict["TWO"] = vectorDict["TWO"]
commandDict["THREE"] = vectorDict["THREE"]
commandDict["FOUR"] = vectorDict["FOUR"]
commandDict["FIVE"] = vectorDict["FIVE"]
commandDict["SIX"] = vectorDict["SIX"]
commandDict["SEVEN"] = vectorDict["SEVEN"]
commandDict["EIGHT"] = vectorDict["EIGHT"]
commandDict["NINE"] = vectorDict["NINE"]
commandDict["TEN"] = vectorDict["TEN"]
commandDict["ELEVEN"] = vectorDict["ELEVEN"]
commandDict["TWELVE"] = vectorDict["TWELVE"]
commandDict["Q"] = vectorDict["Q"]
commandDict["R"] = vectorDict["R"]

nullCommands = ["ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "ELEVEN", "TWELVE", "R", "Q"]

def phonetic_approximant(recievedString):
    recievedString = recievedString.upper()
    splitString = recievedString.split(" ")
    #debug
    print(splitString)
    indexEnd = len(splitString) - 1
    #splitString[indexEnd] = splitString[indexEnd].rstrip(".")
    splitString.pop(0) #Pop the Author
    splitString.pop(0) #Pop the Space ''
    recievedVector = np.zeros(50)
    smallest_cos_sim = 1000
    matchingCommand = ""
    
    for word in splitString:
        print(word)
        word = word.rstrip(".,-")
        if word in vectorDict:
            wordVector = vectorDict[word]
            recievedVector = np.add(recievedVector, wordVector)
        
    for key in commandDict:
        commandVector = commandDict[key]
        cos_sim = spatial.distance.cosine(recievedVector, commandVector)
        if cos_sim < smallest_cos_sim:
            smallest_cos_sim = cos_sim
            matchingCommand = key
    

    if matchingCommand in nullCommands:
        smallest_cos_sim = MAX_INT
    return (matchingCommand, smallest_cos_sim)
    
    
    
#Debug
#in the format: Word, 50 vector values
#test = "**Entr0py**: Kill me."
#recievedString = test.upper()
#splitString = recievedString.split(" ")
#print(splitString)
#indexEnd = len(splitString) - 1
#print(indexEnd)
#splitString[indexEnd] = splitString[indexEnd].rstrip('.')
#print(splitString.pop(0))
#print(splitString)
#print(phonetic_approximant(test))