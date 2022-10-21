from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "./chromedriver"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://www.amazon.com/')

search = driver.find_element(By.ID, 'twotabsearchtextbox')

search.send_keys('dell g15')
search.send_keys(Keys.RETURN)

search_results = driver.find_elements(By.CSS_SELECTOR, '.s-result-item .a-price')

for result in search_results:
	print(result.text)
# search = driver.find_element(By.NAME, "s")
# search.send_keys("test")
# search.send_keys(Keys.RETURN)

# try:
# 	main = WebDriverWait(driver, 10).until(
# 		EC.presence_of_element_located((By.ID, "main")))

# except:
# 	driver.quit()

# articles = main.find_elements(By.TAG_NAME, "article")
	
# for article in articles:
# 	summary = article.find_element(By.CLASS_NAME, "entry-summary")
# 	print(summary.text)
# driver.close()
