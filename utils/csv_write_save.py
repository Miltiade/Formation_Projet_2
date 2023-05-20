'''A script that:
-- creates directories
-- generates 1 CSV file with scraped data as values
-- and saves the CSV file in one of the directories '''

from pathlib import Path
from csv import writer

def generate(header,values,filename="data.csv"):
    # # Define variable "values" of output CSV file
    # values = []
    # # Define variable "header" of output CSV file
    # header = [
    #     "product_page_url",
    #     "universal_product_code",
    #     "title",
    #     "price_including_tax",
    #     "price_excluding_tax",
    #     "number_available",
    #     "product_description",
    #     "category",
    #     "review_rating",
    #     "image_url",
    #     ]
    base_directory = Path("output_files")
    sequential_art_directory = base_directory / "category_sequential_art"
    sequential_art_directory.mkdir(parents=True, exist_ok=True)
    sequential_art_images_directory = sequential_art_directory / "images"
    sequential_art_images_directory.mkdir(parents=True, exist_ok=True)
    print("directories created successfully!")
    with open(filename, 'w', newline="") as csvfile:
        csv_writer = writer(csvfile)
        csv_writer.writerow(header)
        csv_writer.writerows(values)
    return ("file created successfully!")