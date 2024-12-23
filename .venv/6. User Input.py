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

try:
    temp = input("Type a number to add: ")  # Indentation is mandatory in Python. It helps in distinguishing blocks of code.
    print("100 + {} = {}".format(int(temp), 100 + int(temp)))
except:
    print("Invalid input! Please try giving an integer value.")
print("The program is successfully executed!")