flocation = input('Enter the name of the file:')
fhandle = open(flocation)
q = fhandle.read()
import re
x = re.findall('[0-9]+', q)
total = 0
for i in x:
    total = total + int(i)
print(total)
