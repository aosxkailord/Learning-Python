"""
Project: Favorite Animal Responder
Author: Kashan Malik

This little program demonstrates a very common task:
1. Asking the user a question.
2. Taking their answer as input.
3. Using that answer to craft a personalized response back to them.

It's a great example of how simple input/output works in Python!
"""

def main() -> None:
    """
    This is the heart of our program. It manages the interaction:
    asking for the animal, getting the response, and then replying.
    """
    print("Hello there!")
    print("I'm curious about animals, and I'd love to know your favorite.")
    print("-" * 50) # A neat little separator

    try:
        # Step 1: Ask the user a question to get their favorite animal.
        # The input() function will display the prompt and then wait for the user to type something
        # and press Enter. Whatever they type will be stored as a string.
        user_favorite_animal: str = input("What's your favorite animal? ")

        # Step 2: Now, we'll respond!
        # We'll use an f-string (formatted string literal) here because it's
        # a wonderfully clear and modern way to embed variables directly into strings.
        # This makes our output message dynamic and includes the user's actual input.
        print(f"My favorite animal is also {user_favorite_animal}!")
        print("\nThanks for sharing!")

    except Exception as e:
        # Just a general catch-all for any unexpected issues.
        # For simple input(), this might not happen often, but it's good practice!
        print(f"\nAn unexpected problem occurred: {e}")
        print("Please try running the program again.")

# This is the standard entry point for Python scripts.
# It ensures that our 'main()' function runs when we execute this file directly.
if __name__ == '__main__':
    main()
