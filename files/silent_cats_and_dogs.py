files = ['./text_files/cats.txt', './text_figvles/dogs.txt']

for file in files:
	try:
		with open(file, 'r') as f:
			print(f.read())
	except FileNotFoundError:
		pass