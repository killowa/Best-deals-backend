import sys
import json
from os import listdir
from os.path import isfile, join
from helpers import get_file_path
from Heuristic import Heuristic
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

root_dir = 'app/scrappers'
sys.path.append(root_dir)


WEBSITES_PATH = get_file_path('websites')
scrappingFiles = ['websites.' + f.split('.')[0] for f in listdir(
    WEBSITES_PATH) if isfile(join(WEBSITES_PATH, f))]

SEARCH_KEYS = ' '.join(sys.argv[1:])
# SEARCH_KEYS = "dell g15"
#options = Options()
# options.add_argument('--headless=new') # use headless mode

#driver = webdriver.Chrome(executable_path='D:\Downloads\chromedriver_win32\chromedriver', options=options)
options = webdriver.ChromeOptions()

options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(
    service= Service('D:\Downloads\chromedriver_win32\chromedriver'), 
    options=options,
)
products = []

# n is the maximum number of products to scrape from each website
for scrappingFile in scrappingFiles:
    products += __import__(scrappingFile,fromlist=['scrap']).scrap(driver, SEARCH_KEYS, n=10)

# print('len is = ',len(products))
heuristic = Heuristic(products)
heuristic.normalize()

productsData = []
for product in products:
    productsData.append(json.loads(product.toJson()))

print(productsData)

# quit driver
driver.quit()
