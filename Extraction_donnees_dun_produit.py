# LA COMMANDE: Écrivez un script Python qui visite cette page et en extrait les informations suivantes :
# ● product_page_url
# ● universal_ product_code (upc)
# ● title
# ● price_including_tax
# ● price_excluding_tax
# ● number_available
# ● product_description
# ● category
# ● review_rating
# ● image_url
# Écrivez les données dans un fichier CSV qui utilise les champs ci-dessus comme en-têtes de colonnes.


#D'abord, copions le code HTML de la page web que l'on cible:
import requests
url = "http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
page = requests.get(url)
print(page.content)

#Ensuite, parsons les éléments qui nous intéressent, en utilisant Beautiful Soup
pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
url = "http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Ensuite, récupérons les données que l'on souhaite dans la page HTML visée :
## Récupération de "product_page_url"
>> soup.url
## Récupération de "universal_ product_code (upc)"
>> soup.find("th", id="UPC")
## Récupération de "title"
>> soup.find("h1", class="col-sm-6 product_main")
## Récupération de "price_including_tax"
>> soup.find("th", id="Price (excl. tax)")
## Récupération de "price_excluding_tax"
>> soup.find("th", id="Price (excl. tax)")
## Récupération de "number_available"
>> soup.find_all("p", class="instock availability">)
## Récupération de "product_description"
>> soup.find("p", id="product_description")
## Récupération de "category"
>> soup.find_all("a", href="../category/books/history_32/index.html">History</a>)
## Récupération de "review_rating"
>> soup.find_all(id="reviews" class="sub-header">)
## Récupération de "image_url"
>> soup.findall("img", id="product_gallery" class="carousel")

#Transformons en format CSV les données ainsi extraites

git commit -m "codé : installation des libs, et extraction des données de la page HTML"
git add Extraction_donnees_dun_produit
