"""
This calculator will prompt the user to enter two numbers and select an operation (addition, subtraction, multiplication, or division). 
The script will then perform the selected operation using a Match Case statement and display the result.
"""

while True:
  try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    break
  except ValueError:
    print("Invalid input. Please enter numeric values.")


operation = input("Choose the operation (+, -, *, /): ").strip()
result = None

match operation:
    case '+':
        result = f"The result is {num1 + num2}."
    case '-':
        result = f"The result is {num1 - num2}."
    case '*':
        result = f"The result is {num1 * num2}."
    case '/':
        if num2 != 0:
            result = f"The result is {num1 / num2}."
        else:
            result = "Cannot divide by zero."
    case _:
        result = "Error: Invalid operation selected."

print(result)