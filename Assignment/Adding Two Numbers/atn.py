"""
Project: Add Two Numbers
Author: Kashan Malik

This program is a simple yet foundational exercise designed to help understand:
1. How to get input directly from the user.
2. How to convert that input from text into numbers.
3. Performing basic arithmetic (addition) on those numbers.
4. Displaying a clear, user-friendly result.

It's a great starting point for interactive Python programs!
"""

def main() -> None:
    """
    This is the main function where our program execution begins.
    It orchestrates the steps: getting numbers, calculating, and showing the sum.
    """
    print("Welcome to the Number Adder!")
    print("I'll ask you for two whole numbers, and then I'll tell you their sum.")
    print("-" * 40) # Just a little separator for neatness

    try:
        # Step 1: Get the first number from the user.
        # We prompt them and store whatever they type as a string first.
        first_number_as_text: str = input("Please enter your first whole number: ")

        # Step 2: Convert the first number from text to an actual integer.
        # This is super important because input() always gives us text (string),
        # but we need a number to do math! If they type something that isn't a number,
        # int() will raise an error, which our 'try-except' block will catch.
        first_number: int = int(first_number_as_text)

        # Step 3: Now, let's get the second number, following the same process.
        second_number_as_text: str = input("And now, enter your second whole number: ")

        # Step 4: Convert the second number to an integer.
        second_number: int = int(second_number_as_text)

        # Step 5: Time for the magic! We add the two numbers together.
        # Python's '+' operator works just like you'd expect for numbers.
        calculated_sum: int = first_number + second_number

        # Step 6: Finally, we display the result in a friendly way.
        # Using an f-string here makes it super easy to embed our 'calculated_sum'
        # directly into the message.
        print(f"\nAwesome! The sum of {first_number} and {second_number} is: {calculated_sum}")
        print("Thanks for using the Number Adder!")

    except ValueError:
        # This block runs if the user types something that cannot be converted to a whole number.
        print("\nOops! That wasn't a valid whole number.")
        print("Please make sure you enter only digits (like 10, 25, 100) next time.")
    except Exception as e:
        # A general catch-all for any other unexpected errors, just in case.
        print(f"\nAn unexpected problem occurred: {e}")
        print("Please try running the program again.")

# This is the standard Python entry point.
# It ensures that our 'main()' function is called only when this script
# is executed directly (not when it's imported as a module into another script).
if __name__ == '__main__':
    main()
