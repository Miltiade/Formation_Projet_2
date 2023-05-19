# A function that scrapes, from a Books category page, all the books' requested data

import requests
from bs4 import BeautifulSoup
from utils.scrape_product import scrape as scrape_product

def scrape_category(url):  
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
    values = []
    for link in books:
        url = link.find('a').get("href")
        url = "http://books.toscrape.com/catalogue/" + url[9:]
        values.append(scrape_product(url))
    return values

# TESTING THE FUNCTION ON A SPECIFIC URL:
# url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
# result = scrape_category(url)
# print(result)