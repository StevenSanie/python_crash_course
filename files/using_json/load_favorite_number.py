import json

filename = '../json_files/fav-number.json'
with open(filename, 'r') as f:
	number = json.load(f)

print(f"The stored number is: {number}")