import random

print("Welcome to the game, this is a number guessing game! \n You got 5 attempts to guess the number between 1 and 30, let's start the game!")

number_to_guess = random.randrange(1,30)

chances = 5

guess_counter= 0

while guess_counter < chances :
    guess_counter += 1
    my_guess = int(input("Please enter your guess: "))

    if my_guess == number_to_guess:
        print(f"The number is {number_to_guess} and you found it right!! in the {guess_counter} attempt")
        break
    elif guess_counter >= chances and my_guess != number_to_guess :
        print(f"Sorry, you didn't find the number {number_to_guess}. Better luck next time!")
    
    elif my_guess < number_to_guess:
        print("Too low! Try again.")

    elif my_guess > number_to_guess:
        print("Too high! Try again.")
