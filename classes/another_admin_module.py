from user_module import User
class Admin(User):
	def __init__(self, first_name, last_name, age, gender, location):
		super().__init__(first_name, last_name, age, gender, location)
		self.privaleges = [
			'can add posts', 
			'can delete user', 
			'can delete user', 
			'can close the website'
		]

	def show_privileges(self, name):
		print(f"An admin like {name}...")
		for privilege in self.privaleges:
			print(f"\t * {privilege}")


