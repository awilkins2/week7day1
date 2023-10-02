#working w apis and dictionaries

import requests
import json
response = requests.get("https://randomuser.me/api")

#print(response.json())

title = response.json()['results'][0]['name']['first']
print(title)
gender = response.json()['results'][0]['gender']
print(gender)
lastname = response.json()['results'][0]['name']['last']
print(lastname)
street = response.json()['results'][0]['location']['street']['name']
print(street)
postcode = response.json()['results'][0]['location']['postcode']
city = response.json()['results'][0]['location']['city']
state = response.json()['results'][0]['location']['state']
print(postcode)
print(state)
print(city)
email = response.json()['results'][0]['email']
print(email)