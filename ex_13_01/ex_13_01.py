import urllib.request, urllib.parse, urllib.error
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1049867.json'
uhand = urllib.request.urlopen(url, context=ctx)
data = uhand.read().decode()
info = json.loads(data)
gross = list()
# print(info['note'])

for item in info['comments']:
    gross.append(int(item['count']))

print(sum(gross))