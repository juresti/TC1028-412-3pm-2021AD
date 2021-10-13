def getRole():
    """Function with read a file and convert it to a list of lists with information of every person"""
    with open("Role.txt","r") as myFile:
        dataString = myFile.readlines()
    
    dataNoBS = []
    for person in dataString:
        noBS = person.rstrip()
        dataNoBS.append(noBS.split(","))
    
    finalData = []
    for person in dataNoBS:
        name = person[0]
        num = int(person[1])
        finalData.append([name,num])
        
    return finalData
   
def updateRole(name,role):
    """Receives the name of a person and it updates its information the role received.
        Returns the updated role"""
    index = 0
    found = False
    for register in role:
        if name in register:
            role[index][1] += 1
            found = True
            break
        index += 1
    
    if not found:
        role.append([name,1])
    
    return role

def writeRoleInFile(role):
    """Receivea a list of lists with the role.
        Converts the role to a list of strings
        Writes to the fiel the converted list"""
    finalList = []
    for personData in role:
        newSt = personData[0] + ","
        newSt += str(personData[1]) + "\n"
        finalList.append(newSt)
    
    with open("Role.txt","w") as myFile:
        myFile.writelines(finalList)
        print("File Written to disk")
    
    

def main():
    data = getRole()
    name = input("Tell me the name of the person to update: ")
    data = updateRole(name,data)
    writeRoleInFile(data)
    