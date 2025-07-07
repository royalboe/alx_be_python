"""
A script that calculates the user’s monthly savings based on inputted monthly income and expenses. 
It will then project these savings over a year, assuming a fixed interest rate, to demonstrate compound interest’s effect on savings.
"""

monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

interest_rate = 0.05  # Assuming a fixed interest rate of 5%

projected_savings = int((monthly_savings * 12)  + (monthly_savings * 12 * interest_rate))

print(f"Your monthly savings are: ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")