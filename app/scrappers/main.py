import sys
import json
from os import listdir
from os.path import isfile, join
from helpers import get_file_path
from Heuristic import Heuristic
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ROOT_DIR = 'app/scrappers'
sys.path.append(ROOT_DIR)


WEBSITES_PATH = get_file_path('websites')
scrappingFiles = ['websites.' + f.split('.')[0] for f in listdir(
    WEBSITES_PATH) if isfile(join(WEBSITES_PATH, f))]

print('SCRAPING: ', scrappingFiles)

SEARCH_KEYS = ' '.join(sys.argv[1:])
# SEARCH_KEYS = "dell g15"
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
# options.add_argument('--remote-debugging-port=9222')

driver = webdriver.Chrome(service=Service(
    ChromeDriverManager().install()), options=options)
# options.add_argument('--headless=new')  # use headless mode
# driver = webdriver.Chrome(service=Service(
#     ChromeDriverManager().install()), options=options)

products = []

# n is the maximum number of products to scrape from each website
for scrappingFile in scrappingFiles:
    products += __import__(scrappingFile, fromlist=['scrap']).scrap(
        driver, SEARCH_KEYS, num_of_products=10)

# print('len is = ',len(products))
heuristic = Heuristic(products)
heuristic.normalize()

productsData = []
for product in products:
    productsData.append(json.loads(product.toJson()))

print('All: ', productsData)

# quit driver
driver.quit()
