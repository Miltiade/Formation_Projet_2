import requests
import csv
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html"

books = []

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
books += soup.find_all('article', {'class': 'product_pod'})
while soup.find('li', {'class': 'next'}):
    next_url = soup.find('li', {'class': 'next'}).find('a').get('href')
    url = "/".join(url.split('/')[:-1]) + '/' + next_url
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')
    books += soup.find_all('article', {'class': 'product_pod'})

# II. Encapsuler le script de l'étape 1 dans une fonction / Passer l'URL à mon code qui parse les pages Livre

# Définir la fonction
def scrape_data(product_page_url):
    ##a) Récupération de "product_page_url"
    response = requests.get(product_page_url)
    book = BeautifulSoup(response.content, 'html.parser')
    ##b) Récupération de "universal_ product_code (upc)"
    universal_product_code = book.find("table", class_="table table-striped").find("td").text
    ##c) Récupération de "title"
    div = book.find("div", class_="product_main")
    title = div.find("h1").text
    ##d) Récupération... des données qui se trouvent dans la même zone de la page web (i.e. "table")
    # Définition du périmètre de ladite zone
    table = book.find("table", class_="table table-striped")
    table_td = table.find_all("td")
    # Récupération de price_including_tax
    price_including_tax = table_td[3].text
    # Récupération de price_excluding_tax
    price_excluding_tax = table_td[2].text
    # Récupération de number_available
    number_available = table_td[5].text
    ##e) Récupération des données qui se trouvent ailleurs dans la page
    # Récupération de product_description
    product_description = book.find_all("p")[3].text
    # Récupération de category
    category = book.find_all("a")[3].text
    # Récupération de review_rating
    review_rating = div.find("p", class_="star-rating").attrs["class"][1]
    # Récupération de image_url
    image_url = book.find("img").attrs["src"]
    # Définir, comme variables, la ligne dite "header" et la ligne dite "données"
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

# Appeler la fonction
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

print("Data has been scraped and written to 'data_produit.csv' file.")