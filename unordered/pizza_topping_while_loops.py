is_active = True
pizza_toppings = []
while is_active:
	requested_topping = input('Enter your pizza toppings: ')

	if requested_topping != 'quit':
		pizza_toppings.append(requested_topping)
		print(f"{requested_topping} will be added to your pizza!")
	else:
		print(f"\n You requested for:")
		for topping in pizza_toppings:
			print(f"\t > {topping.title()}")
		break