largest = 0
smallest = 0
num = input("Enter a number: ")
try :
    x = int(num)
    while True :
        continue
    while False :
        if largest < x:
            largest = x
        if smallest > x :
            smallest = x
        elif num == "done":
            print("Maximum is", largest)
            print("Minimum is", smallest)
        else :
            print("Invalid input")
