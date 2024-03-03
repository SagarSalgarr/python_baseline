def askint():
    while True:
        try:
            val = int(input("Please enter an integer: "))
        except:
            print("Looks like you did not enter an integer!")
            continue
        else:
            print("Yep that's an integer!")
            print(val)
            break
        
        finally:
            print("Finally, I executed!")


def test_comparison():
    try:
        # Floating Point Numbers
        result = 0.1 + 0.2 == 0.3
        print("Floating Point Test Result:", result)

        # NaN
        result = float('nan') == float('nan')
        print("NaN Test Result:", result)

        # Infinity
        result = float('inf') == float('inf')
        print("Infinity Test Result:", result)

        # Negative Zero
        result = -0.0 == 0.0
        print("Negative Zero Test Result:", result)

        result = 1 == '1'
        print("Equality of Different Types Test Result:", result)

        a = [1, 2, 3]
        b = a
        result1 = a == b  
        result2 = a is b  
        print("Comparing Objects Test Result (Equality):", result1)
        print("Comparing Objects Test Result (Identity):", result2)
    except Exception as e:
        print("An error occurred during comparison:", e)
    else:
        print("All comparison operations completed successfully.")
    finally:
        print("Comparison tests completed.")


def debug_comparison():
    try:
        result = 0.1 + 0.2
        print("Floating Point Debug Result:", result)
    except Exception as e:
        print("An error occurred during debugging:", e)
    finally:
        print("Debugging completed.")


askint()
test_comparison()
debug_comparison()

