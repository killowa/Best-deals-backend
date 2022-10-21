import json

class Product:
	def __init__(self, price, deliveryPrice, rating, imageUrl):
		self.price = price
		self.deliveryPrice = deliveryPrice
		self.imageUrl = imageUrl
		self.rating = rating
		self.score = 0

	def calculateScore(self, normalizedRate, normalizedTotalPrice):
		self.score = normalizedRate - normalizedTotalPrice

	def totalPrice(self):
		return self.parsePrice(self.price)+ self.parsePrice(self.deliveryPrice)

	def parsePrice(self, price):
		return float(price[1:].replace(',', ''))


	def toJson(self):
		data = { 
			'price': self.price, 
			'deliveryPrice': self.deliveryPrice, 
			'rating': self.rating, 
			'score': self.score
		}

		return json.dumps(data)
