import requests
import json

url = "https://infuser.odcloud.kr/oas/docs?namespace=15115720/v1"

response = requests.get(url)
response.raise_for_status()

data = response.json()
print(data['info']['version'])
