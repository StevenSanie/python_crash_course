def check_stage():
	age = int(input('Enter Age: ').strip())
	if age  >= 65:
		print('You are an elder')
		check_stage()
	elif age >= 20:
		print('you are an adult')
		check_stage()
	elif age >= 13:
		print('you are a teen')
		check_stage()
	elif age >= 4:
		print('you are a kid')
		check_stage()
	elif age >= 4:
		print('you are a toddler')
		check_stage()
	else: 
		print('You are a baby!')
		
check_stage()