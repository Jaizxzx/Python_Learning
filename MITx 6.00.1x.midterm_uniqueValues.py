def uniqueValues(aDict):
    key1 = []
    key2 = {}

    for key in list(aDict.keys()):
        key2[aDict[key]] = key2.get(aDict[key], 0) + 1
    for keyInkey2 in key2.keys():
        if key2[keyInkey2] == 1:
            for keyinaDict in aDict.keys():
                if aDict[keyinaDict] == keyInkey2:
                    key1.append(keyinaDict)
    print(key2)
    return sorted(key1)
uniqueValues({1: 1, 2: 1, 3: 1})