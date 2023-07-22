import requests
from bs4 import BeautifulSoup
url = "https://www.codewithharry.com/videos/python-web-scraping-tutorial-in-hindi"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup)