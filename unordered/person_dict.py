person = {
	'name': 'Steven',
	'age': 23,
	'city': 'lusaka'
}

for v, k in sorted(person.items()):
	if k == 'Steven':
		print(f"{k} is my name".upper())
	else:
		print(f"{v} is the key for the value {k}")