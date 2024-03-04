x=4
y="t"
print(x is y)


x=4
y="t"
print(x is not y)

def check_membership():
    # Empty list
    empty_list = []
    if 1 in empty_list:
        print("1 is in the empty list.")
    else:
        print("1 is not in the empty list.")

    # Checking membership in a string
    string = "Hello, World!"
    if "Hello" in string:
        print("Substring 'Hello' is present in the string.")
    else:
        print("Substring 'Hello' is not present in the string.")

    # Checking membership in a tuple
    my_tuple = (1, 2, 3)
    if 4 not in my_tuple:
        print("4 is not present in the tuple.")
    else:
        print("4 is present in the tuple.")

check_membership()
