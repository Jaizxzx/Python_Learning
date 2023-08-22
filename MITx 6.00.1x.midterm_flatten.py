def flatten(aList):
    newList = []
    for i in aList:
        if type(i) != type([]):
            newList.append(i)
        else:
            newList.extend(flatten(i))
    return newList
