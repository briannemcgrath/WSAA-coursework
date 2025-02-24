import requests
import json 

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/CSV/1.0/en"
response = requests.get(url)
data = response.text

with open ('cso.json', 'w') as f:
    f.write(data)