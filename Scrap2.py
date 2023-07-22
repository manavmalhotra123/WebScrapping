import requests
from bs4 import BeautifulSoup

# url pattern
url = "https://codewithharry.com"

r = requests.get(url)

content = r.content

soup = BeautifulSoup(content,'html.parser')

# Fetching the content of the title tag of the page
title = soup.title.string
print(title)

# Fetching all the paragraphs of the page 
paras = soup.find_all('p') # list of paragraphs of the page
links = soup.find_all('a') # list of all the link tags of the page

print(type(paras)) # result set 

# getting the classes of the paragraphs
classes = soup.find('p')['class']
print(classes)


# find all the elements of class lead
print(soup.find_all('p',class_ ="mt-2"))

# get the text from the elements/tags/soups
# print(soup.find('p').get_text())

# fetching all the text of the html page 
# print(soup.get_text())