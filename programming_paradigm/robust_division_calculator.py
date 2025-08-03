def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return
    except ValueError:
        print("Error: Please enter numeric values only.")
        return
    else:
        return f"The result of the division is {result:.1f}"
