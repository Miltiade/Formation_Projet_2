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

#D'abord, copions le code HTML de la page web que l'on cible

## Nom et prénom
import requests
from bs4 import BeautifulSoup

## Intro (cf. énoncé du projet) : on va chercher la page web concernée et on en analyse la structure
## Problématique : extraire des données spécifiques d'une page HTML et les ordonner dans un fichier CSV
url = "http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

## PARTIE I : DECLARER comme variables les données que l'on récupère dans la page HTML visée
##a) Récupération de "product_page_url"
soup.url
##b) Récupération de "universal_ product_code (upc)"
table = soup.find("table",class_="table table-striped")
#print(table)
td = soup.find("td")
upc = td.text
##c) Récupération de title

## PARTIE II : ECRIRE LES DONNEES DANS UN FICHIER

##a) Créer un nouveau fichier CSV et l'ouvre en écriture
fichier = open("data_produit.csv","w")

#b) Ecrire la 1ère ligne, dite "en-têtes de colonnes"
entetecolonne = ["product_page_url","universal_product_code"]
fichier.write(";".join(entetecolonne))
fichier.write("product_page_url;universal_product_code;title;price_including_tax;price_excluding_tax;number_available;product_description;category;review_rating;image_url")

#c) Remplir la 2e ligne avec les données récupérées dans la PARTIE I

#d) Fermer le fichier

#e) Notifier à l'utilisateur que le script est terminé

#fichier.write()
fichier.close()