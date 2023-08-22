from urllib.request import urlopen
import re
url = input('Enter - ')
html = urlopen(url)
total = 0
for i in html:
    y = i.decode().strip()
    x = re.findall('>([0-9]*[0-9])<+', y)
    for e in x:
        total = total + int(e)
print(total)
