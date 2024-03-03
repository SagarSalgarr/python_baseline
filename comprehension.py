def main():
    try:
        squared_numbers = [x ** 2 for x in range(1, 6)]

        square_dict = {x: x ** 2 for x in range(1, 6)}

        even_squares_set = {x ** 2 for x in range(1, 11) if x % 2 == 0}

        square_generator = (x ** 2 for x in range(1, 6))

        print("List Comprehension (Squared Numbers):", squared_numbers)
        print("Dictionary Comprehension (Square Dictionary):", square_dict)
        print("Set Comprehension (Even Squares Set):", even_squares_set)
        print("Generator Comprehension (Square Generator):", list(square_generator))

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except ZeroDivisionError as zde:
        print(f"ZeroDivisionError: {zde}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
