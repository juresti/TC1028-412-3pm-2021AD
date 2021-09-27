def listP(numPer):
    myList = []
    for veces in range(numPer):
        name = input(f"{veces + 1}. Tell me the name: ")
        myList.append(name)
    return myList

def printPersons(listP):
    for person in listP:
        print(person)
        
def menuPer():
    print("\nWelcome to people manager")
    print("1) Input people first time")
    print("2) Add people to previous list")
    print("3) Print people")
    print("4) Quit")
    op = int(input("Enter option: "))
    return op

def updateListP(listP):
    op = input("Add a name? (Yes/no) ")
    while (op.lower() == "yes"):
        name = input("Tell me the name: ")
        listP.append(name)
        op = input("Add a name? (Yes/no) ")
    return listP

def peopleManager():
    opt = 0
    listPeople = []
    while (opt != 4):
        opt = menuPer()
        if (opt == 1):
            numP = int(input("How many would you capture? "))
            listPeople = listP(numP)
        elif (opt == 2):
            listPeople = updateListP(listPeople)
        elif (opt == 3):
            printPersons(listPeople)
        elif (opt == 4):
            print("Bye bye")
        else:
            print("ERROR: valid values are 1, 2, 3 and 4")
            
#peopleManager()


def listWithTuple(numP):
    data = []
    for num in range(1,numP + 1):
        name = input(f"Give the name {num}: ")
        age = int(input(f"Give the age {num}: "))
        data.append((name,age))
    return data


def onlyAges(dataList):
    ages = []
    for personData in dataList:
        age = personData[1]
        ages.append(age)
    return ages






