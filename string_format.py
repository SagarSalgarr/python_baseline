if __name__ == "__main__":
    # Using placeholders
    price = 49
    txt = "The price is {} dollars"
    print(txt.format(price))

    # Formatting the price with two decimals
    txt = "The price is {:.2f} dollars"
    print(txt.format(price))

    #  Using multiple values
    quantity = 3
    itemno = 567
    price = 49
    myorder = "I want {} pieces of item number {} for {:.2f} dollars."
    print(myorder.format(quantity, itemno, price))

    #  Using index numbers
    myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
    print(myorder.format(quantity, itemno, price))

    #  Referring to the same value more than once using index numbers
    age = 36
    name = "John"
    txt = "His name is {1}. {1} is {0} years old."
    print(txt.format(age, name))

    # Using named indexes
    myorder = "I have a {carname}, it is a {model}."
    print(myorder.format(carname="Ford", model="Mustang"))
