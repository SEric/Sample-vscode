import requests

r = requests.get("https://github.io")
print(r.status_code)
print(r.ok)