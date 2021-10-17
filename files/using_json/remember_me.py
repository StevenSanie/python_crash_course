import json
username = input('Enter you name: ')

filename = '../json_files/username.json'
with open(filename, 'w') as f:
	json.dump(username, f)

print(f'I will remember your name next time - {username}.')
