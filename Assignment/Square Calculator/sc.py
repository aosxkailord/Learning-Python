"""
Project: Square Calculator
Author: Kashan Malik

This program takes a number from the user and calculates its square.
It focuses on:
1. Getting a numerical input from the user (which can be a decimal).
2. Performing the exponentiation operation (number * number).
3. Displaying the original number and its square clearly.
4. Implementing error handling for invalid input.

It's a foundational example for basic arithmetic and input validation in Python!
"""

def main() -> None:
    """
    The main function for our square calculation tool.
    It prompts the user for a number, computes its square, and prints the result.
    """
    print("Welcome to the Square Calculator!")
    print("I can tell you the square of any number you give me.")
    print("-" * 55) # A visual separator for a neat console experience

    try:
        # Step 1: Prompt the user to enter a number.
        # We'll treat this as a string initially, as input() always returns text.
        # It's important to allow for decimal numbers, so we'll prepare for floats.
        user_input_str: str = input("Type a number to see its square: ")

        # Step 2: Convert the user's input from text to a floating-point number.
        # Using float() ensures we can handle both whole numbers and decimals.
        # If the user types non-numeric characters, float() will raise a ValueError.
        number_to_square: float = float(user_input_str)

        # Step 3: Calculate the square of the number.
        # Python's '**' operator is perfect for exponentiation (raising to a power).
        # 'number_to_square ** 2' means 'number_to_square multiplied by itself'.
        calculated_square: float = number_to_square ** 2

        # Step 4: Display the result to the user.
        # We'll use an f-string for clear and concise output, embedding
        # both the original number and its calculated square directly.
        print(f"{number_to_square} squared is {calculated_square}")
        print("\nCalculation complete! Hope you found that useful.")

    except ValueError:
        # This specific 'except' block catches the ValueError that occurs
        # if float() can't convert the user's input (e.g., they typed "hello").
        print("\nOops! That doesn't look like a valid number.")
        print("Please enter a numeric value (like 5, 12.3, or -7) next time.")
    except Exception as e:
        # A more general catch-all for any other unforeseen issues, just for robustness.
        print(f"\nAn unexpected problem occurred: {e}")
        print("Please try running the program again.")

# This standard Python construct ensures that our 'main()' function
# is called and the program starts only when this script file is executed directly.
if __name__ == '__main__':
    main()
