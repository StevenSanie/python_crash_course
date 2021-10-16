filename = './text_files/test.txt'
with open(filename, 'r') as f:
	contents = f.read()
	print(f"{len(contents.split())}")
