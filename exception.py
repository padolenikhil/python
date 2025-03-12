def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"The result is {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Both inputs must be numbers.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Test the function
divide_numbers(10, 2)  # Expected output: The result is 5.0
divide_numbers(10, 0)  # Expected output: Error: Division by zero is not allowed.
divide_numbers(10, 'a')  # Expected output: Error: Both inputs must be numbers.
