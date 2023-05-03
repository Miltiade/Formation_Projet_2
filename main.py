# Import relevant libraries
from utils.csv import generate as generate_csv
from utils.category import scrape_category
from utils.extract_categories_urls import extract_categories_url

# Define URL of website to scrape
index_url = "http://books.toscrape.com/index.html"

# From the website's homepage : extract urls of all books categories
# extract_categories_url(url)

# Create a "for" loop code on url below
for url in extract_categories_url(index_url):
    print(url)
    values = scrape_category(url)

# Extract category data for url
# values= scrape_category(url)
# Write csv file with data
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
# Variabilize category name using module url
generate_csv(header, values, "nonfiction.csv")

# download images based on image_url in values
from utils.image import download
download(values)

print("Data has been scraped and written to csv files.")