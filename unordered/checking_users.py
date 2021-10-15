current_users = ['sanie', 'violet', 'enock', 'jeff', 'steven']
new_users = ['ruth', 'sanday', 'steven', 'mongwa', 'memory', 'sharon', 'sanie']


for user in new_users: 
	if user in current_users:
		print(f'\n \t\t Sorry, {user}@zedrevise.com is already taken \n')
	else:
		print(f'\n{user}@zedrevise.com is available!\n')

# first create a list with new_users and another with current_users
# loop through the list and using the if statement, check if the new_user is in the current user list