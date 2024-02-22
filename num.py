#handling -ve integer
x = -5
x_float = float(x)
print(x_float)
print(type(x_float))

#handling large integer
x = 1e100  # A very large integer
x_float = float(x)
print(x_float)
print(type(x_float))

#handling nom-numeric input
x = input("Enter a number: ")  # Assuming user input
try:
    x_float = float(x)
    print(x_float)
    print(type(x_float))
except ValueError:
    print("Invalid input! Please enter a valid number.")



