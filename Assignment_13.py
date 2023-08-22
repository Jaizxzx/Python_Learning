import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

api_key = False

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(html)
x = tree.findall('comments/comment')
total = 0
coun1 = 0
for counts in x:
    y = counts.find('count').text
    total = total + int(y)
    coun1 = coun1 + 1
print(total)
print(coun1)
