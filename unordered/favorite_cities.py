cities = {
	'lusaka': {
		'country': 'zambia',
		'population': 3_989_678,
		'fact': 'capital of zambia'
	},

	'livingstone': {
		'country': 'zambia',
		'population': 3_231_342,
		'fact': 'center of tourism '
	},

	'eastern province': {
		'country': 'zambia',
		'population':989_678,
		'fact': 'where home is'
	},

}

# loop through the dictionary, and grab the city names
# loop through the nested dictionary and grab the information about the nested city

for city_name, city_data in cities.items():
	print(f"\nThe following is information about {city_name.title()}")
	for key, value in city_data.items():
		print(f"\t{key.title()}: {value}")