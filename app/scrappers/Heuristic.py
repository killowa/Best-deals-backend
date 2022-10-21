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
			product.calculateScore(totalPrices[0], ratings[0])
			return

		for product in self.products:

			normalizedTotalPrice = (product.totalPrice() - minTotalPrice)/(maxTotalPrice-minTotalPrice)
			normalizedRate = (product.rating - minRate)/(maxRate-minRate)

			product.calculateScore(normalizedRate, normalizedTotalPrice)


	def calculateRatingScore(self, rates, numberOfReviews):
		weights = [9, 3, 1, -3, -9] # Increasing weight as rate increase

		totalRateScore = 0

		for rate, weight in zip(rates, weights):
			rateScore = weight*percentToFraction(rate)*int(numberOfReviews)
			totalRateScore = totalRateScore + rateScore

		return round(totalRateScore, 3)