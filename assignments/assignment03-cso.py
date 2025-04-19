import requests
import json 

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/1.0/en"
response = requests.get(url)
data = response.json()

with open ('cso.json', 'w') as f:
    json.dump(data,f)