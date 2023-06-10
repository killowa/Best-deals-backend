from product import Product
from helpers import fetchElement, fetchElements

def scrap(driver, search_key, n):

    search_key = search_key.replace(' ', '%20')
    driver.get('https://www.noon.com/egypt-en/search/?q=' + search_key)

    
    product_containers = fetchElements(driver, "span[class='sc-5e739f1b-0 gEERDr wrapper productContainer  ']")

    # slice the first n products
    product_containers = product_containers[:n]

    names = []
    prices = [0.0]*len(product_containers)
    links = []
    rates = [0.0]*len(product_containers)
    reviews_count = [0]*len(product_containers)


    for i,p in enumerate(product_containers):
        name = fetchElement(p, "div[data-qa='product-name']")
        names.append(name.get_attribute("title").replace('"', '').replace('\'', '') if name else "")

        price = fetchElement(p, "strong[class='amount']")
        prices[i]=float(price.text) if price else 0

        link = fetchElement(p, "span[class='sc-5e739f1b-0 gEERDr wrapper productContainer  ']>a")
        links.append(link.get_attribute("href") if link else "")

        rate = fetchElement(p, "span[class='sc-e568c3b8-1 bFgxSY']")
        rate = rate.text if rate else 0
        if rate != 0:
            numOfRates = fetchElement(p,"span[class='sc-61515602-2 cmvYOR']")
            numOfRates = numOfRates.text if numOfRates else 0
            #replace 7.0K with 7000
            if numOfRates[-1] == 'K':
                numOfRates = float(numOfRates[:-1]) * 1000

            rates[i]=float(rate)
            reviews_count[i]=int(numOfRates)
        
    products = [Product(prices[i], rates[i], reviews_count[i], "", names[i], "noon", links[i]) for i in range(len(product_containers))]
    return products
