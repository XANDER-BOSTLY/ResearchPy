# This script converts a temperature from celsius to fahrenheit units
# Author: Swayambhuba Pattanayak
# Date: 22/12/2024
# Rev.:


days_in_week = 7
celsius_temp = 423.5678  # Temperature to convert
pi = 3.14159  # Example of a float constant

greetings = "Hello, "
user_name = "Wika"

is_summer = True

month = ["January", "February", "March"]

temp_scales = {"Celsius" : "°C", "Fahrenheit" : "°F"}
# Can also be written as
# temp_scales = dict(Celsius = "°C", Fahrenheit = "°F")
# or list of tuples
# temp_scales = dict([("Celsius", "°C"),("Fahrenheit", "°F")])
# key - value pairs

celsius_to_fahrenheit_factor = 9/5
fahrenheit_offset = 32

fahrenheit_temp = (celsius_temp * celsius_to_fahrenheit_factor) + fahrenheit_offset
fahrenheit_temp = round(fahrenheit_temp, 2)  # Rounds off the result to 2 decimal places

full_greeting = greetings + user_name

shouted_greeting = full_greeting.upper()
whispered_greeting = full_greeting.lower()

month_count = len(month)  # Gets the length of strings or lists

output1 = str(celsius_temp) + temp_scales["Celsius"] + " is equal to " + str(fahrenheit_temp) + temp_scales["Fahrenheit"] + "."

output2 = f"{celsius_temp}{temp_scales["Celsius"]} is equal to {fahrenheit_temp}{temp_scales["Fahrenheit"]}."

print(full_greeting)
print(shouted_greeting)
print(whispered_greeting)
print(f"Number of months in the list: {month_count}")
print(output1)
print(output2)
print(f"Is it summer right now? {is_summer}")
print(f"There are {days_in_week} days in a week, and pi is approximately {pi:.3f}")