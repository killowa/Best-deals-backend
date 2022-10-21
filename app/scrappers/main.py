from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from helpers import fetchElement, fetchElements, percentToFraction, doesItemMatchesSearchKeys
from product import Product
from Heuristic import Heuristic
from CssSelctors import selectors

def formatPrice(price):
	return '.'.join(price.splitlines())

def filterResultsWithSearchKeys(search_results, searchKeys):
	filtered_results = []

	for result in search_results:

		result_header = fetchElement(result, selectors['HEADER_SELECTOR'])#
		if doesItemMatchesSearchKeys(result_header.text, searchKeys):
			filtered_results.append(fetchElement(result, 'a').get_attribute('href'))#

	return filtered_results

def formatDeliveryPrice(deliveryPrice):

	if deliveryPrice == '': return 0

	return deliveryPrice.split()[0]

options = Options()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

driver.get('https://www.amazon.com/')

search = fetchElement(driver, selectors['SEARCH_BAR'])

SEARCH_KEYS = 'dell g15' # TODO: read this from user input in our site

search.send_keys(SEARCH_KEYS)
search.send_keys(Keys.RETURN)

search_results = fetchElements(driver, '[data-component-type="s-search-result"]')
filtered_results_url = filterResultsWithSearchKeys(search_results, SEARCH_KEYS)

products = []
heuristic = Heuristic(products)

for result_url in filtered_results_url:

	driver.get(result_url)

	productPrice = formatPrice(fetchElement(driver, selectors['PRODUCT_PRICE_SELECTOR']).text) if fetchElement(driver, selectors['PRODUCT_PRICE_SELECTOR']) else 0
	deliveryPrice = formatDeliveryPrice(fetchElement(driver, selectors['DELIVERY_PRICE_SELECTOR']).text) if fetchElement(driver, selectors['DELIVERY_PRICE_SELECTOR']) else 0
	imageUrl = fetchElement(driver, selectors['IMAGE_SELECTOR']).get_attribute('src')
	numberOfReviews = fetchElement(driver, selectors['NUMBER_OF_REVIWES_SELECTOR']).text.split()[0] if fetchElement(driver, selectors['NUMBER_OF_REVIWES_SELECTOR']) else 0
	
	rates = [rate.get_attribute('aria-valuenow')[:-1] for rate in fetchElements(driver, selectors['RATING_SELECTOR'])]#

	if not productPrice or not numberOfReviews: continue

	product = Product(productPrice, deliveryPrice, heuristic.calculateRatingScore(rates, numberOfReviews), imageUrl)
	products.append(product)

heuristic.normalize()

productsData = []
for product in products: productsData.append(product.toJson())

print(productsData)
driver.quit()


