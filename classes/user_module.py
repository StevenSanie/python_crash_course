class User:
	def __init__(self, first_name, last_name, age, gender, location):
		self.f_name = first_name
		self.l_name = last_name
		self.age = age
		self.gender = gender
		self.location = location


	def describe_user(self):
		print(f"{self.f_name.title()} is a {self.age} year old "
			f"{self.gender} who lives in {self.location.title()}.")
	

	def greet_user(self):
		full_name = f"{self.f_name} {self.l_name}"
		print(f"Hello {full_name.title()}, How are you?")
