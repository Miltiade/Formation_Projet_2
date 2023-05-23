""" A script to:
-- Generate 1 CSV file (containing scraped data) for one book category
-- Download every book's image"""

from utils.scrape_category import scrape_category
# from utils.extract_categories_urls import extract_categories_url
# from utils.url import extract_category_name
from utils.create_output_files_directory import create_output_files_directory
# from utils.create_category_directories import create_category_directories

# For ONE category: scrape all books data and generate CSV file

#1. Define as variable the URL to scrape
cat_url = "https://books.toscrape.com/catalogue/category/books/music_14/index.html"
#2. Scrape products data from this URL
result = scrape_category(cat_url)

#3.a. Create directory: "output_files/
create_output_files_directory()
#3.b. Create category directories: "output_files/category_sequential_art/ and "output_files/category_sequential_art/images
# create_category_directories()

#4.a. Generate CSV file with scraped product data; create adequate category directories; save it there
generate_and_save(result)
print("file generated and saved successfully! Evohe! Onnea!")
#5. For every book in the category: save image in "category_sequential_art" directory