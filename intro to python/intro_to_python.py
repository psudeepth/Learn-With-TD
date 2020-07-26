# Youtube Link: https://youtu.be/dtEYQWjjZA8

# "#" is used to comment out a line in python. what ever is preciding the # will not read by the python execuiter.

# Variables

# string:
	varName = "This is a string"

# Integer
	varName = 10

# float
	varName = 10.5

# vector
	varName = (10.3, 5, 40.6)

# Matrix
	varName[5][5] = [[0, 0, 0, 0, 0,]
					 [0, 0, 0, 0, 0,]
					 [0, 0, 0, 0, 0,]
					 [0, 0, 0, 0, 0,]
					 [0, 0, 0, 0, 0,]]

# Dictionary
	varName = {Key: Value}
	varName = {"One": "The first value"}

# Array
	varName = [1, 2, "This can be a string", 4, 5.5, [6, 7, 8, 9], 10]

# tuple
	varName = (1, 2, "This can be a string", 4, 5.5, 10)

# IF Condition
	# Syntax
		if Condition:
			statement
		else:
			statement

	# elif
		if Condition:
			statement
		elif:
			statement
		else:
			statement

	# nested if
		if Condition:
			if Condition:
				if Condition:
					statement
				else:
					statement
			else:
				statement
		else:
			statement

# Loop
	varName = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	for each in varName:
		print(each)

# If Condition in a Loop
	varName = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	for each in varName:
		if each == 5:
			print("{} is equal to 5".format(each))
		elif each > 5:
			print("{} is greater than 5".format(each))
		else:
			print("{} is less than 5".format(each))


# I missed out something in the video i will explain it here.
"""
I really missed out something that when using variables in python you have to be very careful 
In other languages once a variable is declared you cannot change the variable type
But in python you can change one variable type to another variable type.
For the better understanding you can follow the below example.
"""

a = "This is a string"
print(a)

a = 10
print("Now the value of a is {}, what do you think it is".format(a))
		


