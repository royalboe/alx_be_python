"""
This script will ask the user to enter a number, then use a for loop to print the multiplication table for that number from 1 to 10.
"""

while True:
    try:
        number = int(input("Enter a number to see its multiplication table: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")