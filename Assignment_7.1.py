# Use words.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
z = fh.read()
x = z.strip()
print(x.upper())
