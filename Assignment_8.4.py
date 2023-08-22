fname = input("Enter file name: ")
fh = open(fname)
st = list()
for line in fh:
    line.rstrip()
    x = line.split()
    for y in x:
        if y in st:
            continue
        else:
            st.append(y)
st.sort()
print(st)
