# try:
# 	print(5/0)
# except ZeroDivisionError:
# 	print('Sorry man, I just cannot devide a number by a zero, you know.')

# try:
# 	print(2 + '2')
# except TypeError:
# 	print('Number and String cannot be added together, man!')

from typing import SupportsComplex


print('Give me two numbers I devide them for you in less than a second')
print('Enter q to quit the calculator')

while True:
	first_number = input('Enter first number: ')
	if first_number == 'q':
		break
	second_number = input('Enter second number: ')
	if second_number == 'q':
		break

	try:
		answer = int(first_number) / int(second_number)
	except ValueError:
		print('You must enter only numbers!!'.upper())
	except ZeroDivisionError:
		print("Can't devide a number by zero!!".upper())
	else:
		print(f"\t{answer}")