# # This prograam calculates the volume of the cube
#
# try:
#     cube_edge = float(input("Enter the edge length of the cube: "))
#
#     cube_volume = cube_edge ** 3
#     cube_surface_area = 6 * (cube_edge ** 2)
#
#     print(f"The volume and the surface area of the cube, with its edge {cube_edge} units long, are {cube_volume} cubic units and {cube_surface_area} square units respectively.")
#
# except:
#     print("Invalid input! Please enter a number.")


# # Movie theatre seating arrangement
#
# total_seats = int(input("Enter the total number of seats in the theatre: "))
# num_rows = []
# num_columns = []
# group_size = int(input("Enter your desired group size: "))
#
# n = group_size
# while n <= total_seats:
#     if total_seats % n == 0:
#         num_columns.append(n)
#         num_rows.append(total_seats // n)
#         n += 1
#     else:
#         n += 1
#
# # print(num_rows, num_columns)
#
# remaining_seats = []
#
# for row_size in num_columns:
#     remaining_seats_in_each_row = row_size % group_size
#     total_remaining_seats = remaining_seats_in_each_row * num_rows[num_columns.index(row_size)]
#     remaining_seats.append(total_remaining_seats)
#
# # print(remaining_seats)
#
# optimum_row_size = num_columns[remaining_seats.index(min(remaining_seats))]
#
# print(f"For {total_seats} seats in total with a group having {group_size} individuals the optimum seating arrangement is {optimum_row_size} seats in a row and {total_seats // optimum_row_size} rows. This arrangement has the minimum number of empty seats left, that is, {min(remaining_seats)}.")

# Decode the secret message

# import random
#
# my_dict = {"1th":"first", "2th":"second", "3th":"third", "4th":"fourth", "5th":"fifth", "6th":"sixth", "7th":"seventh", "8th":"eighth", "9th":"ninth", "10th":"tenth", "11th":"eleventh", "12th":"twelfth", "13th":"thirteenth", "14th":"fourteenth", "15th":"fifteenth", "16th":"sixteenth", "17th":"seventeenth", "18th":"eighteenth", "19th":"nineteenth", "20th":"twentieth", "21th":"twenty-first", "22th":"twenty-second", "23h":"twenty-third", "24th":"twenty-fourth", "25th":"twenty-fifth", "26th":"twenty-sixth", }
#
# list_of_num = []
# n = 1
# while n <= 26:
#     list_of_num.append(n)
#     n += 1
#
# # print(list_of_num)
#
# random.shuffle(list_of_num)
# secret_message = list_of_num
# # print(secret_message)
#
# last_letter_the_secret_message = secret_message[-1]
# # print(last_letter_the_secret_message)
#
# alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# decoded_last_letter = alphabets[last_letter_the_secret_message - 1]
# # print(decoded_last_letter)
#
# print(f"The last letter of the secret message is {last_letter_the_secret_message} which is decoded to the {my_dict[str(last_letter_the_secret_message) + 'th']} letter in the English alphabets, that is '{decoded_last_letter}'.")
#
# # print(int(chr(2)))

encoded_message = 1233248916372176407
# The message is the number of digits in the sequence of letters: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEF............

last_digit = encoded_message % 26

decoded_letter = chr(65 + last_digit)
# chr() takes an integer input between 0 and 1,114,111 and gives the Unicode code character corresponding to the number
# 65 - A
# 97 - a
# ord() is the inverse of chr()

print(f"The last letter of the secret message is '{decoded_letter}'")
