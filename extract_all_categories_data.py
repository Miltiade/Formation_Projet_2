# Import relevant libraries
import requests
import csv
from bs4 import BeautifulSoup

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

# Define function to scrape data
def scrape_data(product_page_url):
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
    values.append(scrape_data(url))

with open("data_produit.csv","w") as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(header)
    csv_writer.writerows(values)

# Setup loop to scrape data from all pages:
while soup.find('li', {'class': 'next'}):
    next_url = soup.find('li', {'class': 'next'}).find('a').get('href')
    url = "/".join(url.split('/')[:-1]) + '/' + next_url
    response = requests.get(url)

print("Data has been scraped and written to csv file.")