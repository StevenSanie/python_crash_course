import json
filename = '../json_files/username.json'

with open(filename) as f:
	username = json.load(f)
	print(f'I have remembered you. Welcome back, {username}')