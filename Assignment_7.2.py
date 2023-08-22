# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
a = 0.0
y = 0.0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        a = a + 1.0
        x = line[19:]
        b = float(x)
        y = y + b
        continue
    else:
        continue
print("Average spam confidence:", y/a)
