filename = './text_files/learning_python.txt'

with open(filename) as my_file:
	for language in my_file:
		language = language.replace('python', 'JavaScript')
		print(language)