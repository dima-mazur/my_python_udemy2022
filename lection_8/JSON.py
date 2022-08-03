import json

import requests


class Tournamet:

    def __init__(self, name, year):
        self.name = name
        self.year = year


tournaments = {
    "Australian Open": 2010,
    'FIDE World Cup': 2018,
    'FIDE Grand Prix': 2016
}

json_data = json.dumps(tournaments, indent=2) # serialization
print(json_data)

loaded = json.loads(json_data) # deserialization
print(type(loaded))
print(loaded)

t1 = Tournamet('A_Open', 2020)

json_data = json.dumps(t1.__dict__)
print(json_data)

t = Tournamet(**json.loads(json_data))
print(t.name, t.year)

response = requests.post('https://httpbin.org/post', json=json_data)
json_response = response.json()
print(json_response['data'])