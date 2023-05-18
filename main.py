""" A script to:
-- Generate 1 CSV file per book category
-- Download every book's image"""

# Import relevant libraries
from utils.csv import generate as generate_csv
from utils.scrape_category import scrape_category
from utils.extract_categories_urls import extract_categories_url
from utils.url import extract_category_name

# Define URL of website to scrape
index_url = "http://books.toscrape.com/index.html"

# Define variable "header" of output CSV files
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

# From the website's homepage : extract urls of all books categories

# extract_categories_url(url)

# Create a "for" loop on url below
cat_urls = extract_categories_url(index_url)
print(cat_urls)
for url in cat_urls:
    values = scrape_category(url)
    name = extract_category_name(url)
    # Variabilize category name using module "url"
    generate_csv(header, values, name + ".csv")

    # download images based on image_url in values
    # from utils.image import download
    # download(values)

print("Data has been scraped and written to csv files.")