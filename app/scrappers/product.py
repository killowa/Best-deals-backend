import json

class Product:
	def __init__(self, price, deliveryPrice, rate, reviewsCount, imageUrl, header, source, link):
		self.price = price
		self.deliveryPrice = deliveryPrice
		self.imageUrl = imageUrl
		self.reviewsCount = reviewsCount
		self.rate = rate
		self.score = 0
		self.header = header
		self.source = source
		self.link = link

	def setScore(self, score):
		self.score = score

	def totalPrice(self):
		return self.parsePrice(self.price)+ self.parsePrice(self.deliveryPrice)

	def parsePrice(self, price):
		return float(price[3:].replace(',', ''))


	def toJson(self):
		data = { 
			'price': self.price, 
			'deliveryPrice': self.deliveryPrice,
			'rate': self.rate, 
			'score': self.score,
			'imageUrl': self.imageUrl,
			'reviewsCount': self.reviewsCount,
			'header': self.header,
			'link': self.link,
			'source': self.source
		}

		return json.dumps(data)
