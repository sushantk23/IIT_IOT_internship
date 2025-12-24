import requests

url = "http://127.0.0.1:5000/submit"
data = {
    "temperature": 27.5,
    "light": 320
}

response = requests.post(url, json=data)
print(response.json())