vowel_list = ['a', 'e', 'i', 'o', 'u']

print("Type quit at any time to exit the program.")
print(" ")

var_1 = ''

while var_1 != 'quit':

	var_1 = input("Type the word you wish to convert to pig latin: ")
	var_2 = var_1[0]
	var_3 = var_1[1:]

	if var_1 == 'quit':
		print("Exiting...")

	elif var_2 in vowel_list:
		print("The translated word is: " + var_1 + "way")

	else:
		print("The translated word is: " + var_3 + var_2 + "ay")
