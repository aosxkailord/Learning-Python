"""
Project: Age Riddle Solver
Author: Kashan Malik

This program solves a specific age riddle for a group of friends: Anton, Beth, Chen,
Drew, and Ethan. It demonstrates how to:
1. Store initial given information in variables.
2. Calculate subsequent values based on relationships to existing variables.
3. Print out all the final calculated values in a clear, formatted way.

It's a practical way to see variables and basic arithmetic in action!
"""

def main() -> None:
    """
    The main function where we solve the age riddle.
    We'll define each friend's age step-by-step and then display them.
    """
    print("Welcome to the Age Riddle Solver!")
    print("Let's figure out the ages of Anton, Beth, Chen, Drew, and Ethan.")
    print("-" * 60) # Just a little visual separation

    # Step 1: Start with the age that is directly given.
    # Anton's age is our anchor point for the riddle.
    anton_age: int = 21

    # Step 2: Calculate Beth's age.
    # Beth is 6 years older than Anton, so we simply add 6 to Anton's age.
    beth_age: int = anton_age + 6

    # Step 3: Calculate Chen's age.
    # Chen is 20 years older than Beth. We build upon Beth's calculated age.
    chen_age: int = beth_age + 20

    # Step 4: Calculate Drew's age.
    # Drew's age is the sum of Chen's age and Anton's age. This involves two
    # previously calculated ages.
    drew_age: int = chen_age + anton_age

    # Step 5: Calculate Ethan's age.
    # Ethan is the same age as Chen, which is a direct assignment.
    ethan_age: int = chen_age

    # Step 6: Print out all the ages.
    # It's important to match the requested output format exactly,
    # including capitalization and punctuation. Using f-strings here
    # makes formatting very clean and readable.
    print(f"Anton is {anton_age}")
    print(f"Beth is {beth_age}")
    print(f"Chen is {chen_age}")
    print(f"Drew is {drew_age}")
    print(f"Ethan is {ethan_age}")

    print("\nRiddle solved! All ages calculated and displayed.")

# This is the standard entry point for Python scripts.
# It ensures that our 'main()' function is called when this script
# is executed directly from the terminal.
if __name__ == '__main__':
    main()
