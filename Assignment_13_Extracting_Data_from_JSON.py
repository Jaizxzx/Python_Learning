import json
import urllib.request, urllib.parse, urllib.error
import js as js
link = input('Enter- ')
z = urllib.request.urlopen(link).read()
info = json.loads(z)
coun1 = 0
total = 0
for item in info['comments']:
    counting = item["count"]
    coun1 = coun1 + 1
    total = total + int(counting)
print(total)
print(coun1)
