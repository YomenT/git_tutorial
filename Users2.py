class User:

	number_of_attempts = 0

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def describe_user(self):
		print("First Name: " + self.first_name)
		print("Last Name: " + self.last_name)

	def greet_user(self):
		print("Hello, " + self.first_name + " " + self.last_name + "!") 

	@classmethod
	def increment_login_attempts(cls):
		cls.number_of_attempts = cls.number_of_attempts + 1 
		print("Number of login attempts: " + str(cls.number_of_attempts))

class Admin(User):

	def __init__(self, first_name, last_name):
		super().__init__(first_name, last_name)
		self.privileges = ['Can ban users', 'Can add posts', 'Can delete posts']

	def show_privileges(self):
		print("Here are some privileges unique to an admin...")
		for x in self.privileges:
			print(x)

admin = Admin('Yomen', 'Tohmaz')

admin.show_privileges()

"""
user1 = User('Yomen', 'Tohmaz')
print ("number of objects so far: "+str(User.numberObj))
user2 = User('Mosab', 'Tohmaz')
print ("number of objects so far: "+str(User.numberObj))
user3 = User('Mahmoud', 'Tohmaz')
print ("number of objects so far: "+str(User.numberObj))

user1.describe_user()
user1.greet_user()
User.increment_login_attempts()
print(" ")
user2.describe_user()
user2.greet_user()
user2.testit()
user1.testit()
User.increment_login_attempts()
print(" ")
user3.describe_user()
user3.greet_user() 
User.increment_login_attempts()
"""
