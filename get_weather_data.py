import requests


API_KEY = "7d4d4878-78f0-4520-8106-b8dafd61a9f8"
payload = {
    "q": "bangkok",
    "appid": API_KEY,
    "units": "metric"
}
url = "http://api.airvisual.com/v2"
response = requests.get(url, params=payload)
print(response.url)

data = response.json()
print(data)