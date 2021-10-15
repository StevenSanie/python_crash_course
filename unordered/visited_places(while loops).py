places = []
while True:
	name = input('Enter city you have been to before: ')

	if name == 'quit':
		print(f"You have been to: ")
		for place in places:
			print(f"\t{place.title()}") 
		break
	else:

		places.append(name)
		print(f'{name} added to the list of places you have been before!')