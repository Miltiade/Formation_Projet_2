'''A script to download and save image file of each product'''

import requests
from .url import extract_image_name_from_url

def download(url):
    response = requests.get(url)
    if response.ok:
        name = extract_image_name_from_url(url)
        with open("images/" + name, "wb") as file:
            file.write(response.content)
    else:
        print("Erreur lors du téléchargement de l'image")