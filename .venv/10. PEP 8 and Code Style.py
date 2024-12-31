# PEP 8 and code style
from email.policy import EmailPolicy
from inspect import AGEN_CLOSED


# Indentation
# PEP 8 suggests keeping 4 spaces for indentation
# Proper Indentation

def greet(name):
    print(f"Hello, {name}!")
    print("Welcome to Python!")
    print("Let's learn about PEP 8!")

# Line Length
# PEP 8 suggests keeping lines of code to a maximum of 79 characters

# very_long_variable_name = some_long_function_name(
#     long_argument1,
#     long_argument2,
#     long_argument3,
#     long_argument4
# )

# Naming Conventions
# snake_case for functions and variables
# PascalCase for classes
# UPPER_CASE for constants

def calculate_area(length, width):
    return length * width

my_variable = 42

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("Woof!")
#
# my_dog = Dog("Fido", 3)
# print(my_dog.name)  # Output: Fido
# my_dog.bark()  # Output: Woof!

MAX_SPEED = 120  # This value won't change, according to its name at least!!

# Whitespace
x = 5
y = x + 1
languages = ['Python', 'Javascript', 'C++']

# # Practice Exercise

# def CALCULATE_sum(a,b):
#     return a+b
#
# result=CALCULATE_sum(10,20)
# print("The sum is: "+str(result))

def calculate_sum(a, b):
    return a + b

result = calculate_sum(10, 20)
print(f"The sum is: {result}")

# Exercise
# class userAccount:
#     def **init**(self,UserName,Email,Age):
#         self.UserName=UserName
#         self.Email=Email
#         self.Age=Age
#
#     def display_INFO(self):
#         print(f"User: {self.UserName}, Email: {self.Email}, Age: {self.Age}")

# Corrected Code
class UserAccount:
    def __init__(self, user_name, email, age):
        self.user_name = user_name
        self.email = email
        self.age = age

    def display_INFO(self):
        print(f"User: {self.user_name}, Email: {self.email}, Age: {self.age}")


# import os,sys
# import numpy as np
# from datetime import datetime,date,time
# **version**='1.0.0'
# **author**="John Doe"

# Multiple imports on one line
# Inconsistent import formatting
# Incorrect dunder name formatting

# Corrected code according to the PEP 8 rules

import os
import sys  # It is good to write the standard libraries import first
# and then the seconf party imports
# Thus a blank line to separate them

# import numpy as np
from datetime import date, datetime, time  # Proper import formatting

__version__ = '1.0.0'  # Dunder names correct name formatting
__author__ = "John Doe"

# Exercise

def process_data(
        data,
        filter_condition,
        transform_function,
        output_format,
        debug_mode = False,
        log_file = 'process.log',
        max_iterations = 1000
):
    # Process the data here
    pass

def factorial(n):
    """
    Calculate factorial of a number.
    Arg:
        n (int): The number to calculate the factorial for.

    Returns:
        int: the factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# if x == 5: print("x is 5"); y = 1
# Corrected Code
if x == 5:
    print("x is 5")
    y = 1

long_string = (
    "This is a very long string that exceed the recommended maximum "
    "line length of 79 characters in PEP 8. It should be formatted properly."
)

# print(long_string)