filename = './text_files/test.txt'
with open(filename, 'w') as file:
	for i in range(10):
		file.write('Learning Programming Is Really Fun!!\n')