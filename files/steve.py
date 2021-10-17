filename = 'steve.txt'

try:
	with open(filename, encoding='utf-8') as file:
		file.read()
except FileNotFoundError:
	print(f"Filename '{filename}' doesn't exist. Check the file path.")