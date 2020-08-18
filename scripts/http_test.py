import requests

url = "https://api.exchangerate-api.com/v4/latest/USD"
response = requests.get(url)
print("Type = {}, Value = {}".format(type(response), response))

print("Json = {}".format(response.json()))