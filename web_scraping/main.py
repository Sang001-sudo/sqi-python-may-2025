import requests
from bs4 import BeautifulSoup

url = "https://www.google.com"

try:
  res = requests.get(url).status_code
except:
  print('An exception occurred')
else:
    print(f"status code: {res}")