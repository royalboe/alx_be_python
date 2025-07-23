
def perform_operation(num1: float, num2: float, operation: str) -> float:
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
    
    match operation.lower():
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'multiply':
            return num1 * num2
        case 'divide':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            return num1 / num2
        case _ as unsupported:
            raise ValueError(f"Unsupported operation: {operation}")
          