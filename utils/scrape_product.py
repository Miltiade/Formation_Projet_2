# A function to scrape data from a single book's webpage

import requests
from bs4 import BeautifulSoup

def scrape(product_page_url):
    # product_page_url
    response = requests.get(product_page_url)
    book = BeautifulSoup(response.content, 'html.parser')
    # universal_ product_code (upc)
    universal_product_code = book.find("table", class_="table table-striped").find("td").text
    # title
    div = book.find("div", class_="product_main")
    title = div.find("h1").text
    # price_including_tax
    table = book.find("table", class_="table table-striped")
    table_td = table.find_all("td")
    price_including_tax = table_td[3].text
    # price_excluding_tax
    price_excluding_tax = table_td[2].text
    # number_available
    number_available = table_td[5].text
    # product_description
    product_description = book.find_all("p")[3].text
    # category
    category = book.find_all("a")[3].text
    # review_rating
    review_rating = div.find("p", class_="star-rating").attrs["class"][1]
    # image_url
    image_url = book.find("img").attrs["src"]
    # Declare return value
    return [
        product_page_url,
        universal_product_code,
        title,
        price_including_tax,
        price_excluding_tax,
        number_available,
        product_description,
        category,
        review_rating,
        image_url,
    ]

# TESTING THE FUNCTION ON A SPECIFIC URL:
# product_page_url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
# result = scrape(product_page_url)
# print(result)