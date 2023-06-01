"""A script to extract URLs of all books categories from the website's homepage (https://books.toscrape.com/)"""

# Import relevant libraries
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "http://books.toscrape.com/index.html"

# Extract every book category's url
def extract_categories_url(url):
    # Declare empty list
    categories_urls = []
    # Create Soup object that will be parsed
    response = requests.get(url)
    # Parse the page
    soup = BeautifulSoup(response.content, "html.parser")

    sidebar = soup.find("div", class_="side_categories")  # Find the sidebar element

    category_links = sidebar.find_all("a")  # Find all the category links

    for link in category_links:
        category_url = urljoin(
            url, link["href"]
        )  # Construct the full URL using urljoin
        categories_urls.append(category_url)

    return categories_urls
category_urls = extract_categories_url(url)

# TESTING THE FUNCTION ON THE HOMEPAGE URL:
# url = "http://books.toscrape.com/index.html"
# result = extract_categories_url(url)
# print(result)
