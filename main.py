# Import relevant libraries
from utils.csv import generate as generate_csv
from utils.category import scrape_category

# From homepage :
# Extract all category pages url

# For loop code below on url below

# Define URL
url = "http://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html"

# Extract category data for url
values= scrape_category(url)
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

print("Data has been scraped and written to csv file.")