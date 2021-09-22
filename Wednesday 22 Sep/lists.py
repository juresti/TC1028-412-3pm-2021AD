def listP(numPer):
    myList = []
    for veces in range(numPer):
        name = input(f"{veces + 1}. Tell me the name: ")
        myList.append(name)
    return myList
