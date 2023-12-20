import requests

data = {
    "value": 0.5,
    "id": 1
    }
response = requests.post(url="http://127.0.0.1:8000/api/add-point", data=data)
print(response)