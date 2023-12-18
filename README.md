# Projet de Scrapping Selenium WoWhead

Ce projet utilise Selenium et BeautifulSoup pour scraper des informations sur des articles du site WoWhead. Il est conçu pour être rapide et efficace, utilisant le multithreading pour traiter plusieurs articles simultanément.

## Description

Le script Python extrait les informations détaillées de différents articles à partir du site WoWhead. Il s'appuie sur Selenium pour naviguer sur le site et BeautifulSoup pour analyser le HTML et extraire les données nécessaires.

## Prérequis

Pour exécuter ce script, vous devez avoir installé Python sur votre système ainsi que les bibliothèques suivantes :

- Selenium
- BeautifulSoup4
- ChromeDriver (compatible avec la version de votre navigateur Chrome)

## Installation

1. Clonez ce dépôt sur votre machine locale.
2. Installez les dépendances Python en exécutant :
pip install selenium beautifulsoup4


3. Téléchargez ChromeDriver depuis [ici](https://sites.google.com/a/chromium.org/chromedriver/downloads) et extrayez-le dans un dossier de votre choix.

## Configuration

1. Ouvrez le fichier `script.py`.
2. Modifiez la variable `path_to_chromedriver` pour qu'elle pointe vers l'exécutable ChromeDriver que vous avez téléchargé.

## Utilisation

Pour exécuter le script, utilisez la commande suivante dans votre terminal :

python app.py


Assurez-vous que le fichier `items.json` contenant les ID des articles que vous souhaitez scraper est présent dans le même répertoire que le script.

## Fonctionnalités

- Multithreading pour un scraping rapide.
- Gestion des erreurs et des timeouts.
- Récupération propre et structurée des données.


