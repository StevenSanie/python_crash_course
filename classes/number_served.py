class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant = restaurant_name
		self.cuisine = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print(f"{self.restaurant} is the best restaurant that is known for {self.cuisine}")

	def open_restaurant(self):
		print(f"{self.restaurant} is now open for business!")

	def set_number_served(self, number):
		self.number_served = number

# the default value, unchanged
restaurant = Restaurant("Sanie's Deli", "I don't know the type")
print(f"we have served {restaurant.number_served} customers so far")

# directly changed
restaurant.number_served = 224_234
print(f"we have served {restaurant.number_served} customers now")

# changed using a method
restaurant.set_number_served(384_534)
print(f"we have served {restaurant.number_served} customers now")