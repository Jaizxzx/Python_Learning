y = 0
z = 0.0
while True:
    x = input("Enter a Number")
    if x == 'done':
        break
    try :
        a = float(x)
    except:
        print("Invalid input")
        continue
    y = y + 1
    z = a + z
print(z , y , z/y)
