import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy import spatial

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
commandDict["APPLE"] = vectorDict["APPLE"]
commandDict["SILENCE"] = vectorDict["SILENCE"]


def phonetic_approximant(recievedString):
    recievedString = recievedString.upper()
    splitString = recievedString.split(" ")
    recievedVector = np.zeros(50)
    smallest_cos_sim = 1000
    matchingCommand = ""
    
    for word in splitString:
        wordVector = vectorDict[word]
        recievedVector = np.add(recievedVector, wordVector)
    
    for key in commandDict:
        commandVector = commandDict[key]
        cos_sim = spatial.distance.cosine(recievedVector, commandVector)
        if cos_sim < smallest_cos_sim:
            smallest_cos_sim = cos_sim
            matchingCommand = key
            
    return (matchingCommand, smallest_cos_sim)
    
    
    
#Debug
#in the format: Word, 50 vector values
print(commandDict["SILENCE"])
print(phonetic_approximant("DIAMONDS"))