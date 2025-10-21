# comments in Python start with the '#' symbol.
# The purpose of comments is to explain
# the code and make it more understandable for humans
# Comments are ignored by the Python interpreter
# they are notes for anyone reading the code

# Variables are used to store values
name = "Tito"    #This is a string variable
# string variables are used to store text data
# noted by the quotation marks around the text.
age = 15         #This is an integer variable
# Integer variables are used to store whole numbers
height = 6.0     #This is a float variable
# Float variables are used to store decimal numbers
is_student = True     #This is a boolean variable
# Boolean variables are used to store True or False values.

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student", is_student)

# when we make sentences in python
# we can use the + symbol to join strings together
print("Hello, my name is " + name + ". I am " + str(age) + " years old." + " I'm around " + str(height) + " feet tall.")
# Note: We use the str() function to convert the integer 'age' to a string
# so that we can concatenate it with other strings
# this is the old or classic way of formatting strings in python.
# There are newer methods like f-strings and the format() method.
print(f"My name is {name}, I am {age} years old and {height} feet tall")
date = "2024-06-15"
weather = "sunny"
mood = "happy"
hobby = "painting"
city = "New York"
print("Today is " + date + " and the weather is " + weather + ". I feel " + mood + " while " + hobby + " in the nice city of " + city + ".")

print("we did it!")

print("we did something else")
