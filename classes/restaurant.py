"""It works but i honetly don't think the instances made sence, lol
"""

class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant = restaurant_name
		self.cuisine = cuisine_type

	def describe_restaurant(self):
		# print('Best restaurant in town!!')
		print(f"{self.restaurant} is the best restaurant that is known for {self.cuisine}")

	def open_restaurant(self):
		print(f"{self.restaurant} is now open for business!")

# restaurant = Restaurant("Carol's Deli", "Hot")
# restaurant2 = Restaurant("Tidye", "Cold")
# restaurant3 = Restaurant("JESV", "Warmer")
# 
# # print(restaurant.restaurant, restaurant.cuisine)
# restaurant.open_restaurant()
# restaurant.describe_restaurant()
# 
# # print(restaurant2.restaurant, restaurant2.cuisine)
# restaurant2.open_restaurant()
# restaurant2.describe_restaurant()
# 
# # print(restaurant3.restaurant, restaurant3.cuisine)
# restaurant3.open_restaurant()
# restaurant3.describe_restaurant()