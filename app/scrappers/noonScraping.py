import requests
from bs4 import BeautifulSoup

noon = "https://www.noon.com/egypt-en/search/?q="

def scraping(searchRequest):
    req = requests.get(searchRequest)
    # print(url.status_code)
    soup = BeautifulSoup(req.content,"html.parser")
    # print(soup.prettify())
    names=[]
    prices=[]
    links=[]
    rates=[]
    productNames=soup.find_all('div',{'data-qa':'product-name'})
    productPrices=soup.find_all('div',{'class':'sc-ac248257-1 bEaNkb'})
    productLinks=soup.find_all('span',{'class':'sc-5e739f1b-0 gEERDr wrapper productContainer'})
    productRating=soup.find_all('span',{'class':'ratingValue'})
    for n in productNames[:5]:
        name=n.span.get_text()
        names.append(name)

    for p in productPrices[:5]:
        price=p.strong.get_text()
        prices.append(price)

    for l in productLinks[:5]:
        link="https://www.noon.com"+l.a['href']
        links.append(link)

    for r in productRating[:5]:
        rate=r.get_text()
        rates.append(rate)    

    # print(len(names))


    # zip the names, prices, link, rating, and image of the products
    devices=zip(names,prices,links,rates)
    for device in list(devices):
        print(device)
        print('-'*50)


item = input("search: ")
url=noon+item
print(url)
scraping(url)