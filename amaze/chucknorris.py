import requests
thetruth = requests.get("http://api.icndb.com/jokes/random?exclude=explicit").json()['value']['joke']
print(thetruth)

