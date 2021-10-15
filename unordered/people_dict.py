
people = [
	{
		'first_name': 'steven',
		'last_name': 'zulu',
		'age': 23,
		'city': 'lusaka'
	},

	{
		'first_name': 'sanie',
		'last_name': 'torvalds',
		'age': 23,
		'city': 'livingstone'
	},

	{
		'first_name': 'carly',
		'last_name': 'mila',
		'age': 34,
		'city': 'kabwe'
	}
]

# loop through the list
for user in people:
	
	# concatinate the name
	full_name = f"{user['first_name']} {user['last_name']}"

	# print the data
	print(f"\n user details for @{user['first_name']}@zedrevise.com".title())
	print(f"\tFull name: {full_name.title()} " 
	f"\n\tAge: {user['age']} \n\tCity: {user['city'].title()} \n")
