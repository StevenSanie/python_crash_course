import json
def get_username():	
	username = input('Enter you name: ')
	filename = '../json_files/username.json'
	with open(filename, 'w') as f:
		json.dump(username, f)

	print(f'I will remember your name next time - {username}.')

def greet_user():
	filename = '../json_files/username.json'
	try:
		with open(filename) as f:
			username = json.load(f)
			new_user = input(f'Are you {username}? (y/n): ')
			if new_user == 'n':
				get_username()
			else:
				print(f'I have remembered you. Welcome back, {username}')
	except FileNotFoundError:
		get_username()

greet_user()