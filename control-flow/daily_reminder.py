"""
This script will ask the user for a single task, its priority level, and if it is time-sensitive. 
The program will then provide a customized reminder for that task, 
demonstrating control flow and loops without relying on data structures to store multiple tasks.
"""

task_description = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task_description}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task_description}' is a {priority} priority task. Consider completing it when you have free time.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task_description}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task_description}' is a {priority} priority task. Consider completing it when you have free time.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task_description}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task_description}' is a {priority} priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please enter 'high', 'medium', or 'low'.")