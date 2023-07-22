import requests
from bs4 import BeautifulSoup
url = "https://codewithharry.com"

# Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content

# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent)

markup = "<p><!-- this is a comment --></p>"

# comment object type in beautiful soup 
soup2 = BeautifulSoup(markup)
print(soup2.p)       
print(soup2.p.string)  
print(type(soup2))     
