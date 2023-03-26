def formatPrice(price):
	return '.'.join(price.splitlines())

def formatDeliveryPrice(deliveryPrice):

	if deliveryPrice == '': return 0

	return deliveryPrice.split()[0]