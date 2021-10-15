private_messages = [
	'Hello, Steven. I love what you do!',
	'Hey there! Would you like to join the dinner party tonight?',
	'I just want to let you know that i will not make it to the party!',
	'I do not want to be in any relationship with anyone!'
]
sent_box = []

def send_messages(messages, sent_messages):
	while messages:
		just_sent_message = messages.pop()
		print(f"Sending '{just_sent_message}' to Steven!")
		sent_messages.append(just_sent_message)

send_messages(private_messages, sent_box)
print(f"\t\n Pending Messages: {private_messages}")
print(f"\t\n Sent Messages: {sent_box}")