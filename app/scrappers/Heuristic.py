from helpers import percentToFraction

class Heuristic:

	def __init__(self, products):
		self.products = products

	def normalize(self):

		totalPrices = [product.totalPrice() for product in self.products]
		ratings = [product.rating for product in self.products]

		minRate, maxRate = min(ratings), max(ratings)
		minTotalPrice, maxTotalPrice = min(totalPrices), max(totalPrices)

		if len(self.products) == 0: #TODO: Normalize on all sites
			product.setScore(ratings[0] - totalPrices[0])
			return

		for product in self.products:

			normalizedTotalPrice = (product.totalPrice() - minTotalPrice)/(maxTotalPrice-minTotalPrice)
			normalizedRate = (product.rate * product.reviewersCount - minRate)/(maxRate-minRate)

			product.setScore(normalizedRate - normalizedTotalPrice)
