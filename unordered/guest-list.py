from os import name


names = ['Sanie', 'Steve', 'Stephen']
msg = 'You are invited for dinner!'
sorry_msg = 'Sorry, Uyenda kunyumba!'
print(f"""
	{names[0]}, {msg} #print message to person one
	{names[1]}, {msg} #...
	{names[2]}, {msg} #...
""")

print(f"unfortunately, {names[1]} won't make it for dinner")

names[1] = 'Jeffrey'
print(f"""
	{names[0]}, {msg} #print message to person one
	{names[1]}, {msg} #...
	{names[2]}, {msg} #...
""")

print('Guess What? I got more space to host more people!'.upper())

names.insert(0, 'Carol')
names.insert(2, 'Mercy')
names.insert(5, 'Mark')

print(f"""
	{names[0]}, {msg} #print message to person one
	{names[1]}, {msg} #...
	{names[2]}, {msg} #...
	{names[3]}, {msg} #...
	{names[4]}, {msg} #...
	{names[5]}, {msg} #...
""")

print('Sadly, the table broke! Only two can have dinner with me.')

print(f"""
	{names.pop()}, {sorry_msg} #print message to person one
	{names.pop()}, {sorry_msg} #print message to person one
	{names.pop()}, {sorry_msg} #print message to person one
	{names.pop()}, {sorry_msg} #print message to person one
	

	{names[0]} and {names[-1]}, You got yourselves a spot to enjoy dinner with me!
""")

del names[0]
del names[-1]
print(names)