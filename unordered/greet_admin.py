users = ['sanie', 'steven', 'sanday', 'admin', 'owen', 'enock', 'jeff']
del users
if users:
	for user in users:
		if user == 'admin':
			print(f"\t\t\n Successfuly logged in as an {user.title()}\n".upper())
		else:
			print(f'Hey {user.title()}, thank you for logging in again.')
else:
	print('We need to find some users!')