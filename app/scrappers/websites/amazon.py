from helpers import formatPrice, filterWithKeys
from product import Product
from CssSelctors import selectors
from bs4 import BeautifulSoup


def scrap(driver, search_keys, num_of_products):
    # spearate search keys with plus
    driver.get('https://www.amazon.eg/-/en/s?k=' +
               search_keys.replace(" ", "+"))
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # print('Amazon source', soup)

    search_results = soup.select('[data-component-type="s-search-result"]')
    # search_results = result.select_ones '[data-component-type="s-search-result"]')
    # slice the first n results
    search_results = search_results[:num_of_products]

    filtered_results = filterWithKeys(search_results, search_keys, selectors['HEADER'])

    products = []

    for result in filtered_results:

        # Default values for none mandatory elems
        imageUrl = ""

        # Selenium elements for required product data
        product_price_elem = result.select_one(selectors['PRODUCT_PRICE'])
        header_elem = result.select_one(selectors['HEADER'])
        rate_elem = result.select_one(selectors['RATE'])
        reviews_count_elem = result.select_one(selectors['REVIEWS_COUNT'])
        image_elem = result.select_one(selectors['IMAGE'])

        mandatory_elems = [product_price_elem,
                           rate_elem, reviews_count_elem, header_elem]

        if None in mandatory_elems:
            continue

        # Data
        if image_elem:
            imageUrl = image_elem.get('src')
        productPrice = formatPrice(product_price_elem.text)
        rate = rate_elem.get('aria-label').split(' ')[0]
        header = header_elem.text
        header = header.replace('"', '')
        link = header_elem.select_one('a').get('href')
        link = 'https://www.amazon.eg' + link
        reviewsCount = reviews_count_elem.text

        product = Product(float(productPrice[3:].replace(',', '')), float(rate), int(
            reviewsCount.replace(',', '')), imageUrl, header, 'amazon', link)
        products.append(product)

    # print('Amazon: ', products)
    

    return products
