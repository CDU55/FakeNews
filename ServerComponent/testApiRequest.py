import requests

BASE = "http://127.0.0.1:5000/"
html_body = "https://mobile.twitter.com/pinkfloyd/status/1325772237341945858"

response = requests.post(BASE, {"html": html_body})
print(response.json())
