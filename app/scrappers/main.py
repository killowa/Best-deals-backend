from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from product import Product

def doesItemMatchesSearchKeys(text, searchKeys):
	searchKeys = searchKeys.split(" ")
	text = text.lower()

	for searchKey in searchKeys:
		searchKeyWithSpaceBefore = ' ' + searchKey.lower()
		searchKeyWithSpaceAfter = searchKey.lower() + ' '
		if text.find(searchKeyWithSpaceAfter) == -1 and text.find(searchKeyWithSpaceBefore) == -1:
			return ""

	return text

def formatPrice(price):
	return '.'.join(price.splitlines())

def filterResultsWithSearchKeys(search_results):
	filtered_results = []

	for result in search_results:

		result_header = fetchElement(result, 'h2.a-size-mini')
		if doesItemMatchesSearchKeys(result_header.text, SEARCH_KEYS):
			filtered_results.append(fetchElement(result, 'a').get_attribute('href'))

	return filtered_results

def fetchElement(root, cssSelector):
	try:
		element =  WebDriverWait(root, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector)))
		return element
	except:
		return False

def fetchElements(root, cssSelector):
	try:
		element =  WebDriverWait(root, 3).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, cssSelector)))
		return element
	except:
		return False

def score(totalPrice, rate):
	return rate - totalPrice

def percentToFraction(percent):

	return int(percent)/100

def calculateRatingScore(rates, numberOfReviews):
	weights = [9, 3, 1, -3, -9] # Increasing weight as rate increase

	totalRateScore = 0

	for rate, weight in zip(rates, weights):
		rateScore = weight*percentToFraction(rate.get_attribute('aria-valuenow')[:-1])*int(numberOfReviews)
		totalRateScore = totalRateScore + rateScore

	return round(totalRateScore, 3)


def normalize(products):

	totalPrices = [product.totalPrice() for product in products]
	ratings = [product.rating for product in products]

	print(totalPrices)
	print(ratings)

	minRate, maxRate = min(ratings), max(ratings)
	minTotalPrice, maxTotalPrice = min(totalPrices), max(totalPrices)

	if len(products) == 0: 
		product.setScore(1)
		return

	for product in products:

		normalizedPrice = (product.totalPrice() - minTotalPrice)/(maxTotalPrice-minTotalPrice)
		normalizedRate = (product.rating - minRate)/(maxRate-minRate)

		product.setScore(score(normalizedPrice, normalizedRate))	


def formatDeliveryPrice(deliveryPrice):

	if deliveryPrice == '': return 0

	return deliveryPrice.split()[0]

options = Options()
options.headless = False
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=options)

driver.get('https://www.amazon.com/')

search = fetchElement(driver, '#twotabsearchtextbox')

SEARCH_KEYS = 'dell g15' # TODO: read this from user input in our site

search.send_keys(SEARCH_KEYS)
search.send_keys(Keys.RETURN)

search_results = fetchElements(driver, '[data-component-type="s-search-result"]')
filtered_results_url = filterResultsWithSearchKeys(search_results)

products = []

for result_url in filtered_results_url:

	driver.get(result_url)

	IMAGE_SELECTOR = '#landingImage'
	PRODUCT_PRICE_SELECTOR = '#corePrice_feature_div > div > span > span:nth-child(2)'
	DELIVERY_PRICE_SELECTOR = '#mir-layout-DELIVERY_BLOCK-slot-NO_PROMISE_UPSELL_MESSAGE'
	RATING_SELECTOR = '#histogramTable [aria-valuenow]'
	NUMBER_OF_REVIWES_SELECTOR = '#acrCustomerReviewText'

	productPrice = formatPrice(fetchElement(driver, PRODUCT_PRICE_SELECTOR).text) if fetchElement(driver, PRODUCT_PRICE_SELECTOR) else 0
	deliveryPrice = formatDeliveryPrice(fetchElement(driver, DELIVERY_PRICE_SELECTOR).text) if fetchElement(driver, DELIVERY_PRICE_SELECTOR) else 0
	imageUrl = fetchElement(driver, IMAGE_SELECTOR).get_attribute('src')
	numberOfReviews = fetchElement(driver, NUMBER_OF_REVIWES_SELECTOR).text.split()[0] if fetchElement(driver, NUMBER_OF_REVIWES_SELECTOR) else 0
	rates = fetchElements(driver, RATING_SELECTOR)

	if not productPrice or not numberOfReviews: continue

	product = Product(productPrice, deliveryPrice, calculateRatingScore(rates, numberOfReviews), imageUrl)
	products.append(product)

normalize(products)

driver.quit()


