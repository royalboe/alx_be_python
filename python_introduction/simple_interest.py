"""
Python script that calculates the simple interest earned on an investment over a period of time. The formula for simple interest is (I = P * R * T), where:

( I ) is the interest earned,
( P ) is the principal amount (initial investment),
( R ) is the annual interest rate (as a decimal),
( T ) is the time the money is invested for in years.
"""

principal = 1000 # Initial investment amount
rate = 0.05  # 5% interest rate
time = 3  # 3 years

# Calculate simple interest
interest = principal * rate * time

# Print the result
print(f"The simple interest is: {interest:.1f}")
      