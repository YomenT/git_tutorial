class Employee:

	number_of_employees = 0
	raise_amount = 1.03
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + "." + last + "@company.com"
#		Employee.number_of_employees += 1

	def fullname(self):
		print(self.first.title() + " " + self.last.title())

	def apply_raise(self):
		self.pay = self.pay * self.raise_amount
		print("Your raise added onto your salary is: " + str(self.pay))

#	@classmethod
#	def set_raise_amount(cls, amount)
#		cls.raise_amount = amount

#We are now inheriting all of the attributes and methods from the Employee class.
class Developer(Employee):

	raise_amount = 1.10

	def __init__(self, first, last, pay, programming_language):
		super().__init__(first, last, pay)
		self.programming_language = programming_language

	def preffered_language(self):
		print("Preffered Language: " + self.programming_language.title())

class Manager(Employee):

	def __init__(self, first, last, pay, employee = None):
		super().__init__(first, last, pay)
		if employee is None:
			self.employee = []

		else:
			self.employee = employee

	def add_employee(self, emp):
		if emp not in self.employee:	
			self.employee.append(emp)

	def remove_employee(self, emp):
		if emp in self.employee:
			self.employee.remove(emp)

	def print_employee(self):
		for x in self.employee:
			print("--->" + x.title())

manager_1 = Manager('Yomen', 'Tohmaz', 50000, [ben])
dev_1 = Developer('Yomen', 'Tohmaz', 50000, 'Python')
#emp_1 = Employee('Yomen', 'Tohmaz', 50000)

manager_1.fullname()
#dev_1.fullname()
#dev_1.preffered_language()
#emp_1.fullname()
#emp_1.apply_raise()
#print(Employee.number_of_employees)
#Employee.set_raise_amount(1.05)
#print(Employee.raise_amount)
#You can also call the method through the class by using the following syntax.
#Employee.fullname(emp_1)
#This will do the exact same thing as line 15.
