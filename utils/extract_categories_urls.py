## A script to extract urls of all books categories from the website's homepage (https://books.toscrape.com/)

# Import relevant libraries
import requests
from bs4 import BeautifulSoup

# Define URL
url="http://books.toscrape.com/index.html"

# Extract every book category's url
def extract_categories_url(url):
    # Declare empty list
    # categories_urls = []
    # Create Soup object that will be parsed
    response = requests.get(url)
    # Parse the page
    soup = BeautifulSoup(response.content, 'html.parser')
    categories_urls = soup.find_all({'class': 'nav nav-list'})
    print(categories_urls)
    for link in categories_urls:
        url = link.find('a').get("href")
        # url = "http://books.toscrape.com/" + url[4:]
        # categories_urls.append(url)
    return categories_urls