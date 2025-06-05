import random

def hangman():
    words = ["python", "programming", "computer", "algorithm", "developer", "artificial"]
    word = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Head, Body, Two Arms, Two Legs

    print("Welcome to Hangman!")
    print("_ " * len(word))

    while True:
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "
        print(display_word)

        if "_" not in display_word:
            print("Congratulations! You guessed the word:", word)
            break

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
        else:
            incorrect_guesses += 1
            print("Incorrect guess. You have", max_incorrect_guesses - incorrect_guesses, "guesses left.")
            draw_hangman(incorrect_guesses)
            if incorrect_guesses == max_incorrect_guesses:
                print("Game over! The word was:", word)
                break

def draw_hangman(incorrect_guesses):
    stages = [
        # 0 guesses
        """
           -----
           |   |
               |
               |
               |
               |
        ---------
        """,
        # 1 guess
        """
           -----
           |   |
           O   |
               |
               |
               |
        ---------
        """,
        # 2 guesses
        """
           -----
           |   |
           O   |
           |   |
               |
               |
        ---------
        """,
        # 3 guesses
        """
           -----
           |   |
           O   |
          /|   |
               |
               |
        ---------
        """,
        # 4 guesses
        """
           -----
           |   |
           O   |
          /|\  |
               |
               |
        ---------
        """,
        # 5 guesses
        """
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        ---------
        """,
        # 6 guesses
        """
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        ---------
        """
    ]
    print(stages[incorrect_guesses])

if __name__ == "__main__":
    hangman()