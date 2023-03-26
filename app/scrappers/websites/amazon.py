from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from helpers import fetchElement, fetchElements, formatPrice, filterWithKeys, formatDeliveryPrice
from product import Product
from CssSelctors import selectors

def scrap(search_keys):
  options = Options()
  options.headless = False
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

  driver.get('https://www.amazon.eg/-/en')

  search = fetchElement(driver, selectors['SEARCH_BAR'])

  search.send_keys(search_keys)
  search.send_keys(Keys.RETURN)

  search_results = fetchElements(driver, '[data-component-type="s-search-result"]')
  filtered_results = filterWithKeys(search_results, search_keys)

  products = []

  for result in filtered_results:

    # Default values for none mandatory elems
    deliveryPrice = "EGP0"
    imageUrl = ""

    # Selenium elements for required product data
    product_price_elem = fetchElement(result, selectors['PRODUCT_PRICE'])
    header_elem = fetchElement(result, selectors['HEADER'])
    delivery_price_elem = fetchElement(result, selectors['DELIVERY_PRICE'])
    rate_elem = fetchElement(result, selectors['RATE'])
    reviews_count_elem = fetchElement(result, selectors['REVIEWS_COUNT'])
    image_elem = fetchElement(result, selectors['IMAGE'])

    mandatory_elems = [product_price_elem, rate_elem, reviews_count_elem, header_elem]

    if None in mandatory_elems: continue

    # Data
    if delivery_price_elem and delivery_price_elem.text.isnumeric(): deliveryPrice = formatDeliveryPrice(delivery_price_elem.text)
    if image_elem: imageUrl = image_elem.get_attribute('src')
    productPrice = formatPrice(product_price_elem.text)
    rate = rate_elem.text
    header = header_elem.text
    link = fetchElement(header_elem, 'a').get_attribute('href')
    reviewsCount = reviews_count_elem.text[1:-1]

    product = Product(productPrice, deliveryPrice, float(rate), int(reviewsCount), imageUrl, header, 'amazon', link)
    products.append(product)

  return products
