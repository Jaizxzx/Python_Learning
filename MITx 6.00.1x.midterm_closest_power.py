def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    smallest = 0
    list1 = list()
    for i in range(0,100,1 ):
        x = base**i
        y = abs(num - x)
        list1.append(y)
    #print(min(list1))
    z = min(list1)
    a = list1.index(z)
    return a
    #exponent = a
print(closest_power(4, 25))
