def readFile(name):
    with open(name + ".txt","r") as myFile:
        data = myFile.readlines()
    return data

def removeBS(listBS):
    newList = []
    for elem in listBS:
        newList.append(elem.rstrip())
    return newList

def createEmpLists(dataList):
    """Receives a list of strings. Each string is the information of an employee.
        Returns a list of lists, where each internal list is the information of an employee"""
    newList = []
    for empData in dataList:
        newList.append(empData.split("\t"))
    return newList

def createEmpListWFormat(dataList):
    """Receives a list of lists that have only strings. It will change the strings that are numbers,
        to integers. Returns this final list"""
    newList = []
    for empData in dataList:
        empID = int(empData[0])
        name = empData[1]
        salary = float(empData[2])
        numSales = int(empData[3])
        newList.append([empID,name,salary,numSales])
    return newList

def getEmployeesInfo():
    """Read the file of Employees and create a list ready to be used in this program"""
    dirtyData = readFile("Employees")
    #print(dirtyData)
    dataNoBS = removeBS(dirtyData)
    #print(dataNoBS)
    dataInLists = createEmpLists(dataNoBS)
    #print(dataInLists)
    finalEmpList = createEmpListWFormat(dataInLists[1:])
    #print(finalEmpList)
    return finalEmpList
