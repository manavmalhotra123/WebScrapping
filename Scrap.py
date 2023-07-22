# fetching the data from the HTML content
# parse through the HTML content and filter it using your thing

# scrapping can be done using API and Web Scrapping tool called bs4

# step 1: install libraries
import requests
from bs4 import BeautifulSoup


# url pattern
url = "https://codewithharry.com"


# request to get the url
r = requests.get(url)
# fetching the content from the url 
htmlContent = r.content

# Parse the content using BeautifulSoup
soup = BeautifulSoup(htmlContent,'html.parser')

# fetching the title tag 
title = soup.title 
print(title) 
print(type(title))

# Fecthing the real data of the title tag
tiledata = title.string
print(tiledata) 


# Types of object in BeautifulSoup
# 1. Tag
# 2. NavigableString
# 3. BeautifulSoup
# 4. Comment