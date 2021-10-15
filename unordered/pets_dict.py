# make the dictionaries
pet_0 = {
	'kind': 'reptile',
	'name': 'kila',
	'owner': 'sanie'
}

pet_1 = {
	'kind': 'bird',
	'name': 'hueg',
	'owner': 'enock'
}

pet_2 = {
	'kind': 'cat',
	'name': 'simba',
	'owner': 'steven'
}

pet_3 = {
	'kind': 'insect',
	'name': 'ive',
	'owner': 'violet'
}

pet_4 = {
	'kind': 'cat',
	'name': 'Kiara',
	'owner': 'sanday'
}

# store the dictionaries in the list
pets = [pet_0, pet_1, pet_2, pet_3, pet_4]

# loop through the list of pets
for pet in pets:

	# print the data we know about each pet from the list
	print(f"\nPet data for the pet named {pet['name'].title()}")
	print(f"""	Kind of pet: {pet['kind'].title()}
	Pet owner: {pet['owner'].title()}
	""")