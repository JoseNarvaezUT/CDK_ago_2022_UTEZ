#!/bin/python3

import requests

API_URL = 'http://0.0.0.0:3000/saludo/Joselo'

#test GET request
response = requests.request("get",API_URL);

print(response.status_code)
print (response.text)

if response.status_code != 200:
    print ('Se activo fail')
    exit(1)
