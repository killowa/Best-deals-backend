from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from product import Product

product_containers = None

def scrape_description(driver,descriptions):
    desc = driver.find_elements(By.CLASS_NAME, 'name')
    for d in desc:
      descriptions.append(d.get_attribute('textContent').replace('"', '').replace('\'', ''))



def scrape_price(driver,prices):
    price = driver.find_elements(By.CLASS_NAME, 'prc')
    for p in price:
        pr = p.get_attribute('textContent')
        pr = float(pr[4:].split('-')[0].replace(',', ''))
        prices.append(pr)


def scrape_rating(driver,ratings):
    # rating = driver.find_elements(By.CLASS_NAME,'stars _s')
    for i, c in enumerate(product_containers):
        r_element = driver.find_elements(By.CLASS_NAME, 'stars _s')

        r = r_element.text.split() if r_element else None
        # ratings.append(r.get_attribute('textContent'))
        ratings[i] = r[0] if r else None


def scrape_img(driver,imgs):
    img = driver.find_elements(By.CLASS_NAME, 'img')
    for i in img:
        imgs.append(i.get_attribute('src'))


def scrape_link(driver,links):
    link = driver.find_elements(By.CLASS_NAME, 'core')
    for l in link:
        links.append(l.get_attribute('href'))


def scrape_next(driver):
    next_pg = driver.find_element(By.CSS_SELECTOR, '[aria-label="Close"]')
    next_pg.click()


def scrap(driver, search_key):

    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # s = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(options=options, service=s)


    jumia = 'https://www.jumia.com.eg/catalog/?q='

    shipping = '&shipped_from=country_local#catalog-listing'

    search_link = jumia + search_key.replace(" ", "+") + shipping

    driver.get(search_link)

    product_containers = driver.find_elements(
        By.CSS_SELECTOR, ".prd._fb.col.c-prd")

    descriptions = []
    prices = []
    ratings = [0]*len(product_containers)
    reviews_count = [0]*len(product_containers)
    imgs = []
    links = []

    scrape_description(driver,descriptions)
    scrape_price(driver,prices)
    # scrape_rating(driver,ratings)
    scrape_img(driver,imgs)
    scrape_link(driver,links)

    # print(len(product_containers))
    # print()
    # print(len(descriptions), len(prices), len(ratings), len(imgs), len(links),len(reviews_count), len(imgs))

    # create list of Product objects
    products = [Product(prices[i], ratings[i], reviews_count[i], imgs[i], descriptions[i], "jumia", links[i]
                        ) for i in range(len(descriptions))]
    
    
    return products

    # products_json = []

    # # print first product details
    # for i in range(len(products)):
        
    #     products_json.append(json.loads(products[i].toJson()))

    # # print poducts_json as a JSON string to be sent to the API endpoint
    # print(json.dumps(products_json, indent=4))

    # driver.quit()