filename = './text_files/pi_digits.txt'
pi_string = ''

with open(filename) as file_object:
	lines = file_object.readlines()
	for line in lines:
		pi_string += line.strip()

print(pi_string)
print(len(pi_string))
