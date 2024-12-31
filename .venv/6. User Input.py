# temp = input("Type a number to add: ")
# # Default type of the input is string
# # We need to convert to integer or float before operating on it (in this case)
# print(type(temp))
#
# result = 100 + int(temp)
# print("100 + {} = {}".format(temp, result))
# Another way of writing formatted strings
# Use .format() string method

# However, as a developer, one should expect that the user might not input an integer
# If temp variable stores a non-integer string data type
# then the application of int() function will result in an error message and the code will stop running
# To handle such errors in user input, we use TRY AND EXCEPT BLOCKS

# try:
#     temp = input("Type a number to add: ")  # Indentation is mandatory in Python. It helps in distinguishing blocks of code.
#     print("100 + {} = {}".format(int(temp), 100 + int(temp)))
# except:
#     print("Invalid input! Please try giving an integer value.")
# print("The program is successfully executed!")

# name = input("What's your name? ")
# print("Hello! " + name + ". Good Morning!")
#
# # We can also use the datetime module!
# from datetime import datetime
# # current_year = 2024
#
# age = input("How old are you? ")
# current_year = datetime.now().year
#
# birth_year = current_year - int(age)
#
# print(f"Wow! You were born in {birth_year}.")

# def greet(name):
#     print(f"Hello! {name}. Welcome to Python! Let's lunge into this vast and "
#           "immense world of Programming!!")
#
# name = input("What might thy pristine and divine self be christened as? ")
# greet(name)
#
# print("The following is an Echo Check: \nPlease enter a message. "
#       "This program will return back exactly the same.")
# user_msg = input("Your message: ")
# print(f"The output: {user_msg}")

# PERSONAL INFO COLLECTOR
#
# name = input("Enter your name: ")
# age = input("Enter your age: ")
# hometown = input("Enter your hometown: ")
# print(f"{name} is {age} years old and hails from {hometown}.")

# human_age = int(input('Enter your age: '))
# dog_age = human_age * 7
# print(f"Woof! Woof! You are {dog_age} years old in dog years. Woof!")

# Simple Calculator
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
#
# operations = ['+', '-', '*', '/']
#
# desired_operation = input("Enter the opertion you wish "
#                           "to perform (+, -, *, /): ")
#
# if operations.index(desired_operation) == 0:
#     result = num1 + num2
# elif operations.index(desired_operation) == 1:
#     result = num1 - num2
# elif operations.index(desired_operation) == 2:
#     result = num1 * num2
# elif operations.index(desired_operation) == 3:
#     result = round(num1 / num2, 2)
# else:
#     print("Invalid Operation! Please rerun the program.")
#
# print(f"{num1} {desired_operation} {num2} = {result}")

# Mad Libs
# Create a simple mad libs game

# noun = input("Enter a noun: ")
# adjective = input("Enter an adjective to describe the noun: ")
# count = input("State if the noun is supposed to be "
#               "used in singular or plural form: ")
# verb = input("Enter the base form of the verb: ")
# tense = input("Enter the desired tense for the "
#               "verb (past indefinite, past continuous, "
#               "present indefinite, present continuous, "
#               "future indefinite, future continuous): ")
#
# if count == "singular":
#     if tense == "past indefinite":
#         statement = f"The {adjective} {noun} {verb + "ed"}."
#     elif tense == "past continuous":
#         statement = f"The {adjective} {noun} {"was " + verb + "ing"}."
#     elif tense == "present indefinite":
#         statement = f"The {adjective} {noun} {verb + "s"}."
#     elif tense == "present continuous":
#         statement = f"The {adjective} {noun} {"is " + verb + "ing"}."
#     elif tense == "future indefinite":
#         statement = f"The {adjective} {noun} {"will " + verb}."
#     elif tense == "future continuous":
#         statement = f"The {adjective} {noun} {"will be " + verb + "ing"}."
#     else:
#         print("Invalid input")
# elif count == "plural":
#     if tense == "past indefinite":
#         statement = f"The {adjective} {noun + "s"} {verb + "ed"}."
#     elif tense == "past continuous":
#         statement = f"The {adjective} {noun + "s"} {"were " + verb + "ing"}."
#     elif tense == "present indefinite":
#         statement = f"The {adjective} {noun + "s"} {verb}."
#     elif tense == "present continuous":
#         statement = f"The {adjective} {noun + "s"} {"are " + verb + "ing"}."
#     elif tense == "future indefinite":
#         statement = f"The {adjective} {noun + "s"} {"will " + verb}."
#     elif tense == "future continuous":
#         statement = f"The {adjective} {noun + "s"} {"will be " + verb + "ing"}."
#     else:
#         print("Invalid input")
# else:
#     print("Invalid input")
#
# print(f"Your statement is: {statement}")
