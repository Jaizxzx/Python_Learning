def isPalindrome(aString):
    z = str(aString)
    rev=""
    x = len(z)
    while x > 0:
        rev += z[x-1]
        x = x - 1
    if rev == z:
        return True
        #print('True')
    else:
        return False
        #print('False')
x = isPalindrome('oho')