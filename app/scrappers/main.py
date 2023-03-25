from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from helpers import fetchElement, fetchElements, containsKeys
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

driver.get('https://www.amazon.eg/-/en')

search = fetchElement(driver, selectors['SEARCH_BAR'])
SEARCH_KEYS = ' '.join(sys.argv[1:])

search.send_keys(SEARCH_KEYS)
search.send_keys(Keys.RETURN)

search_results = fetchElements(driver, '[data-component-type="s-search-result"]')
filtered_results = filterWithKeys(search_results, SEARCH_KEYS)

products = []
heuristic = Heuristic(products)

for result in filtered_results:

  # Default values for none mandatory elems
  deliveryPrice = "EGP0"
  imageUrl = ""

  # Selenium elements for required product data
  product_price_elem = fetchElement(result, selectors['PRODUCT_PRICE'])
  delivery_price_elem = fetchElement(result, selectors['DELIVERY_PRICE'])
  rate_elem = fetchElement(result, selectors['RATE'])
  reviews_count_elem = fetchElement(result, selectors['REVIEWS_COUNT'])
  image_elem = fetchElement(result, selectors['IMAGE'])

  mandatory_elems = [product_price_elem, rate_elem, reviews_count_elem]

  if None in mandatory_elems: continue

  # Data
  if delivery_price_elem and delivery_price_elem.text.isnumeric(): deliveryPrice = formatDeliveryPrice(delivery_price_elem.text)
  if image_elem: imageUrl = image_elem.get_attribute('src')
  productPrice = formatPrice(product_price_elem.text)
  rate = rate_elem.text
  reviewsCount = reviews_count_elem.text[1:-1]

  product = Product(productPrice, deliveryPrice, float(rate), int(reviewsCount), imageUrl)
  products.append(product)

heuristic.normalize()

productsData = []
for product in products: productsData.append(product.toJson())

print(productsData)
driver.quit()


