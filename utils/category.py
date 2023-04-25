# Import relevant libraries
import requests
from bs4 import BeautifulSoup
from utils.product import scrape as scrape_product
from utils.csv import generate as generate_csv

# Define URL
url = "http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html"

# Declare empty list
books = []

# Create Soup object that will be parsed
response = requests.get(url)

# Parse the page
soup = BeautifulSoup(response.content, 'html.parser')
books += soup.find_all('article', {'class': 'product_pod'})
# Parse the next pages
while soup.find('li', {'class': 'next'}):
    next_url = soup.find('li', {'class': 'next'}).find('a').get('href')
    url = "/".join(url.split('/')[:-1]) + '/' + next_url
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    books += soup.find_all('article', {'class': 'product_pod'})

# Call function and write data to csv file
header = [
    "product_page_url",
    "universal_product_code",
    "title",
    "price_including_tax",
    "price_excluding_tax",
    "number_available",
    "product_description",
    "category",
    "review_rating",
    "image_url",
    ]
values = []
for link in books:
    url = link.find('a').get("href")
    url = "http://books.toscrape.com/catalogue/" + url[9:]
    values.append(scrape_product(url))

generate_csv(header, values, "nonfiction.csv")

# Setup loop to scrape data from all pages:
while soup.find('li', {'class': 'next'}):
    next_url = soup.find('li', {'class': 'next'}).find('a').get('href')
    url = "/".join(url.split('/')[:-1]) + '/' + next_url
    response = requests.get(url)

print("Data has been scraped and written to csv file.")