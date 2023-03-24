def phonetic_approximant(recievedString):
    vecFile = open(r"cmudict-0.7b-simvecs", "Access_Mode")
    
#Debug
vecFile = open(r"cmudict-0.7b-simvecs", "r")
print(vecFile.read(1000))