from random import randint 

class Dice:
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		side = randint(1, self.sides)
		print(f"The die is on number {side}, and has {self.sides} sides!")

for i in range(10):
	Dice(20).roll_die()