name = input("Enter file:")
handle = open(name)
lost = list()
directory = dict()
for line in handle:
    if line.startswith('From:'):
        continue
    if line.startswith('From'):
        line = line.split()
        x = line[5]
        x = x.split(':')
        y = x[0]
        directory[y] = directory.get(y,0) + 1
        lost.append(y)
    if len(line) == 0: continue
q = sorted(directory.items())
for k,v in q:
    print(k , v)
