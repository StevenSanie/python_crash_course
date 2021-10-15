favorite_places = {
	'sanie': ['lusaka', 'new york', 'paris'],
	'steve': ['copperbelt', 'new york', 'chingola'],
	'jeff': ['chingola'],
	'enock': ['kabwe', 'livingstone', 'sillicon valley'],
	'sandy': ['new york']
}

# loot throught the dictionary 
for name, places in favorite_places.items():

	# check if places are equal one
	if len(places) == 1:
		print(f"\n{name.title()}'s favorite place is: ")

		# loop through the list
		for place in places:
			print(f"\t{place.title()}")
	else:
		print(f"\n{name.title()}'s favorite places are:")
		for place in places:
			print(f"\t{place.title()}")