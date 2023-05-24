'''A function that scrapes, from a Book page, all the book's requested data'''
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

'''A function that SCRAPES, from a Books category page, all the books' requested data'''
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
-- creates local DIRECTORIES
-- generates 1 CSV file with scraped data as values
-- and SAVES the CSV file in one of the directories '''
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

'''A function that downloads and SAVES IMAGE FILE of each book.
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
# url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
# result = scrape_category(url)
# print(result,"data scraped successfully! :)")
# result2 = generate_and_save(url)
# print(result2)
# result3 = download(url)
# print(result3)