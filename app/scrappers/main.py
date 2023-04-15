import sys

root_dir = 'app/scrappers'
sys.path.append(root_dir)

import json
from Heuristic import Heuristic
from helpers import get_file_path
from os import listdir
from os.path import isfile, join
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

WEBSITES_PATH = get_file_path('websites')
scrappingFiles = ['websites.' + f.split('.')[0] for f in listdir(WEBSITES_PATH) if isfile(join(WEBSITES_PATH, f))]

SEARCH_KEYS = ' '.join(sys.argv[1:])
SEARCH_KEYS = "dell g15"
options = Options()
options.headless = False
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)


products = []

for scrappingFile in scrappingFiles:
  products += __import__(scrappingFile, fromlist=['scrap']).scrap(driver, SEARCH_KEYS)

heuristic = Heuristic(products)
heuristic.normalize()

productsData = []
for product in products: productsData.append(json.loads(product.toJson()))

print(productsData)
