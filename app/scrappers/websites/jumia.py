from product import Product
from bs4 import BeautifulSoup


def scrap(driver, search_key, n):

    jumia = 'https://www.jumia.com.eg/catalog/?q='

    shipping = '&shipped_from=country_local#catalog-listing'

    search_link = jumia + search_key.replace(" ", "+") + shipping

    driver.get(search_link)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    product_containers = soup.select('.prd._fb.col.c-prd')
    # product_containers = fetchElements(driver, '.prd._fb.col.c-prd')

    # slice the first n products
    product_containers = product_containers[:n]

    headers = []
    prices = []
    ratings = [0.0]*len(product_containers)
    reviews_count = [0]*len(product_containers)
    imgs = []
    links = []

    # get whole html then parse it

    for i in range(len(product_containers)):
        
        # soup = BeautifulSoup(cont.get_attribute('innerHTML'), 'html.parser')
        # parse needed header from html
        header = soup.select_one(
            f'#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div > article:nth-child({i+1}) > a > div.info > h3')
        headers.append(header.text.replace(
            '"', '').replace('\'', '') if header else None)

        # parse needed price from html
        price = soup.select_one(
            f'#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div > article:nth-child({i+1}) > a > div.info > div.prc')
        pr = price.text if price else None
        pr = float(pr[4:].split('-')[0].replace(',', '')) if pr else None
        prices.append(pr if pr else None)

        # parse needed rate from html
        rate = soup.select_one(
            f'#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div > article:nth-child({i+1}) > a > div.info > div.rev > div')
        r = rate.text if rate else None
        # split rate into stars and reviews count
        if r:
            reviews_count[i] = int(rate.next_sibling.text.replace('(', '').replace(')', ''))
            ratings[i] = float(r.split(' ')[0])

        # parse needed image from html
        img = soup.select_one(
            f'#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div > article:nth-child({i+1}) > a > div.img-c > img')
        img_link = img['data-src']
        imgs.append(img_link if img_link[:4] != "data" else "")

        # parse needed link from html
        link = soup.select_one(
            f'#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div > article:nth-child({i+1}) > a')
        full_link = "https://www.jumia.com.eg" + link['href'] if link else ""
        links.append(full_link if link else "")


    # create list of Product objects
    products = [Product(prices[i], ratings[i], reviews_count[i], imgs[i], headers[i], "jumia", links[i]
                        ) for i in range(len(product_containers))]
    
    return products
