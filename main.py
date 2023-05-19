""" A script to:
-- Generate 1 CSV file (containing scraped data) per book category
-- Download every book's image"""

# from utils.csv import generate as generate_csv
from utils.scrape_category import scrape_category
from utils.extract_categories_urls import extract_categories_url
from utils.url import extract_category_name
from utils.write_csv import generate

# Define URL of website to scrape
# index_url = "http://books.toscrape.com/index.html"

# For ONE category: scrape all books data and generate CSV file
#1. Define as variable the URL to scrape
cat_url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
#2. Scrape products data from this URL
result = scrape_category(cat_url)
for book_data in result:
    print(book_data)
#3. generate CSV file using scraped "values"