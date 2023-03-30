import numpy as np

vecFile = open("cmudict-0.7b-simvecs", "r")
fileLines = vecFile.readlines()
vectorDict = {}
    
for line in fileLines:
    elements = line.split(" ")
    lable = elements[0]
    vectorDict[lable] = np.array([])
    elements.remove(lable)
    elements.remove("")
    for vecValue in elements:
        vectorDict[lable] = np.append(vectorDict[lable], float(vecValue))

def phonetic_approximant(recievedString):
    recievedString = recievedString.upper()
    splitString = recievedString.split(" ")
    commandVector = np.zeros(50)
    
    for word in splitString:
        wordVector = vectorDict[word]
        commandVector = np.add(commandVector, wordVector)
        
    cos_sim = dot(commandVector, wordVector)/(norm(commandVector)*norm(wordVector))
    
#Debug
#in the format: Word, 50 vector values
