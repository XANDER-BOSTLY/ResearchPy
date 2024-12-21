# Understanding Data Types in Python
# Common Data Types
# Numbers
3, 6, 9  # Integers (int)
3.14, -0.12  # Floats (float)

# Texts
'This is a string'  # String (str)

# Boolean
True, False  # Boolean (bool)

age = 27  # age is an integer (int)
pi = 3.14 # pi is a float (float)
name = 'Helen' # name is a string (str)
is_new = True # is_new is a boolean (boo)

#Checking data tyoes
# type() is the function used

print(type(age), type(pi), type(name), type(is_new))

# String formatting
print(f"Hello! I am {name} and I am {age} years old. My favourite number is {pi}.")

# or you can define a variable containing a string data type

personal_details = f"Hello! I am {name} and I am {age} years old. My favourite number is {pi}."
print(personal_details)

# Type conversion
str_age = str(age)
float_age = float(age)
int_pi = int(pi)

print(str_age, float_age, int_pi)
print(type(str_age), type(float_age), type(int_pi))

# Other data types are also there like: lists - lst() ; tuples - tuple() ; sets - set()
# Remember to handle potential errors and edge cases when converting data types in Python. For example, attempting to
# convert a non-numeric string to an integer using int() will raise a ValueError. Similarly, trying to convert a non-string
# value to a string using str() will also raise a TypeError.