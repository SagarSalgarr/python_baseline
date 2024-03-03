def square_numbers(numbers):
    try:
        if not isinstance(numbers, list):
            raise TypeError("Input must be a list of numbers")
        
        square = lambda x: x ** 2
        
        # Apply lambda function to each number in the list
        squared_numbers = list(map(square, numbers))
        
        return squared_numbers
    except TypeError as te:
        print(f"TypeError: {te}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
input_numbers = [1, 2, 3, 4, 5]
result = square_numbers(input_numbers)
if result:
    print("Squared numbers:", result)
