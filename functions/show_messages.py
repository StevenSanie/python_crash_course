private_messages = [
	'Hello, Steven. I love what you do!',
	'Hey there! Would you like to join the dinner party tonight?',
	'I just want to let you know that i will not make it to the party!',
	'I do not want to be in any relationship with anyone!'
]
def show_messages(messages):
	print('Here are your messages from Sanie!')
	for message in messages:
		print(f"-> {message.title()}")

show_messages(private_messages)