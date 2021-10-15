data = {}
is_active = True

while is_active:
	name = input('Enter name to continue \n\t: ')
	comment = input('Enter you comment \n\t: ')
	# rating = input('Enter rating: \n\t: ')

	data[name] = comment
	# data['rating'] = rating

	repeat = input('Enter ner data? (y/n)')
	if repeat != 'y':
		is_active = False

print(data)