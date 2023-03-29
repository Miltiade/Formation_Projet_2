import requests
import csv
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
books = soup.find_all('article', {'class': 'product_pod'})

with open('books.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['product_page_url', 'universal_product_code', 'title', 'price_including_tax', 'price_excluding_tax', 'number_available', 'product_description', 'category', 'review_rating', 'image_url'])

    for book in books:
        product_page_url = book.find('h3').find('a')['href'].replace('../../../', 'http://books.toscrape.com/catalogue/')
        upc = book.select('p')[2].text.strip()
        title = book.find('h3').find('a')['title']
        price_including_tax = book.select('p')[1].text.strip()[1:]
        price_excluding_tax = book.select('p')[2].text.strip()[1:]
        number_available = book.select('p')[2].text.strip()[10:]
        description = book.find('p', {'class': None})
        category = soup.find('ul', {'class': 'breadcrumb'}).select('li')[2].text.strip()
        review_rating = book.select('p')[0]['class'][0]
        image_url = book.find('img')['src'].replace('../../', 'http://books.toscrape.com/')

        writer.writerow([product_page_url, upc, title, price_including_tax, price_excluding_tax, number_available, description, category, review_rating, image_url])

print("Data has been scraped and written to 'books.csv' file.")
