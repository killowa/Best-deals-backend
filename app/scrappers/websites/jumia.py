from product import Product
from bs4 import BeautifulSoup
from helpers import filterWithKeys


def scrap(driver, search_key, num_of_products):

    jumia = 'https://www.jumia.com.eg/catalog/?q='

    shipping = '&shipped_from=country_local#catalog-listing'

    search_link = jumia + search_key.replace(" ", "+") + shipping

    driver.get(search_link)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    print('Jumia source: ', soup)

    product_containers = soup.select('.prd._fb.col.c-prd')
    # slice the first n products
    product_containers = product_containers[:num_of_products]

    product_containers = filterWithKeys(product_containers, search_key, 'h3.name')
    

    headers = []
    prices = []
    ratings = [0.0]*len(product_containers)
    reviews_count = [0]*len(product_containers)
    imgs = []
    links = []

    for i, cont in enumerate(product_containers):

        # header = soup.select_one(
        #     f'#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div > article:nth-child({i+1}) > a > div.info > h3')
        header = cont.select_one('h3.name')
        headers.append(header.text.replace(
            '"', '').replace('\'', '') if header else None)

        # price = soup.select_one(
        #     f'#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div > article:nth-child({i+1}) > a > div.info > div.prc')
        price = cont.select_one('div.prc')
        pr = price.text if price else None
        pr = float(pr[4:].split('-')[0].replace(',', '')) if pr else None
        prices.append(pr if pr else None)

        # rate = soup.select_one(
        #     f'#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div > article:nth-child({i+1}) > a > div.info > div.rev > div')
        rate = cont.select_one('div.rev > div')
        r = rate.text if rate else None
        if r:
            reviews_count[i] = int(
                rate.next_sibling.text.replace('(', '').replace(')', ''))
            ratings[i] = float(r.split(' ')[0])

        # img = soup.select_one(
        #     f'#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div > article:nth-child({i+1}) > a > div.img-c > img')
        img = cont.select_one('div.img-c > img').get('data-src')
        imgs.append(img if img[:4] != "data" else "")

        # link = soup.select_one(
        #     f'#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div > article:nth-child({i+1}) > a')
        link = cont.select_one('a').get('href')
        full_link = "https://www.jumia.com.eg" + link if link else ""
        links.append(full_link if link else "")

    # create list of Product objects
    products = [Product(prices[i], ratings[i], reviews_count[i], imgs[i], headers[i], "jumia", links[i]
                        ) for i in range(len(product_containers))]
    
    print('Jumia: ', products)

    return products
