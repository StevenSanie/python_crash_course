favorite_languages = {
	'San': ['Python', 'JavaScript'],
	'Ted': ['Ruby', 'C++'],
	'Dani': ['Java', 'C'],
	'Carl': ['Python']
}

for name, languages in favorite_languages.items():
	if len(languages) > 1:
		print(f"\n{name}'s favorite programming languages are: ")
		for lang in languages:
			print(f"\t{lang}")
	else:
		print(f"\n{name}'s favorite programming language is only: ")
		for lang in languages:
			print(f"\t{lang}")

