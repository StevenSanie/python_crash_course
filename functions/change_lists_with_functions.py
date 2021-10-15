unprinted_designs = ['phone case', 'iphones', 'robot pendat', 'bags']
completed_designs = []

# My sollution
# def print_design():
# 	while unprinted_designs:
# 		done_design = unprinted_designs.pop()
# 		print(f"printing: {done_design.title()}")
# 		printed_designs.append(done_design)
# print_design()

# def show_printed_work(printed_designs):
# 	print(f"The following art works were printed: ")
# 	for printed in printed_designs:
# 		print(f"> {printed.title()}")
# show_printed_work(printed_designs[:])

# Book solutions
def print_models(unprinted_design, completed_designs):
	while unprinted_design:
		current_design = unprinted_design.pop()
		print(f"Now printing: {current_design.title()}.")
		completed_designs.append(current_design)

def show_completed_prints(comleted_designs):
	print('\nWe managed to make: ')
	for design in completed_designs:
		print(f"\t > {design.title()}")


print_models(unprinted_designs[:], completed_designs)
show_completed_prints(completed_designs)
print(unprinted_designs)