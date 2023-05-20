""" A script to:
-- Generate 1 CSV file (containing scraped data) for one book category
-- Download every book's image"""

from utils.csv_write_save import generate
from utils.scrape_category import scrape_category
# from utils.extract_categories_urls import extract_categories_url
# from utils.url import extract_category_name
from utils.create_output_files_directory import create_output_files_directory
from utils.create_category_directories import create_category_directories
from utils.csv_write_save import generate

# For ONE category: scrape all books data and generate CSV file

#1. Define as variable the URL to scrape
cat_url = "https://books.toscrape.com/catalogue/category/books/sequential-art_5/index.html"
#2. Scrape products data from this URL
result = scrape_category(cat_url)

#3.a. Create directory: "output_files/
create_output_files_directory()
#3.b. Create category directories: "output_files/category_sequential_art/ and "output_files/category_sequential_art/images
# create_category_directories()

#4.a. Generate CSV file with scraped product data; create adequate category directories; save it there
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
values = [result]
for book_data in values:
    directory = "category_sequential_art"
    generate(header, book_data, directory)
print("file generated successfully!")
#5. Download every book's image. Save it in "category_sequential_art" directory