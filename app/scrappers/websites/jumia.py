from product import Product
from helpers import fetchElement, fetchElements


def scrap(driver, search_key):

    jumia = 'https://www.jumia.com.eg/catalog/?q='

    shipping = '&shipped_from=country_local#catalog-listing'

    search_link = jumia + search_key.replace(" ", "+") + shipping

    driver.get(search_link)

    product_containers = fetchElements(driver, '.prd._fb.col.c-prd')

    headers = []*len(product_containers)
    prices = []*len(product_containers)
    ratings = [0.0]*len(product_containers)
    reviews_count = [0]*len(product_containers)
    imgs = []*len(product_containers)
    links = []*len(product_containers)

    for i,cont in enumerate(product_containers):
        header = fetchElement(cont, f'#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div > article:nth-child({i+1}) > a > div.info > h3')
        headers.append(header.get_attribute('textContent').replace('"', '').replace('\'', '') if header else None)
                
        price = fetchElement(cont, f'#jm > main > div.aim.row.-pbm > div.-pvs.col12 > section > div > article:nth-child({i+1}) > a > div.info > div.prc')
        pr = price.get_attribute('textContent') if price else None
        pr = float(pr[4:].split('-')[0].replace(',', '')) if pr else None
        prices.append(pr if pr else None)

        rate = fetchElement(cont, '.rev')
        r = rate.get_attribute('innerHTML') if rate else None
        #split rate into stars and reviews count
        if r:
            reviews_count[i] = int(r[-2])
            ratings[i] = float(r.split('>')[1].split(' ')[0])
        
        img = fetchElement(cont, '.img')
        img_link = img.get_attribute('src')
        imgs.append(img_link if img_link[:4] != "data" else "")

        link = fetchElement(cont, '.core')
        links.append(link.get_attribute('href') if link else "")


    # create list of Product objects
    products = [Product(prices[i], ratings[i], reviews_count[i], imgs[i], headers[i], "jumia", links[i]
                        ) for i in range(len(product_containers))]
    
    return products
