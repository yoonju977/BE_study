import requests
from bs4 import Beautifulsoup

url = "https://naver.com"

req = requests.get(url)
print(req)

html = req.text
print(html)
