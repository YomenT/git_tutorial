#ice_cream = ['strawberry', 'chocolate', 'vanilla', 'cookies and cream']

class Restaurant(object):
	def __init__(x, restaurant_name, cuisine_type):
		x.restaurant_name = restaurant_name
		x.cuisine_type = cuisine_type
		x.numbers_served = 0

	def describe_restaurant(x):
		print("The restaurant name is " + x.restaurant_name.title() + ".")
		print("The cuisine type today is " + x.cuisine_type.title() + ".")

	def open_restaurant(x):
		print("The restaurant is now open!")

	def read_numbers_served(x):
		print("The number of people served so far: " + str(x.numbers_served)) 

	def set_number_served(x, number_served):
		x.numbers_served = number_served

	def increment_number_served(x, people):
		x.numbers_served += people

class IceCreamStand(Restaurant):
	def ___init___(x, restaurant_name, cuisine_type):
		super(IceCreamStand, x).___init___(restaurant_name, cuisine_type)

	def describe_flavors(x):
		for flavors in x:
			print("Here are the following flavors...")
			print(flavors)

y = ['strawberry', 'chocolate', 'vanilla']

ice_cream_stand = IceCreamStand('kilwins', y)

ice_cream_stand.describe_restaurant()
ice_cream_stand.describe_flavors()

"""
restaurant1 = Restaurant('on the border', 'mexican')
restaurant2 = Restaurant('bosphorus', 'turkish')
restaurant3 = Restaurant('olive garden', 'italian')

restaurant1.describe_restaurant()
restaurant1.set_number_served(10)
restaurant1.increment_number_served(3)
#restaurant1.numbers_served = 10
restaurant1.read_numbers_served()
print(" ")
restaurant2.describe_restaurant()
print(" ")
restaurant3.describe_restaurant()
"""
