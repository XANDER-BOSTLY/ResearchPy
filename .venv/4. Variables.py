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

# Basic Variable Naming Rules.
# 1. Start with a letter or underscore (a-z, A-Z)(_)
# 2. Use letters, numbers, or underscores (az, a_)
# 3. Case sensitive (az, aZ, A_, a_)
# 4. No reserved keyword (from, del)

# Simple operations
N1 = 10
N2 = 6
# Addition
Sum = N1 + N2
print(Sum)

# Subtraction
Difference = N1 - N2
print(Difference)

# Multiplication
Product = N1 * N2
print(Product)

# Division
Quotient = N1 / N2
print(Quotient)

# Integer Division
Int_Quotient = N1 // N2
print(Int_Quotient)

# Remainder
Remainder = N1 % N2
print(Remainder)

# Exponentiation
exponent = N2 ** N1
print(exponent)

print((3 ** 4) % 5)

# print(2023 ** 2023)
# print(2023)

# def factoial(number):
#     if number > 1:
#         n = number - 1
#         while n > 1:
#             number *= n - 1
#             n -= 1
#         return number
#
#     elif number == 1 and number == 0:
#         return 1
#
#     else:
#         return "Invalid input!"


# print(factoial(0))

