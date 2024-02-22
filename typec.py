def addition(a, b):
    print("Type of first number(a) :", a, type(a))
    print("Type of second number(b) :", b, type(b))
    c = a + b
    print("Type of resulting variable(c) :",  c, type(c))

addition(21, 23)  
print('\n')
addition(21, 23.0) 
print('\n')
addition(21.0, 23) 
addition(21.0, 23.0) 


# x = 'abc'  # Non-numeric input
# x_float = float(x)
# print(x_float)
# print(type(x_float))

# a = '1.5e3'  # Scientific notation string
# a_float = float(a)
# print(a_float)
# print(type(a_float))

def convert_to_float(x):
    try:
        x_float = float(x)
        return x_float, type(x_float)
    except ValueError:
        return None, None  

if __name__ == "__main__":
    test_values = [10, '10', '10.5', 'abc', 1e100, -5 ,'1.5e3']
    for val in test_values:
        result, data_type = convert_to_float(val)
        if result is not None:
            print(f"Converted value: {result}")
            print(f"Data type: {data_type}")
        else:
            print(f"Failed to convert: {val}")


