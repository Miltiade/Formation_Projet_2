'''A function that scrapes, from a Books category page, all the books' requested data'''
import requests
from bs4 import BeautifulSoup
from scrape_product import scrape
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
        values.append(scrape(url))
    return values

'''A function that:
-- creates local directories
-- generates 1 CSV file with scraped data as values
-- and saves the CSV file in one of the directories '''
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
def generate_and_save(values,filename="data.csv"):
    base_directory = Path("output_files")
    directory = base_directory / values[0][CATEGORY_INDEX]
    directory.mkdir(parents=True, exist_ok=True)
    images_directory = directory / "images"
    images_directory.mkdir(parents=True, exist_ok=True)
    print("directories created successfully!")
    file_path = directory/filename
    with open(file_path, 'w', buffering=-1) as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow(HEADER)
        csv_writer.writerows(values)
    return ("file created successfully!")

'''A function that downloads and saves image file of each book.
NB1: filename = [booksUPC].jpeg
NB2: file saved in "[category]/images/" directory'''
import requests
from url import extract_image_name_from_url
def download(url):
    response = requests.get(url)
    if response.ok:
        name = extract_image_name_from_url(url)
        with open("images/" + name, "wb") as file:
            file.write(response.content)
    else:
        print("Erreur lors du téléchargement de l'image")

#TESTING:
url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
result = scrape_category(url)
print(result)
result2 = generate_and_save(url)
print(result2)
result3 = download(url)
print(result3)