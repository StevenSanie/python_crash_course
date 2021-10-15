class User:
	def __init__(self, first_name, last_name, age, gender, location):
		self.f_name = first_name
		self.l_name = last_name
		self.age = age
		self.gender = gender
		self.location = location
		self.login_attempts = 0

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0

	def describe_user(self):
		print(f"{self.f_name.title()} is a {self.age} year old "
			f"{self.gender} who lives in {self.location.title()}.")
	

	def greet_user(self):
		full_name = f"{self.f_name} {self.l_name}"
		print(f"Hello {full_name.title()}, How are you?")

# Created an instance
user_1 = User('Sanie', 'Stevens', 23, 'Male', 'New York')

# print and increment the login attempts
for i in range(1, 6):
	print(f"{i}. Login Attempt: {user_1.login_attempts}")
	user_1.increment_login_attempts()

# Reset user login attempts back to 0
user_1.reset_login_attempts()
print(f"\n\t Login Attempts Resetted To: {user_1.login_attempts}")
