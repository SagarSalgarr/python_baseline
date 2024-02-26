import math


def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero is not allowed."

print("Result of 10 divided by 0:", safe_divide(10, 0))  # Output: Division by zero is not allowed.

# Square root of negative number
def safe_square_root(a):
    try:
        result = math.sqrt(a)
        return result
    except ValueError as e:
        if str(e) == "math domain error":
            return "Square root of a negative number is not allowed."
        else:
            return f"An unexpected error occurred: {e}"

print("Square root of -4:", safe_square_root(-4))  # Output: Square root of a negative number is not allowed.

# Overflow error
def safe_power(a, b):
    try:
        result = a ** b
        return result
    except OverflowError:
        return "Result too large to compute."

print("10 raised to the power of 1000:", safe_power(10, 1000))  # Output: Result too large to compute.

# Undefined result (e.g., 0 divided by 0)
def handle_undefined_result():
    a = 0
    b = 0
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Result is undefined (0 divided by 0)."

print("Result of 0 divided by 0:", handle_undefined_result())  # Output: Result is undefined (0 divided by 0).
