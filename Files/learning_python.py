filename = './text_files/learning_python.txt'

"""print the entire file contents"""
# with open(filename) as my_file:
# 	contents = my_file.read()
# 	print(contents)

"""print the file's content using a loop"""
# with open(filename) as my_file:
# 	for line in my_file:
# 		print(line)


"""store the contents of the file in a list and print"""
with open(filename) as my_file:
	listed_strings = my_file.readlines()

for string in listed_strings:
	print(string)