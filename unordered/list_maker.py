# python lists
names = []

def add_names():
	# print(names)
	name = input('>>@: ')
	if name == 'edit()' or name == 'edit':
		if len(names) == 0:
			print('The list is empty. Add item to edit the list')
			add_names()
		else:
			print(f'the list looks like this at this stage: {names}')
			print('To abort the editing, you can just enter the digit 0000')
			editable_name_id = int(input('Enter the ID number of the name you want to edit: '))

			if editable_name_id == '':
				print('You did not enter an ID')
			elif editable_name_id == 0000:
				print('Editing was aborted successfuly!')
				add_names()
			else:
				print(f'You have selected {names[editable_name_id]}, which hold the ID: {editable_name_id}')
				old_name = names[editable_name_id]
				edit_name = input(f'Enter the new name to replace "{old_name.upper()}:"  \t') 
				new_name = names[editable_name_id] = edit_name
				print(f'Success! "{old_name.upper()}" was changed to  "{new_name.upper()}" ')
				add_names()

	elif name == 'get-one':
		if len(names) != 0:
			print(f'your list look like this: {names}\n Its position number is its ID.')
			name_id = int(input('Keeping In My Mind That Counting Starts From Zero In Computer Science Enter The ID To Display It: '))
			print(f'Your ID, {name_id}, returns {names[name_id].title()}')
			print(names)
			add_names()
		else:
			print('The list is Empty')
			add_names()

	elif name == 'cls':
		print(names)

	elif name == '--s/l':
		print(f'\n\t {names} \n\t')
		add_names()

	elif name == 'rm-n':
		print('Python is case senstive')
		removable_name = input('Enter name you want to remove from the list above: ')

		names.remove(removable_name)
		print(names)
		add_names()

	else:
		names.append(name)
		add_names()

add_names()