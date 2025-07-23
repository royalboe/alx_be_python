
def perform_operation(num1, num2, operation):
    """
    Perform arithmetic operations on two numbers.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform ('add', 'subtract', 'multiply', 'divide').

    Returns:
    float: The result of the arithmetic operation.
    
    Raises:
    ValueError: If an unsupported operation is provided.
    ZeroDivisionError: If division by zero is attempted.
    """
    operation = operation.strip().lower()  # Normalize the operation string
    operations = ['add', 'subtract', 'multiply', 'divide']
    if operation == operations[0]:
        return num1 + num2
    elif operation == operations[1]:
        return num1 - num2
    elif operation == operations[2]:
        return num1 * num2
    elif operation == operations[3]:
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError(f"Unsupported operation: {operation}")

    # match operation:
    #     case operations[0]:
    #         return num1 + num2
    #     case operations[1]:
    #         return num1 - num2
    #     case operations[2]:
    #         return num1 * num2
    #     case operations[3]:
    #         if num2 == 0:
    #             raise ZeroDivisionError("Cannot divide by zero.")
    #         return num1 / num2
    #     case _ as unsupported:
    #         raise ValueError(f"Unsupported operation: {operation}")
          