def string(input_string):
    # Empty String
    if input_string == "":
        print("Input is an empty string")

    # Single Character String
    elif len(input_string) == 1:
        print("Input is a single character string")

    #  Whitespace Strings
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

user_input = input("Enter your input: ")

string(user_input)
