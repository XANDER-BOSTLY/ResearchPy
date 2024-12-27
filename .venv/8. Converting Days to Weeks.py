# Converting days to week
# Identifying the day of the week after a given number of days from a certain day of week

num_days = int(input("By how many days do you want to go ahead in future? "))

current_day_of_the_week = input("Enter the day of the week you are starting with: ")
try:
    num_weeks = num_days // 7
    excess_days = num_days % 7

    days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    if (days_of_the_week.index(current_day_of_the_week.capitalize()) + excess_days) <= 6:
        index_final = days_of_the_week.index(current_day_of_the_week.capitalize()) + excess_days

    else:
        index_final = days_of_the_week.index(current_day_of_the_week.capitalize()) + excess_days - len(days_of_the_week)

    if excess_days >= 2:
        print(f"The day after {num_weeks} weeks and {excess_days} days is a {days_of_the_week[index_final]}.")

    elif excess_days == 1:
        print(f"The day after {num_weeks} weeks and {excess_days} day is a {days_of_the_week[index_final]}.")

    else:
        print(f"The day after {num_weeks} weeks is a {current_day_of_the_week}.")

except:
    print("Invalid input for the weekday! Please enter the entire word for the day, for instance: Monday")
