def getSublists(L, n):
    list1 = []
    for i in range(len(L) - n + 1):
        list1.append(L[i:i+n])
    print(list1)
getSublists([10, 4, 6, 8, 3, 4, 5, 7, 7, 2],4)