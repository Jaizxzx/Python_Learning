import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup('a')
lost = list()
for tag in tags:
    x = tag.get('href', None)
    z = lost.append(x)
q = lost[17]
html = urllib.request.urlopen(q, context=ctx).read()
sup = BeautifulSoup(html, 'html.parser')
tat = sup('a')
lest = list()
for m in tat:
    o = m.get('href', None)
    lest.append(o)
r = lest[17]
html = urllib.request.urlopen(r, context=ctx).read()
sep = BeautifulSoup(html, 'html.parser')
tmt = sep('a')
list4 = list()
for u in tmt:
    w = u.get('href', None)
    mnm = list4.append(w)
rt = list4[17]
html = urllib.request.urlopen(rt, context=ctx).read()
sp = BeautifulSoup(html, 'html.parser')
tt = sp('a')
list5 = list()
for ui in tt:
    we = ui.get('href', None)
    mmm = list5.append(we)
rr = list5[17]
html = urllib.request.urlopen(rr, context=ctx).read()
spp = BeautifulSoup(html, 'html.parser')
ttt = spp('a')
list6 = list()
for uuu in ttt:
    www = uuu.get('href', None)
    qqq = list6.append(www)
miui = list6[17]
html = urllib.request.urlopen(miui, context=ctx).read()
ssp = BeautifulSoup(html, 'html.parser')
tttt = ssp('a')
list7 = list()
for qwe in tttt:
    uueue = qwe.get('href', None)
    sss = list7.append(uueue)
zxzx = list7[17]
html = urllib.request.urlopen(zxzx, context=ctx).read()
sp = BeautifulSoup(html, 'html.parser')
ttttt = sp('a')
list8 = list()
for zaza in ttttt:
    aqaq = zaza.get('href', None)
    rtrt = list8.append(aqaq)
pol = list8[17]
print(pol)
