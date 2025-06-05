# Guess the Number Game (Computer)

# --- 1. Import the 'random' module ---
# The 'random' module provides functions for generating random numbers.
# We need it so the computer can pick a secret number.
import random

# --- 2. Define the game function ---
# We're putting the entire game logic inside a function called 'guess_the_number'.
# Functions help organize your code and make it reusable.
def guess_the_number():
    """
    This function implements the 'Guess the Number' game where the computer
    chooses a number, and the user tries to guess it.
    It now includes a guess limit and allows the user to play multiple rounds.
    """
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")

    # Generate a random integer between 1 and 100 (inclusive)
    # The computer's secret number is stored in 'secret_number'.
    secret_number = random.randint(1, 100)

    # Initialize a variable to count how many guesses the user makes.
    guesses_taken = 0
    # Set a maximum number of guesses allowed.
    max_guesses = 7 # User gets 7 tries to guess the number

    # Initialize the user's guess to a value that won't match the secret number
    # immediately, so the while loop runs at least once.
    guess = 0

    # --- 3. Use a while loop for repeated guesses with a limit ---
    # The game continues as long as the user's guess is not equal to the secret number
    # AND they haven't run out of guesses.
    while guess != secret_number and guesses_taken < max_guesses:
        try:
            # Get user input for their guess
            # input() returns a string, so we convert it to an integer using int().
            guess = int(input(f"Take a guess (Guess {guesses_taken + 1} of {max_guesses}): "))
            guesses_taken += 1 # Increment the guess counter

            # --- 4. Use conditionals (if/elif/else) to check the guess ---
            if guess < secret_number:
                print("Your guess is too low!")
            elif guess > secret_number:
                print("Your guess is too high!")
            # If guess == secret_number, the loop condition will become false and exit.
            # The success message is handled after the loop.
        except ValueError:
            # This block handles cases where the user types something that's not a number.
            print("Invalid input. Please enter a whole number.")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

    # --- 5. Check game outcome after the loop ---
    if guess == secret_number:
        print(f"Good job! You guessed my number ({secret_number}) in {guesses_taken} guesses!")
    else:
        print(f"Sorry, you ran out of guesses! The number I was thinking of was {secret_number}.")
        print("Better luck next time!")

# --- 6. Allow the user to play again ---
# This loop will keep the game running until the user decides to quit.
play_again = True
while play_again:
    guess_the_number() # Call the game function to start a round

    # Ask the user if they want to play again
    while True: # Loop to ensure valid input for playing again
        choice = input("Do you want to play again? (yes/no): ").lower().strip()
        if choice == 'yes':
            play_again = True
            break # Exit the inner loop and start a new game
        elif choice == 'no':
            play_again = False
            break # Exit the inner loop and then the outer loop will terminate
        else:
            print("Invalid input. Please type 'yes' or 'no'.")

print("\nThanks for playing!")
