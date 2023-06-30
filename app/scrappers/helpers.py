from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def fetchElement(root, cssSelector):
    try:
        element = WebDriverWait(root, 3).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, cssSelector)))
        return element
    except:
        return None


def fetchElements(root, cssSelector):
    try:
        element = WebDriverWait(root, 3).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, cssSelector)))
        return element
    except:
        return None


def formatPrice(price):
    return '.'.join(price.splitlines())


def filterWithKeys(search_results, keys, header_selector):
    return [res for res in search_results if containsKeys(res.select_one(header_selector).text, keys)]


def containsKeys(text, searchKeys):
    for searchKey in searchKeys.split(" "):
        if text.lower().find(searchKey.lower()) == -1:
            return False

    return True


def get_file_path(file_name):
    root_dir = 'app/scrappers/'
    return root_dir + file_name
