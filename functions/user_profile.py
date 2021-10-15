def build_user(first_name, last_name, **other_data):
	other_data['first_name'] = first_name
	other_data['last_name'] = last_name
	print(other_data)

build_user('sanie', 'zulu', location = 'lusaka', age = 34, relationship_status = 'very single')