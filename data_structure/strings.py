import json

def handle_input(input_string):
    # Check if input is a valid JSON string
    
        json_object = json.loads(input_string)
        print("Input is a valid JSON string. Type:", type(json_object))
        # Empty String
        if input_string == "":
            print("Input is an empty string")

        # Single Character String
        elif len(input_string) == 1:
            print("Input is a single character string")

        # Whitespace Strings
        elif input_string.isspace():
            print("Input consists entirely of whitespace characters")

        # Case Sensitivity
        elif input_string.lower() != input_string.upper():
            print("Input contains mixed case characters")

        # Strings with Leading or Trailing Whitespace
        elif input_string != input_string.strip():
            print("Input contains leading or trailing whitespace")
        
         

        else:
            print("Input does not match any specific corner case")

# Take input from the user
user_input = input("Enter your input: ")

# Process the input
handle_input(user_input)
