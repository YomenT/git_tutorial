class Restaurant:
	
	number_served = 0

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		print(self.restaurant_name)
		print("Cuisine Type: " + self.cuisine_type)

	def open_restaurant(self):
		print("The restaurant is now open!")

	@classmethod
	def served(cls, number):
		cls.number_served = number
		print("Number Served: " + str(cls.number_served))

#restaurant1 = Restaurant('On the Border', 'Mexican')
#restaurant2 = Restaurant('Bosphorus', 'Turkish')
#restaurant3 = Restaurant('Olive Garden', 'Italian')

#This is just printing the two attributes individually.
#print(restaurant.restaurant_name)
#print(restaurant.cuisine_type)

#This just prints the class variable.
#print(Restaurant.number_served)

#Restaurant.served(10)

class IceCreamStand(Restaurant):
	
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type)
		self.ice_cream_flavors = ['strawberry', 'chocolate', 'vanilla']
		
	def list_flavors(self):
		print("Here are the ice cream flavors.")
		for x in self.ice_cream_flavors:
			print(x.title())

restaurant = IceCreamStand('Kilwins', 'Ice Cream')

restaurant.list_flavors()
