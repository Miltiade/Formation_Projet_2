# P2_Book_to_Scrape_PDellac
# Programme de scraping d'informations d'un site e-commerce.

Ce programme est une version beta d'un script permettant d'automatiser un système de surveillance des prix sur un site e-commerce de vente de livre : http://books.toscrape.com/. 

L'objectif est de récupérer les informations suivantes:

* product_page_url_
* universal_ product_code (upc)
* title
* price_including_tax
* price_excluding_tax
* number_available
* product_description
* category
* review_rating
* image_url


Ce programme enregistre ces données sous la forme d'un fichier CSV : il enregistre un fichier CSV par catégorie de livres (histoire, roman policier, etc..). Il enregistre également l'image de la couverture de chaque livre.
A chaque fois qu'on l'exécute, ce programme crée un dossier pour chaque catégorie de livres ; il enregistre le fichier CSV dans ce dossier. Il y crée également un sous-dossier, dans lequel il enregistre les images des couvertures des livres.

## Pour commencer

Les instructions ci-dessous vous permettront d'exécuter correctement ce programme.

## Pré-requis 

* Python est 3 installé ([Télécharger Python](https://www.python.org/downloads/)) 
* Vous savez naviguer dans les dossiers & fichiers d'un ordinateur à partir d'un terminal.

## Installation

Pour un fonctionnement optimal, il est préférable d'exécuter le programme dans un environnement virtuel.

Voici toutes les étapes à suivre:
(NB: c'est dans le terminal que toutes les commandes indiquées ci-dessous doivent être saisies)

1. **Téléchargement du projet.**

    1. Depuis votre terminal, placez-vous dans le dossier où vous souhaitez télécharger le programme:
    
    ```cd [chemin d'accès]```  
    
    2. Créez un nouveau dossier:
    
    ```mkdir [nom de votre dossier]```
    
    3. Copiez le code source:
    
    ```git clone https://github.com/Miltiade/Formation_Projet_2.git```
    
    Vous devez voir (dans le dossier que vous avez créé, depuis votre explorateur) les fichiers suivants:
        * main.py
        * scrape_category.py
        * scrape_book.py
        * extract_categories_urls.py
        * requirements.txt
    

2. **Creer un environnement virtuel.**

    Depuis windows/macOS/linux: ```python3 -m venv env```
    

3. **Activer l'environnement virtuel.**
    
    Depuis windows: ```env\Scripts\activate.bat```
    
    Depuis mac/linux: ```source env/bin/activate```
    

    Si vous rencontrez des difficultés ou si vous souhaitez plus de détails sur l'installation d'un environnement virtuel, vous pouvez vous reporter à la documentation Python officielle:
    
    [Documentation Python](https://docs.python.org/fr/3/library/venv.html/)  
    
4. **Installer les paquets.**

    ```pip install -r requirements.txt```

    (En executant la commande: ```pip freeze```, vous devez voir apparaitre cette liste: 
beautifulsoup4==4.12.0
black==23.3.0
bs4==0.0.1
certifi==2022.12.7
charset-normalizer==3.1.0
click==8.1.3
flake8==6.0.0
idna==3.4
iniconfig==2.0.0
mccabe==0.7.0
mypy-extensions==1.0.0
packaging==23.1
pathspec==0.11.1
platformdirs==3.5.1
pluggy==1.0.0
pycodestyle==2.10.0
pyflakes==3.0.1
pytest==7.3.1
requests==2.28.2
soupsieve==2.4
urllib3==1.26.15)
    
5. **Lancement du programme**

    ```python main.py```

    Le programme crée un dossier unique nommé 'data'. Il y crée également des sous-dossiers : chaque sous-dossier a pour nom la catégorie de livres concernée (histoire, roman policier, etc.). Dans chaque sous-dossier, le programme crée un fichier CSV contenant l'ensemble des données des livres de la catégorie, ainsi qu'un dossier 'images' dans lequel il enregistre toutes les images des couvertures de ces mêmes livres.


## Fabriqué avec
Visual Studio Code, version 1.78.2 (Universal)

## Auteur

* **Paul Dellac** 


## Remerciements

Mille mercis à **Ranga Gonnage** pour ses conseils et son soutien.
