import requests
import csv
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
books = soup.find_all('article', {'class': 'product_pod'})

# Récupérer les toutes les URL des liens depuis la page Catégorie
Books_URL = soup.find_all('a')
for link in Books_URL:
    print(link.get('href'))

# Encapsuler le script de l'étape 1 dans une fonction

def scrape_data(books):
    ##a) Récupération de "product_page_url"
    product_page_url = link
    ##b) Récupération de "universal_ product_code (upc)"
    universal_product_code = (
        link.find("table", class_="table table-striped").find("td").text
    )
    ##c) Récupération de "title"
    div = link.find("div", class_="product_main")
    title = div.find("h1").text
    ##d) Récupération... des données qui se trouvent dans la même zone de la page web (i.e. "table")
    # Définition du périmètre de ladite zone
    table = link.find("table", class_="table table-striped")
    table_td = table.find_all("td")
    # Récupération de price_including_tax
    price_including_tax = table_td[3].text
    # Récupération de price_excluding_tax
    price_excluding_tax = table_td[2].text
    # Récupération de number_available
    number_available = table_td[5].text
    ##e) Récupération des données qui se trouvent ailleurs dans la page
    # Récupération de product_description
    product_description = link.find_all("p")[3].text
    # Récupération de category
    category = link.find_all("a")[3].text
    # Récupération de review_rating
    review_rating = div.find("p", class_="star-rating").attrs["class"][1]
    # Récupération de image_url
    image_url = link.find("img").attrs["src"]
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
    ## PARTIE II : ECRIRE LES DONNEES DANS UN FICHIER
    # Ecrire la ligne "header" et la ligne "données" dans le fichier CSV
    with open("data_produit.csv","w") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(header)
        csv_writer.writerow(values)

# # Appeler la fonction
print(scrape_data)

# # with open('books.csv', mode='w', newline='', encoding='utf-8') as file:
# #     writer = csv.writer(file)
# #     writer.writerow(['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])

# #     for book in books:
# #         product_page_url = book.find('h3').find('a')['href'].replace('../../../', 'http://books.toscrape.com/catalogue/')
# #         upc = book.select('p')[2].text.strip()
# #         title = book.find('h3').find('a')['title']
# #         price_including_tax = book.select('p')[1].text.strip()[1:]
# #         price_excluding_tax = book.select('p')[2].text.strip()[1:]
# #         number_available = book.select('p')[2].text.strip()[10:]
# #         description = book.find('p', {'class': None})
# #         category = soup.find('ul', {'class': 'breadcrumb'}).select('li')[2].text.strip()
# #         review_rating = book.select('p')[0]['class'][0]
# #         image_url = book.find('img')['src'].replace('../../', 'http://books.toscrape.com/')

# #         writer.writerow([product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, description, category, review_rating, image_url])

print("Data has been scraped and written to 'books.csv' file.")
