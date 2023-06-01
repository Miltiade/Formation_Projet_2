""" A script to:
-- generate 1 CSV file (containing scraped data) 
-- and download every book's image
for each book category"""

from utils.extract_categories_urls import extract_categories_url
from utils.scrape_category import main_single_category

print("I heard you; processing now.")

# Define homepage as webpage to scrape
url = "https://books.toscrape.com/"

# From homepage, extract each book category's URL
categories_URLs = extract_categories_url(url)
print("Categories URL extracted!")

# Loop through the book categories' URLs and call the data scraping function for each URL
for url in categories_URLs:
    main_single_category(url)
print("all done! cheers!")

# DONE: Créer la fonction qui récupère l'URL de chaque catégorie ("extract_categories_urls").
# DONE Puis: dans le "main", appeler la fonction "main_single_category".
# Créer le fichier main. La seule URL qui y existera sera celle de la page d'accueil du site web.

# PROBLEME : quand on exécute main, le terminal répond:
# "  File "/Users/zyggie/Documents/Git_Projet_2/Formation_Projet_2/utils/scrape_category.py", line 31, in scrape_category
#     values.append(scrape(url))
#                   ^^^^^^^^^^^
#   File "/Users/zyggie/Documents/Git_Projet_2/Formation_Projet_2/utils/scrape_book.py", line 11, in scrape
#     book.find("table", class_="table table-striped").find("td").text
#     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'NoneType' object has no attribute 'find'"
# Pourquoi répond-il cela alors que, quand on exécute la fonction "scrape_book" dans le script éponyme,
# il ne renvoie alors aucun message d'erreur ?
# Autrement dit : pourquoi renvoie-t-il un message d'erreur ou non, suivant le script qu'on exécute?

# Faire "correction PEP-8", avec flake8 et black
# Re-modulariser les fonctions
# Faire/modifier les docstrings

# Préparer la soutenance