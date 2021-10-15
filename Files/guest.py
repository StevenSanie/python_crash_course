from os import write

filename = './text_files/guest.txt'
is_active = True

while is_active:
	name = input('Enter your name: ')
	with open(filename, 'a') as guest_file:
		if name == 'quit':
			is_active = False
		else:
			guest_file.write(f"{name} \n")