import random

join_year = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]

class Users(object):
	def __init__(x, first_name, last_name, age):
		x.first_name = first_name
		x.last_name = last_name
		x.age = age
		x.login_attempts = 0

	def describe_users(x):
		print("Name: " + x.first_name.title() + " " + x.last_name.title()) 
		print("Age: " + str(x.age)) 
		print("Year Joined: " + str(random.choice(join_year))) 

	def greet_users(x):
		print("Hello, " + x.first_name.title() + " " + x.last_name.title())

	def increment_login_attempts(x):
		x.login_attempts += 1

	def reset_login_attempts(x):
		x.login_attempts = 0

	def print_login_attempts(x):
		print("Login Attempts: " +str(x.login_attempts))

user1 = Users('yomen', 'tohmaz', 20)
user2 = Users('mosab', 'tohmaz', 22)
user3 = Users('mahmoud', 'tohmaz', 24)

user1.describe_users()
user1.greet_users()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.print_login_attempts()
user1.reset_login_attempts()
user1.print_login_attempts()
print(" ")
user2.describe_users()
user2.greet_users()
print(" ")
user3.describe_users()
user3.greet_users()
