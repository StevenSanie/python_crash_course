is_activate = True
while is_activate:
	age = int(input('Enter you age: '))
	if age < 3:
		print('Free!')
		break #or can simply change the is_active flag to False to stop the loop
	elif age <= 12:
		print('$10.00')
		break
	elif age > 12:
		print('$25.00')