name = input("Enter file:")
handle = open(name)
directory = dict()
lost = list()
for line in handle:
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        line = line.split()
        x = line[1]
        lost.append(x)
        directory[x] = directory.get(x,0) + 1
    if len(line) == 0: continue
largest = None
correspond = None
for k,v in directory.items():
    if largest is None or largest < v:
        largest = v
        correspond = k
print(correspond,largest)
