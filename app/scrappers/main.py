from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from helpers import fetchElement, fetchElements, percentToFraction, containsKeys
from product import Product
from Heuristic import Heuristic
from CssSelctors import selectors
import sys

def formatPrice(price):
	return '.'.join(price.splitlines())

def filterWithKeys(search_results, keys):
  return [res for res in search_results if containsKeys(fetchElement(res, selectors['HEADER']).text, keys)]

def formatDeliveryPrice(deliveryPrice):

	if deliveryPrice == '': return 0

	return deliveryPrice.split()[0]

options = Options()
options.headless = False
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

driver.get('https://www.amazon.com/')

search = fetchElement(driver, selectors['SEARCH_BAR'])
# SEARCH_KEYS = ' '.join(sys.argv[1:])
SEARCH_KEYS='dell g15'

search.send_keys(SEARCH_KEYS)
search.send_keys(Keys.RETURN)

search_results = fetchElements(driver, '[data-component-type="s-search-result"]')
filtered_results = filterWithKeys(search_results, SEARCH_KEYS)

products = []
heuristic = Heuristic(products)

for result in filtered_results:

	productPrice = formatPrice(fetchElement(driver, selectors['PRODUCT_PRICE']).text) if fetchElement(driver, selectors['PRODUCT_PRICE']) else 0
	deliveryPrice = formatDeliveryPrice(fetchElement(driver, selectors['DELIVERY_PRICE']).text) if fetchElement(driver, selectors['DELIVERY_PRICE']) else 0
	imageUrl = fetchElement(driver, selectors['IMAGE']).get_attribute('src')
	numberOfReviews = fetchElement(driver, selectors['REVIEWS_COUNT']).text.split()[0] if fetchElement(driver, selectors['REVIEWS_COUNT']) else 0
	
	rates = fetchElements(driver, selectors['RATE'])

	if not productPrice or not numberOfReviews: continue

	product = Product(productPrice, deliveryPrice, heuristic.calculateRatingScore(rates, numberOfReviews), imageUrl)
	products.append(product)

heuristic.normalize()

productsData = []
for product in products: productsData.append(product.toJson())

print(productsData)
driver.quit()


