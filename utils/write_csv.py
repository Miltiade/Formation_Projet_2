'''A script that generates 1 CSV file with scrapped data as values'''

from csv import writer

def generate(header,values,filename="data.csv"):
    # Define variable "values" of output CSV file
    values = []
    # Define variable "header" of output CSV file
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
    with open(filename,"w") as file:
        csv_writer = writer(file)
        csv_writer.writerow(header)
        csv_writer.writerows(values)