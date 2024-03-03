# corner case related to string manipulation using built-in functions
def string(input_string):
    try:
        uppercased = input_string.upper()

        words = uppercased.split()

        reversed_words = words[::-1]

        reversed_string = ' '.join(reversed_words)

        return reversed_string
    except AttributeError:
        print("Error: Input must be a string.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

input_string = "Hello World"
reversed_string = string(input_string)
print("Reversed String:", reversed_string)
