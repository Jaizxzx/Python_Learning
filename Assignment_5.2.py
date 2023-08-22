largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        x = int(num)
        if largest is None or x > largest:
            largest = x
        if smallest is None or smallest > x:
            smallest = x
    except:
        print("Invalid input")
        continue
print("Maximum is", largest)
print("Minimum is", smallest)
