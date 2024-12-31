# Startup financial calculator

# Description
# You're an aspiring entrepreneur with a brilliant idea for a new software-as-as-service (SaaS) startup.
# Before pitching to investors, you need to create a financial model to project your costs, revenue,
# and break-even point. Your task is to complete a Python script that calculates these crucial financial
# metrics.

# 1. Calculate Total Startup Cost: Sum up the individual startup costs
# (development, marketing, and equipment) to get the total initial investment needed.

# 2. Project Monthly Revenue: Calculate the expected monthly revenue based on the
# number of users in each subscription tier and their respective prices.

# 3. Calculate Monthly Operating Costs: Sum up all the monthly recurring costs to
# determine your total monthly operating expenses.

# 4. Determine Monthly Profit: Subtract the monthly operating costs from the monthly
# revenue to find out how much profit (or loss) you're making each month.

# 5. Estimate Time to Break Even: Calculate how many months it will take to recover
# your initial investment based on your monthly profits.

# 6. Implement Sensitivity Analysis: Create code that adjusts the number of users
# in each tier and recalculate all financial metrics.

# 7. Format and Display Results: Use f-string to format the results nicely displaying
# currency value with commas and two decimal places, and rounding the break-even time
# to one decimal place.


# Startup Costs
dev_cost = 50000
marketing_cost = 20000
equip_cost = 10000

# Subscription Tiers
basic_tier_price = 9.99
pro_tier_price = 19.99
basic_tier_users = 1000
pro_tier_users = 500

# Monthly Operting Costs
server_cost = 1000
support_cost = 5000
misc_cost = 2000

# Total Startup Cost
total_startup_cost = dev_cost + marketing_cost + equip_cost

# Monthly Revenue
monthly_revenue = basic_tier_price * basic_tier_users + pro_tier_price * pro_tier_users

# Monthly Operating Cost (Total)
total_monthly_operating_cost = server_cost + support_cost + misc_cost

# Monthly Profit
monthly_profit = monthly_revenue - total_monthly_operating_cost

# Months to break-even
break_even_time = round(total_startup_cost / monthly_profit, 1)

# Results
print("Financial Projects:\n")
print(f"\tTotal initial investment needed to run the startup is ${total_startup_cost}.")
print(f"\tThe monthly revenue and operating costs of running the startup are ${monthly_revenue} and ${total_monthly_operating_cost} respectively.")
print(f"\tMonthly profit obtained from the startup is ${monthly_profit}.")
print(f"\tThe break-even time (in months) for the startup, that is, the time required (in months) to recover the initial investment, for the startup is {break_even_time} months.")

# Sensitivity analysis
basic_tier_users += 500
pro_tier_users += 200
monthly_revenue = basic_tier_price * basic_tier_users + pro_tier_price * pro_tier_users
monthly_profit = monthly_revenue - total_monthly_operating_cost

break_even_time = total_startup_cost / monthly_profit

print("\nSensitivity Analysis:\nUpdated Financial Projects:\n")
print(f"\tTotal initial investment needed to run the startup is ${total_startup_cost}.")
print(f"\tNew monthly revenue and operating costs of running the startup are ${monthly_revenue} and ${total_monthly_operating_cost} respectively.")
print(f"\tNew Monthly profit obtained from the startup is ${monthly_profit}.")
print(f"\tThe updated break-even time (in months) for the startup is {break_even_time:.1f} months.")