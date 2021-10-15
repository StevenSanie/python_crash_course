people_numbers = {
	'sanie': [1232, 2321, 2342],
	'steven': [2341, 2313, 342],
	'carly': [3421, 3423, 521],
	'violet': [2341, 1422, 563]
}

for name, numbers in people_numbers.items():
	print(f"\n\t{name.title()}'s Numbers are:")
	for number in numbers:
		print(f"\t{number}")