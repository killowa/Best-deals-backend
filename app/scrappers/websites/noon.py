from product import Product
from bs4 import BeautifulSoup
from helpers import filterWithKeys


def scrap(driver, search_key, num_of_products):

    driver.get('https://www.noon.com/egypt-en/search/?q=' + search_key.replace(' ', '%20'))
    # get whole html then parse it
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # product_containers = fetchElements(
    # driver, "span[class='sc-5e739f1b-0 gEERDr wrapper productContainer  ']")

    product_containers = soup.find_all(
        'span', class_='sc-5e739f1b-0 gEERDr wrapper productContainer')

    # slice the first n products
    product_containers = product_containers[:num_of_products]
    product_containers = filterWithKeys(product_containers, search_key, 'div[data-qa="product-name"]')

    names = []
    prices = [0.0]*len(product_containers)
    links = [""]*len(product_containers)
    rates = [0.0]*len(product_containers)
    reviews_count = [0]*len(product_containers)

    for i, cont in enumerate(product_containers):

        # get needed name from every product container
        name = cont.select_one('div[data-qa="product-name"]')
        names.append(name['title'].replace(
            '"', '').replace('\'', '') if name else "")

        # get needed price from every product container
        price = cont.select_one('strong[class="amount"]')
        prices[i] = float(price.text) if price else 0

        # # get needed link from every product container
        link = cont.select_one(
            'a', attrs={'class': 'sc-5e739f1b-0 gEERDr wrapper productContainer  '})
        # link = cont.next_sibling

        full_link = 'https://www.noon.com' + link['href'] if link else ""
        links[i] = full_link if link else ""

        # soup2 = BeautifulSoup(cont.get_attribute('innerHTML'), 'html.parser')

        rate = cont.select_one('span[class="sc-e568c3b8-1 bFgxSY"]')
        rate = rate.text if rate else 0.0
        if rate != 0.0:
            numOfRates = cont.select_one('span[class="sc-61515602-2 cmvYOR"]')
            numOfRates = numOfRates.text if numOfRates else 0
            # replace 7.0K with 7000
            if numOfRates[-1] == 'K':
                numOfRates = float(numOfRates[:-1]) * 1000

            rates[i] = float(rate)
            reviews_count[i] = int(numOfRates)

    products = [Product(prices[i], rates[i], reviews_count[i], "", names[i],
                        "noon", links[i]) for i in range(len(product_containers))]
    return products
