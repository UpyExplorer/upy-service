import requests

url = "http://localhost:8080/ads_links/1"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
