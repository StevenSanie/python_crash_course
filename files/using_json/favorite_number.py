import json
filename = '../json_files/fav-number.json'
number = input('Enter number: ')
with open(filename, 'w') as f:
	json.dump(number, f)
	print(f'We will remember your number - {number}')