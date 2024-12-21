# Strings in python

greeting = "Hello, world!"
name = "Alice"

# Finding the length of a string
length = len(greeting)  # len() function is used to get the length of a string
print(f"The string 'Hello, world!' is {length} characters long.")

# Indexing
# Gives the letter of the string at the specfiied index of the string
# positive indices start from 0
# negative indices start from -1
print(greeting[0])
print(greeting[1])
print(greeting[2])
print(greeting[3])
print(greeting[4])
print(greeting[5])
print(greeting[6])
print(greeting[7])
print(greeting[8])
print(greeting[9])
print(greeting[10])
print(greeting[11])
print(greeting[12])
print(greeting[-1])
print(greeting[-10])
print(greeting[-12])

# Slicing
# The syntax is string[start:end:step]
print(greeting[0:5])  # starts slicing before greeting[0] and ends slicing before greeting[5]
# Will display the indices 0, 1, 2, 3 and 4
print(name[1:3])  # will display the indices 1 and 2
print(greeting[::2])
# when nothing is mentoned in start and end, the value defaults to the first and the last indices
# respectively. The step instructs the interpreter to display the values of the indices at the said interval
# here, it starts at 0 then displays the second index after it (0+2 = 2) then the second one after that, and so on
# INDEXING IS A SPECIAL CASE OF SLICING. We just mention the starting index. Since, there is no ending index, the
# interpreter only displays the mentioned index

print(greeting[::-1])  # Negative step values reverse the order of the string

# Concatenation
full_name = name + ' in the Wonderland!'
print(full_name)

# Repetition
chant = name * 3
print(chant)

# String methods
# Syntax string.method()
print(greeting.upper())
print(name.lower())
print(name.replace('l', 'x'))
print(name.isupper())
print(name.isnumeric())