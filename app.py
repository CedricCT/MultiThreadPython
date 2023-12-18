import json
import threading
import time  # Importation de la bibliothèque pour le chronométrage
from queue import Queue
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup

# Cette fonction traite un élément et extrait les informations nécessaires
def process_item(driver, item_id, results):
    print(f"Traitement de l'item {item_id}...")
    url = f'https://www.wowhead.com/fr/item={item_id}#reagent-for'
    driver.get(url)

    try:
        # Attente de la présence d'un élément spécifique sur la page
        element_present = EC.presence_of_element_located((By.ID, 'tab-reagent-for'))
        WebDriverWait(driver, 10).until(element_present)
    except TimeoutException:
        print("Timeout waiting for page load")

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Fonction pour vérifier si le tag a seulement la classe 'q1'
    def has_only_q1_class(tag):
        return tag.name == 'a' and tag.get('class') == ['q1']

    tab_reagent_for = soup.find(id="tab-reagent-for")
    if tab_reagent_for:
        first_a_element = tab_reagent_for.find(has_only_q1_class)
        if first_a_element:
            text = first_a_element.get_text(strip=True)
            results.put(f"{item_id} : {text}")
        else:
            results.put(f"{item_id} : Aucun élément <a> avec uniquement la classe 'q1' trouvé")
    else:
        results.put(f"{item_id} : Aucun élément avec l'ID 'tab-reagent-for' trouvé")

# Fonction exécutée par chaque thread pour traiter les éléments
def worker(item_queue, results):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Mode sans interface graphique
    chrome_options.add_argument("--log-level=3")
    service = Service(executable_path=path_to_chromedriver)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    while not item_queue.empty():
        item_id = item_queue.get()
        process_item(driver, item_id, results)
        item_queue.task_done()

    driver.quit()

# Lire les identifiants des articles à partir du fichier JSON
with open('items.json', 'r') as file:
    data = json.load(file)
    item_ids = data['items']

# Chemin vers ChromeDriver
path_to_chromedriver = './chrome/chromedriver.exe'

# Création des files d'attente
item_queue = Queue()
results = Queue()

# Ajouter des éléments dans la file d'attente
for item_id in item_ids:
    item_queue.put(item_id)

# Nombre de threads
num_threads = 5  # Ajustez en fonction des capacités de votre système

threads = []

start_time = time.time()  # Début du chronométrage

for i in range(num_threads):
    thread = threading.Thread(target=worker, args=(item_queue, results))
    thread.start()
    threads.append(thread)

# Attendre que tous les threads soient terminés
for thread in threads:
    thread.join()

end_time = time.time()  # Fin du chronométrage

# Affichage des résultats
print("Résultats obtenus :")
while not results.empty():
    print(results.get())

print(f"Temps total d'exécution: {end_time - start_time} secondes")  # Affichage du temps total d'exécution
