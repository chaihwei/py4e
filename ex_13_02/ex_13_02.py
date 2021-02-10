import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = 'Malayer Azad University'
params = dict()
params['address'] = address
if api_key is not False: params['key'] = api_key
url = serviceurl + urllib.parse.urlencode(params)

print('Retrieving url:', url)
uhand = urllib.request.urlopen(url, context=ctx)
data = uhand.read().decode()
print('Retrieved', len(data), 'characters')
info = json.loads(data)

print(info['results'][0]['place_id'])