sandwich_orders = ['egg', 'pastrami',  'seafood', 'grilled chicken', 'pastrami', 'ham', 'roast beef', 'pastrami']
finished_sandwiches = []

print('We have run out of pastrami!')
print(sandwich_orders)

while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

while sandwich_orders:
	for made_sandwich in sandwich_orders:
		print(f"What I made: \n{made_sandwich.title()} sandwich. \n")
		done_sandwiches = sandwich_orders.pop()
		finished_sandwiches.append(done_sandwiches)

print(f"\n\t The following are the sandwiches we made for you:")
for sandwich in finished_sandwiches:
	print(f"\t > {sandwich.title()} Sandwich")
4