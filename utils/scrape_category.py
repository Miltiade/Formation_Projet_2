"""MAIN_SINGLE_CATEGORY:
a script that scrapes data from a Books category webpage, 
then saves scraped data in a CSV file, 
then saves each book's image in a specified directory"""
# main_single_category(url_de_la_categorie)

import requests
from bs4 import BeautifulSoup

from scrape_book import scrape

"""2. A function that SCRAPES, from a Books category page, all the books' requested data"""


def scrape_category(url):
    # Declare empty list
    books = []
    # Create Soup object that will be parsed
    response = requests.get(url)
    # Parse the page
    soup = BeautifulSoup(response.content, "html.parser")
    books += soup.find_all("article", {"class": "product_pod"})
    # Parse the next pages
    while soup.find("li", {"class": "next"}):
        next_url = soup.find("li", {"class": "next"}).find("a").get("href")
        url = "/".join(url.split("/")[:-1]) + "/" + next_url
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        books += soup.find_all("article", {"class": "product_pod"})
    values = []
    for link in books:
        url = link.find("a").get("href")
        url = "http://books.toscrape.com/catalogue/" + url[9:]
        values.append(scrape(url))
    return values


"""3. A function that:
-- creates local DIRECTORIES
-- generates 1 CSV file with scraped data as values
-- and SAVES the CSV file in one of the directories """
from pathlib import Path
from csv import writer

HEADER = [
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
CATEGORY_INDEX = 7


def generate_and_save(values, filename="data.csv"):
    base_directory = Path("output_files")
    directory = base_directory / values[0][CATEGORY_INDEX]
    directory.mkdir(parents=True, exist_ok=True)
    file_path = directory / filename
    with open(file_path, "w", buffering=-1) as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow(HEADER)
        csv_writer.writerows(values)
    return ()


"""4. A function that downloads and SAVES IMAGE FILE of each book.
NB1: filename = [booksUPC].jpeg
NB2: file saved in "[category]/images/" directory"""
import requests


def download(upc, url, category):
    images_directory = Path("output_files") / category / "images"
    images_directory.mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    if response.ok:
        file_path = images_directory / upc
        with open(f"{file_path}.jpg", "wb") as file:
            file.write(response.content)
            print(f"Image '{upc}' downloaded successfully.")
    else:
        print("Error")


def download_category_images(values):
    category_name = values[0][7]
    for book_data in values:
        image_url = book_data[9]
        upc = book_data[1]
        full_image_url = image_url.replace("../../", "https://books.toscrape.com/")
        print(full_image_url)
        download(upc, full_image_url, category_name)


# TESTING: MAIN_SINGLE_CATEGORY
url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
result = scrape_category(url)
print(result, "data scraped successfully! :)")
# result2 = generate_and_save(result)
# print(result2, "file saved successfully. Nice job!")
result3 = download_category_images(result)
print(result3, "images downloaded successfully. Cheers!")

# Créer la fonction qui récupère l'URL de chaque catégorie. Puis: dans le "main", appeler la fonction "main_single_category".
# Créer le fichier main. La seule URL qui y existera sera celle de la page d'accueil du site web.

# Faire "correction PEP-8", avec flake8 et black
# Re-modulariser les fonctions
# Faire/modifier les docstrings

# Préparer la soutenance