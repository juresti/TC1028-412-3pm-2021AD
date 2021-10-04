import os
print(os.getcwd())
os.chdir("/Users/dr.jorge/Desktop")
print(os.getcwd())

def writeOneLine(fileName,line):
    myFile = open(fileName + ".txt","w")
    myFile.write(line)
    myFile.close()

def readOneLine(fileName):
    myFile = open(fileName + ".txt","r")
    info = myFile.readlines()
    myFile.close()
    
    cleanList = cleanBackSlash(info)
    print(cleanList)
    return cleanList

def writeTwoLines(fileName,line1,line2):
    myFile = open(fileName + ".txt","w")
    myFile.write(line1 + "\n")
    myFile.write(line2)
    myFile.close()

def cleanBackSlash(list):
    """Receives a list that has \n in its elements and returns a list without them"""
    newList = []
    for element in list:
        new = element.rstrip()
        newList.append(new)
    return newList

def addOnePerson(fileName,nameP,ID,listPeople):
    """Add a person to the file given"""
    newList = listPeople
    newList.append(nameP)
    newList.append(ID)
    
    listWB = []
    for element in newList:
        listWB.append(element + "\n")
    print(listWB)
    
    with open(fileName + ".txt","w") as myFile:
        myFile.writelines(listWB)
    return newList
    