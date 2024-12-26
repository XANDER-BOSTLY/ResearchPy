# # '+' for addition
# # '-' for subtraction
# # '*' for multiplication
# # '/' for division
# # '//' for integer division
# # '%' for finding remainder
#
# wallet = 50  # you start with $50
# # Buy some itmes
# book = 15
# snack = 5
# drink = 3
# # Calculate total amount spent
# total_spent = book + snack + drink
# # Calculate the remaining money
# money_left = wallet - total_spent
#
# print(f"You have spent ${total_spent}, and are thus left with ${money_left} in your wallet.")


# Personal Savings Calculator

# month1 = 43.0
# month2 = 56.0
# month3 = 168.0
#
# list_of_months = [month1, month2, month3]
#
# total_savings = month1 + month2 + month3
#
# num_month = len(list_of_months)
# avg_savings = total_savings / num_month
#
# print("The savings in the first, second and third months are ${}, ${} and ${} respectively. The total savings in the {} months is ${}. The average savings, thus, are ${}.".format(month1, month2, month3, num_month, total_savings, avg_savings))
#
# month4 = float(input("Enter your savings this month: $"))
# # list_of_months.insert(4, month4)  # For adding an item at a specific index
# list_of_months.append(month4)  # Adds an item at the end of the list
#
# # print(list_of_months)
# num_month_updated = len(list_of_months)
# total_savings_updated = list_of_months[3] + total_savings
# avg_savings_updated = total_savings_updated / num_month_updated
#
# print(f"The savings in the fourth month are ${month4}. The total and average savings at the end of the fourth month are ${total_savings_updated} and ${avg_savings_updated:.0f} respectively.")
#
# # Calculating what percentage of each monhs savings contribute to the total
#
# def percent_contribution(month):
#     return round((month / total_savings_updated) * 100, 2)
#
#
# percent_contribution_month1 = percent_contribution(month1)
# percent_contribution_month2 = percent_contribution(month2)
# percent_contribution_month3 = percent_contribution(month3)
# percent_contribution_month4 = percent_contribution(month4)
#
# print(f"The percent contributions of each month's savings to the total savings are {percent_contribution_month1}%, {percent_contribution_month2}%, {percent_contribution_month3}% and {percent_contribution_month4}%.")

# SPLITTING A BILL CALCULATOR

my_dict = {"rupees" : "₹"}

# Items
# Starters
veg_chowmein = 20
chicken_chowmein = 30
paneer_nuggets = 15
chicken_nuggets = 25
mushroom_nuggets = 10
harabhara_kabab = 10
fish_nuggets = 20

# Main course
naan = 10
rice = 7
chilli_paneer = 30
paneer_65 = 25
chilli_chicken = 35
chicken_tikka_masala = 40
fish_fry = 25
curd = 15
salad = 15

# Dessert
kheer = 15
vanilla_icecream = 20
butterscotch = 20
malpua = 20
rabdi = 25
rasagula = 20
chenna_podo = 30

# Friends
tim = [veg_chowmein, paneer_nuggets, mushroom_nuggets, harabhara_kabab, naan, chilli_paneer, paneer_65, curd, salad, butterscotch, chenna_podo]
robin = [chicken_nuggets, mushroom_nuggets, fish_nuggets, chilli_chicken, rice, naan, fish_fry, malpua, rabdi, rasagula]
sam = [chicken_chowmein, paneer_nuggets, chicken_nuggets, fish_nuggets, naan, rice, chicken_tikka_masala, curd, salad, paneer_65, kheer, chenna_podo, rabdi, vanilla_icecream]

friends = [tim, robin, sam]
expense = 0
friends_expenses = []

for friend in friends:
    i = 0
    while i < len(friend):
        expense += friend[i]
        i += 1
    friends_expenses.append(expense)
    expense = 0

total_expenses = 0
j = 0
while j < len(friends_expenses):
    total_expenses += friends_expenses[j]
    j += 1

tips_percent = 0.15
tips_amount = tips_percent * total_expenses
total_with_tips = total_expenses + tips_amount

each_friend_share = round(total_with_tips / len(friends), 2)

print(f"Three friends visited a restaurant. Their total expenses (tips included) was {my_dict["rupees"]}{total_with_tips}. Each friend had to pay {my_dict["rupees"]}{each_friend_share}.")

# print(friends_expenses)

# tim_expenses = 0
# i = 0
#
# while i < len(tim):
#     tim_expenses += tim[i]
#     i += 1
#
# print(f"Tim's expenses are {my_dict["rupees"]}{tim_expenses}.")
# expense = 0

# robin_expenses = 0
# j = 0
#
# while j < len(robin):
#     robin_expenses += robin[j]
#     j += 1
#
# print(f"Robin's expenses are {my_dict["rupees"]}{robin_expenses}.")
#
# sam_expenses = 0
# k = 0
#
# while k < len(sam):
#     sam_expenses += sam[k]
#     k += 1
#
# print(f"Robin's expenses are {my_dict["rupees"]}{sam_expenses}.")
#
# total_expenses = tim_expenses + robin_expenses + sam_expenses
# total_expenses *= 1.15  #  15% tips also added
#
#
# def percent_contribution(friend):
#     return round((friend / total_expenses) * 100, 2)
#
#
# tim_share = percent_contribution(tim_expenses)
# robin_share = percent_contribution(robin_expenses)
# sam_share = percent_contribution(sam_expenses)
#
# amount_to_be_paid_by_each = total_expenses / len(friends)
#
# print(f'Each friend has to pay {my_dict["rupees"]}{amount_to_be_paid_by_each:.2f}.')
# print(f'Tim has contributed to {tim_share}% of the total expenses.')
# print(f'Robin has contributed to {robin_share}% of the total expenses.')
# print(f'Sam has contributed to {sam_share}% of the total expenses.')