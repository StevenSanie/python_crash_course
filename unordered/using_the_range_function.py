#working with list - Chapter 4
names = ['Carol', 'Sanie', 'Sanday', 'Steven', 'David', 'Benjamin', 'Violet']

num = list(range(1, len(names) + 1)) 
a = -1
for name in names:
	a += 1
	print(f'{num[a]} - {name}')