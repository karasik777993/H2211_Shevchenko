import requests


response = requests.get("https://http.org/get")
print(response.content)
print(f"Data type - {type(response.text)}")