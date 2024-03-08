import requests

apiUrl = 'https://webexapis.com/v1/rooms'
access_token = 'ZWY0NGRkOTMtOTQ4OS00MDA2LTg4MTItMTQ1NTAxOGE2ZTI0ZTIwODUwZTAtNzYx_PF84_505dfc47-94b2-4c0b-9375-52de70df59bc'

httpHeaders = { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + access_token }
queryParams = { 'sortBy': 'lastactivity', 'max': '2' }

response = requests.get( url = apiUrl, headers = httpHeaders, params = queryParams )

print( response.status_code )
print( response.text )