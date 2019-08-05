import random
import time

first_names = ['saad', 'chris', 'dick', 'paul', 'harry', 'moe', 'ethan', 'larry', 'curly', 'shemp', 'al', 'adam', 'amanda', 'barry'] 
last_names = ['long', 'perv', 'twocock', 'lester', 'condom', 'howard', 'fine', 'swett', 'maan', 'bino', 'fresco', 'seltzer', 'cade']

print("This program is a random name generator.")
print(" ")
print("To continue to randomly generate names, type 'generate'.")
print(" ")
print("To quit this program, type 'quit'.")
print(" ")
print(" ")
time.sleep(1)
a = raw_input("Shall we begin? (yes/no)  ")

if a == 'yes':
    print(random.choice(first_names).title() + " " + random.choice(last_names).title()) 
    
    x = " "
    while x != 'quit':
        x = raw_input("Continue or quit? (generate/quit)  ")
        random_first_name = random.choice(first_names) 
        random_last_name = random.choice(last_names)

        if x == 'generate':
            print(random_first_name.title() + " " + random_last_name.title()) 
        
        elif x == 'quit':
            print("Exiting...")

        else:
            print("Please type a valid answer.")

    
