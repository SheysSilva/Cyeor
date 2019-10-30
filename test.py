import requests
import json

print('GET ONE ELEMENT')
get = requests.get('http://localhost:5000/chaves/25190908414996000193650120002072401001967168')
print(get.json())