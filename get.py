import requests

url = "http://myui.uiowa.edu"
r = requests.get(url)
print(r.text)

with open("test.txt") as f:
    contents = f.readlines()
