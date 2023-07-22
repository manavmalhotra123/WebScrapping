import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

r = requests.get(url)

content = r.content

soup = BeautifulSoup(content, 'html.parser')

anchors = soup.find_all('a')

all_links = set()
# Getting all the links from the website page and storing them in a set for uniqueness
for link in anchors:
    href = link.get('href')
    if href and href != "#":
        all_links.add(href)
        print(href)
