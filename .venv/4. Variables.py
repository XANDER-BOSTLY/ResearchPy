# Variables store data types for future use
# Variable names comprise of lettrs, numbers and underscore(s)
# The variable names cannot start with numbers

num1 = 5  # variable storing an integer data type
num2 = -9.6  # variable storing an float data type
name = 'John Smith'  # variable storing an string data type
Name = 'Heron'  # variable name is case sensitive. So, name and Name are two different variables
Is_stupid = False  # variable storing an boolean data type

# Operations on variables
result = num1 + num2
print(result)
# Variables can be redefined
result += 1 # same as result = result + 1
print(result)

result *= 10 # same as result = result * 10
print(result)

# Variable values can be overwritten
print(name)
name = "Samuel Garrison"
print(name)

# Basic Variable Naming Rules
# 1. Start with a letter or underscore (a-z, A-Z)(_)
# 2. Use letters, numbers, or underscores (az, a_)
# 3. Case sensitive (az, aZ, A_, a_)
# 4. No reserved keyword (from, del)