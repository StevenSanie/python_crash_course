print('\nEnter the letter "q" to close this program.\n')
while True:
	number1 = input('Enter Number: ')
	if number1 == 'q':
		print('Program closed')
		break

	number2 = input('Enter another Number: ')
	if number2 == 'q':
		print('Program closed')
		break

	try:
		answer = int(number1) + int(number2)
	except ValueError:
		print('\tYou Entered An Invalid Number.'.upper())
	else:
		print(answer)
		break