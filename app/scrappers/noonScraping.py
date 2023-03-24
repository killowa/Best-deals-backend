import resource
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
# from noonProduct import Product
# from Heuristic import Heuristic
import sys

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# PATH = "/usr/local/bin/chromedriver"
# driver = webdriver.Chrome(PATH)
driver.get('https://www.noon.com/egypt-en/')
driver.implicitly_wait(10)

search = driver.find_element(By.CSS_SELECTOR, 'input[id]')
SEARCH_KEYS = ' '.join(sys.argv[1:])
search.send_keys(SEARCH_KEYS)
search.send_keys(Keys.RETURN)

names=[]
prices=[]
links=[]
rates=[]
peopleRates=[]
products=[]
# heuristic = Heuristic(products)
#CSS SELECTORS
# div[data-qa='product-name']
# strong[class='amount']
# span[class='sc-5e739f1b-0 gEERDr wrapper productContainer  ']>a
# div[class='sc-61515602-0 czLWQH']

productNames = driver.find_elements(By.CSS_SELECTOR,"div[data-qa='product-name']")
productPrices = driver.find_elements(By.CSS_SELECTOR,"strong[class='amount']")
productHref = driver.find_elements(By.CSS_SELECTOR,"span[class='sc-5e739f1b-0 gEERDr wrapper productContainer  ']>a")
productRates = driver.find_elements(By.CSS_SELECTOR,"div[class='sc-61515602-0 czLWQH']")

for name in productNames:
    names.append(name.get_attribute("title"))
for price in productPrices:
    prices.append(price.text)  
for link in productHref:
    links.append(link.get_attribute("href"))
for r in productRates:
    rate=r.text.split('\n', 1)[0]
    if rate =='':
        rate=0
        numOfRates=0
    else:
        numOfRates=r.text.split('\n', 1)[1]
    rates.append(rate)
    peopleRates.append(numOfRates)

products=zip(names,prices,links,rates,peopleRates)
for product in list(products):
    print(product)
    print('-'*50)

for i in range(len(names)):
    product = Product(float(prices[i]), 0, float(rates[i]),int(numOfRates[i]), 0)
    products.append(product)


heuristic.normalize()

productsData = []
for product in products: productsData.append(product.toJson())

print(productsData)