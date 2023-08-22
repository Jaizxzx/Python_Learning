from urllib.request import urlopen
import re
from bs4 import BeautifulSoup
url = input('Enter - ')
html = urlopen(url)
total = 0
soup = BeautifulSoup(html, "html.parser")
for i in soup:
    y = i.decode().strip()
    x = re.findall('>([0-9]*[0-9])<+', y)
    for e in x:
        total = total + int(e)
print(total)
