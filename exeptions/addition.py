number1 = input('Enter Number: ')
number2 = input('Enter another Number: ')

try:
	answer = int(number1) + int(number2)
except ValueError:
	print('\tPlease enter valid numbers!'.upper())
else:
	print(answer)