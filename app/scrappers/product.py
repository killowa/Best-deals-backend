import json

class Product:
	def __init__(self, price, rate, reviewsCount, imageUrl, header, source, link):
		self.price = price
		self.imageUrl = imageUrl
		self.reviewsCount = reviewsCount
		self.rate = rate
		self.score = 0
		self.header = header
		self.source = source
		self.link = link

	def setScore(self, score):
		self.score = score

	def toJson(self):
		data = { 
			'price': self.price, 
			'rate': self.rate, 
			'score': self.score,
			'imageUrl': self.imageUrl,
			'reviewsCount': self.reviewsCount,
			'link': self.link,
			'source': self.source,
			'header': self.header,
		}

		return json.dumps(data)
