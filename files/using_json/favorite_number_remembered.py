import json
filename = '../json_files/fav-number.json'

try:
	with open(filename, 'r') as f:
		number = json.load(f)
except FileNotFoundError:
	number = input('Enter number: ')
	with open(filename, 'w') as f:
		json.dump(number, f)
		print(f'We will remember your number - {number}')
else:
	print(f'I still remember that your favorite number is {number}')