import requests
import json
import os

city = input('Enter the name of the city\n')

url = f'https://api.weatherapi.com/v1/current.json?key=9cab33a9752042648d131123233103&q={city}'

r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
print(wdic['current']['temp_c'])


#the below line will work in MAC OS
# os.system(f"say 'The current weather in {city} is {w} degrees'")
