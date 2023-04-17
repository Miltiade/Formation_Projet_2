import requests
import csv
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
books = soup.find_all('article', {'class': 'product_pod'})

# Récupérer toutes les URL des liens depuis la page Catégorie
Books_URL = soup.find_all('a')
for link in Books_URL:
    print(link.get('href'))

# Encapsuler le script de l'étape 1 dans une fonction

def scrape_data(books):
    ##a) Récupération de "product_page_url"
    product_page_url = books
    ##b) Récupération de "universal_ product_code (upc)"
    universal_product_code = (
        books.find("table", class_="table table-striped").find("td").text
    )
    ##c) Récupération de "title"
    div = books.find("div", class_="product_main")
    title = div.find("h1").text
    ##d) Récupération... des données qui se trouvent dans la même zone de la page web (i.e. "table")
    # Définition du périmètre de ladite zone
    table = books.find("table", class_="table table-striped")
    table_td = table.find_all("td")
    # Récupération de price_including_tax
    price_including_tax = table_td[3].text
    # Récupération de price_excluding_tax
    price_excluding_tax = table_td[2].text
    # Récupération de number_available
    number_available = table_td[5].text
    ##e) Récupération des données qui se trouvent ailleurs dans la page
    # Récupération de product_description
    product_description = books.find_all("p")[3].text
    # Récupération de category
    category = books.find_all("a")[3].text
    # Récupération de review_rating
    review_rating = div.find("p", class_="star-rating").attrs["class"][1]
    # Récupération de image_url
    image_url = books.find("img").attrs["src"]
    # Définition, comme variables, de la ligne dite "header" et de la ligne dite "données"
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
    values = [
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
    ## ECRIRE LES DONNEES DANS UN FICHIER
    # Ecrire la ligne "header" et la ligne "données" dans le fichier CSV
    with open("data_produit.csv","w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)
        csv_writer.writerow(values)

# Appeler la fonction
print(scrape_data)

print("Data has been scraped and written to 'books.csv' file.")
