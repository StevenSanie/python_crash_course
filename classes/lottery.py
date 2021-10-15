from random import choice
codes = [1, 6, 8 , 4, 3, 0, 2, 5]

card_code = []

print('Generated Codes: ')
while len(card_code) < 2:
	code = choice(codes) 
	if code not in card_code:
		print(f"\t = {code}")
		card_code.append(code)

print(f"Winning Card: {card_code}")