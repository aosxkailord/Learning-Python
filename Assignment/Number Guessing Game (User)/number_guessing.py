import random

def play_guess_the_number_game():
    """
    Lets you play a fun game where you try to guess a secret number!
    The computer will think of a number, and you'll try to figure it out.
    """

    # --- Game Setup ---
    print("---------------------------------------")
    print("🎉 Welcome to the 'Guess the Number' Adventure! 🎉")
    print("---------------------------------------")
    print("I'm thinking of a secret number between 1 and 100.")

    # The computer secretly picks a number. Shhh, it's a secret!
    secret_number_chosen_by_computer = random.randint(1, 100)
    
    # We'll keep track of how many guesses you've made.
    number_of_guesses_taken = 0
    # Let's give you a fair chance, say, 10 attempts.
    maximum_attempts_allowed = 10

    print(f"You have {maximum_attempts_allowed} chances to find it. Good luck!\n")

    # --- The Guessing Loop ---
    # This loop will keep going as long as you have attempts left.
    while number_of_guesses_taken < maximum_attempts_allowed:
        
        # Let's get your guess.
        print("---------------------------------------")
        user_guess_str = input(f"Attempt {number_of_guesses_taken + 1} of {maximum_attempts_allowed}. What's your guess? ")

        # We need to make sure you entered a whole number.
        try:
            user_guess_int = int(user_guess_str)
        except ValueError:
            print("Oops! 🤔 That doesn't look like a whole number. Please try again with a number (e.g., 7, 42).")
            # This 'continue' skips the rest of the loop for this turn and asks for input again.
            continue 
        
        # Okay, you've officially made a guess!
        number_of_guesses_taken += 1

        # --- Check the Guess ---
        if user_guess_int < secret_number_chosen_by_computer:
            print(f"A little bird told me... your guess of {user_guess_int} is a bit too low! 🐦 Try a higher number.")
        elif user_guess_int > secret_number_chosen_by_computer:
            print(f"Whoa there! Your guess of {user_guess_int} is a bit too high! 🎈 Try a lower number.")
        else:
            # You got it!
            print("\n---------------------------------------")
            print(f"🥳🎉 WOOHOO! You did it! 🎉🥳")
            print(f"You guessed the secret number {secret_number_chosen_by_computer} in just {number_of_guesses_taken} attempts!")
            print("You're a number-guessing wizard! ✨")
            print("---------------------------------------\n")
            return # Exit the function, the game is won!

        # --- After each guess (if not correct) ---
        attempts_left = maximum_attempts_allowed - number_of_guesses_taken
        if attempts_left > 0:
            print(f"You still have {attempts_left} attempts remaining. Keep going!\n")
        
    # --- If all attempts are used up ---
    # This part only runs if the 'while' loop finishes without a correct guess.
    print("\n---------------------------------------")
    print("Game Over! 😔")
    print(f"You've used all {maximum_attempts_allowed} attempts.")
    print(f"The secret number I was thinking of was: {secret_number_chosen_by_computer}")
    print("Better luck next time! 👍")
    print("---------------------------------------\n")

# This is a common Python practice. The code inside this 'if' block
# runs only when you execute this file directly (not when you import it somewhere else).
if __name__ == "__main__":
    play_guess_the_number_game()