from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

def percentToFraction(percent):

	return int(percent)/100

def doesItemMatchesSearchKeys(text, searchKeys):
	searchKeys = searchKeys.split(" ")
	text = text.lower()

	for searchKey in searchKeys:
		searchKeyWithSpaceBefore = ' ' + searchKey.lower()
		searchKeyWithSpaceAfter = searchKey.lower() + ' '
		if text.find(searchKeyWithSpaceAfter) == -1 and text.find(searchKeyWithSpaceBefore) == -1:
			return ""

	return text