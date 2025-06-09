"""
Project: Triangle Perimeter Calculator
Author: Kashan Malik

This program calculates the perimeter of a triangle. It demonstrates:
1. Taking multiple numerical inputs from the user, including decimals.
2. Converting these inputs into floating-point numbers.
3. Performing a simple sum to find the perimeter.
4. Displaying the result clearly.

It's a practical example for geometry calculations in Python!
"""

def main() -> None:
    """
    The main function for our triangle perimeter calculator.
    It prompts for each side length, sums them up, and prints the total perimeter.
    """
    print("Welcome to the Triangle Perimeter Calculator!")
    print("I'll help you find the total length around your triangle.")
    print("-" * 60) # A visual separator for a clean console experience

    try:
        # Step 1: Get the length of the first side from the user.
        # We expect a number, possibly with decimals, so we'll use float().
        side1_str: str = input("What is the length of side 1? ")
        side1: float = float(side1_str)

        # Step 2: Get the length of the second side.
        side2_str: str = input("What is the length of side 2? ")
        side2: float = float(side2_str)

        # Step 3: Get the length of the third and final side.
        side3_str: str = input("What is the length of side 3? ")
        side3: float = float(side3_str)

        # Optional (but good practice): You might add a check here
        # to ensure side lengths are positive. For this problem, we'll assume valid input.
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            print("\nError: Side lengths must be positive numbers. Please try again.")
            return # Exit the function if input is invalid.

        # Step 4: Calculate the perimeter.
        # The perimeter is simply the sum of all three sides.
        triangle_perimeter: float = side1 + side2 + side3

        # Step 5: Display the calculated perimeter to the user.
        # An f-string makes this output clear and easy to read.
        print(f"\nThe perimeter of the triangle is {triangle_perimeter}")
        print("\nCalculation complete! Hope that helps with your geometry!")

    except ValueError:
        # This error occurs if the user types something that isn't a valid number
        # when asked for a side length.
        print("\nOops! Invalid input detected.")
        print("Please make sure you enter valid numbers (e.g., 3, 4.5, 7) for side lengths.")
    except Exception as e:
        # A general error catch for any other unexpected issues.
        print(f"\nAn unexpected error occurred: {e}")
        print("Please try running the program again.")

# This standard block ensures that 'main()' runs only when this Python script
# is executed directly, not when imported as a module.
if __name__ == '__main__':
    main()
