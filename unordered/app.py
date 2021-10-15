is_active = True
data = {}
while is_active:

	# get the data
	name = input('Enter Name: ')
	comment = input('Enter Comment: ')
	print('You comment was submitted!')
	repeat = input('Repeat? y/n')

	# add data in the dictionary
	data[name] = comment
	if repeat == 'n':
		is_active = False
print(data)