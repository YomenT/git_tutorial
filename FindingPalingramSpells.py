english_dictionary = ['sexes', 'apples', 'oranges', 'civic', 'madam', 'beer', 'red', 'read', 'terret', 'stats', 'solos', 'dewed', 'book', 'drink', 'laptop', 'television', 'phone', 'wallet', 'stand', 'table', 'erase', 'pencil', 'pen', 'wow', 'wood']
palingrams = []

for x in english_dictionary:
	
	if len(x) == 3 and x[0] == x[-1]:
		palingrams.append(x)

	elif len(x) == 4 or 5 and x[0] == x[-1] and x[1] == x[-2]:
		palingrams.append(x)

#	elif len(x) == 5 and x[0] == x[-1] and x[1] == x[-2]:
#		palingrams.append(x)

	elif len(x) == 6 and x[0] == x[-1] and x[1] == x[-2] and x[2] == x[-3]:
		palingrams.append(x)

	elif len(x) == 7 and x[0] == x[-1] and x[1] == x[-2] and x[2] == x[-3]:
		palingrams.append(x)

	elif len(x) == 8 and x[0] == x[-1] and x[1] == x[-2] and x[2] == x[-3] and x[3] == x[-4]:
		palingrams.append(x)

	elif len(x) == 9 and x[0] == x[-1] and x[1] == x[-2] and x[2] == x[-3] and x[3] == x[-4]:
		palingrams.append(x) 

print(palingrams)
