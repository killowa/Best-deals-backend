import json


class Product:
    def __init__(self, name, price, link, rate, reviewsCount, imageUrl):
        self.name = name
        self.price = price
        self.link = link
        self.imageUrl = imageUrl
        self.reviewsCount = reviewsCount
        self.rate = rate
        self.score = 0

    def setScore(self, score):
        self.score = score

    def parsePrice(self, price):
        return float(price)

    def toJson(self):
        data = {
            'name': self.name,
            'price': self.price,
            'link': self.link,
            'rating': self.rate,
            # 'score': self.score,
            'reviews_count': self.reviewsCount,
            'img_url': self.imageUrl,
        }

        return json.dumps(data)
