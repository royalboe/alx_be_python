"""
This script will prompt the user to enter a positive integer, 
then use nested loops to print a square pattern of that size made of asterisks (*).
"""

while True:
    try:
        size = int(input("Enter the size of the pattern: "))
        if size <= 0:
            print("Please enter a positive integer.")
            continue
        break
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
times = size
while size:
    for i in range(times):
        print('*', end=' ')
    print()  # Print a newline after each row
    size -= 1  # Decrease the size for the next row