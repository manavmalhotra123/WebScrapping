import requests
from bs4 import BeautifulSoup

url = "https://codewithharry.com"

r = requests.get(url)

content = r.content

soup = BeautifulSoup(content,'html.parser')


anchors = soup.find_all('a')
# Getting all the links from the website page 
for link in anchors:
    print(link.get('href'))

