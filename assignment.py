# Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.
# Handle Multiple Exceptions:
class NegativeNumberError(Exception):
    def __init__(self, message="Number cannot be negative."):
        self.message = message
        super().__init__(self.message)


def check_positive(number):
    if number < 0:
        raise NegativeNumberError()


try:
    check_positive(-5)
except NegativeNumberError as e:
    print(e)


# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.

def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except TypeError:
        print("Error: Inputs must be numbers.")
    except ValueError:
        print("Error: Inputs must be convertible to floats.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




safe_divide(10, 0)  # ZeroDivisionError
safe_divide(10, 'a')  # TypeError
safe_divide('10', 2)  # ValueError
