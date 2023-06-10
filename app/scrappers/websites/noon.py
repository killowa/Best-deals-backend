from product import Product
from helpers import fetchElement, fetchElements
from bs4 import BeautifulSoup


def scrap(driver, search_key, n):

    search_key = search_key.replace(' ', '%20')
    driver.get('https://www.noon.com/egypt-en/search/?q=' + search_key)

    
    product_containers = fetchElements(driver, "span[class='sc-5e739f1b-0 gEERDr wrapper productContainer  ']")

    # slice the first n products
    product_containers = product_containers[:n]

    names = []
    prices = [0.0]*len(product_containers)
    links = [""]*len(product_containers)
    rates = [0.0]*len(product_containers)
    reviews_count = [0]*len(product_containers)

    # get whole html then parse it
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # link = soup.find_all('a', class_='sc-5e739f1b-0 gEERDr wrapper productContainer  ')

    for i in range(len(product_containers)):

        # get needed name from every product container
        name = soup.select('div[data-qa="product-name"]')[i]
        names.append(name['title'].replace('"', '').replace('\'', '') if name else "")

        # get needed price from every product container
        price = soup.select('strong[class="amount"]')[i]
        prices[i]=float(price.text) if price else 0

        #TODO: fix link issue

        # # get needed link from every product container
        # link = soup.select('span[class="sc-5e739f1b-0 gEERDr wrapper productContainer  "]>a')[i]
        link = soup.select_one('span[class="sc-5e739f1b-0 gEERDr wrapper productContainer  "]')
        if link:
            links.append(link['href'])

        # get needed rate from html
        rate = soup.select('span[class="sc-e568c3b8-1 bFgxSY"]')[i]
        rate = rate.text if rate else 0
        if rate != 0:
            numOfRates = soup.select('span[class="sc-61515602-2 cmvYOR"]')[i]
            numOfRates = numOfRates.text if numOfRates else 0
            #replace 7.0K with 7000
            if numOfRates[-1] == 'K':
                numOfRates = float(numOfRates[:-1]) * 1000

            rates[i] = float(rate)
            reviews_count[i] = int(numOfRates)
        
    products = [Product(prices[i], rates[i], reviews_count[i], "", names[i], "noon", links[i]) for i in range(len(product_containers))]
    return products
