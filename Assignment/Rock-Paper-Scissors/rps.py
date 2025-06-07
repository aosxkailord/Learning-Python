import random


def rock_paper_scissors():

    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    rounds = 0

    print("Welcome to Rock-Paper-Scissors !")
    print("Enter 'rock', 'paper', 'scissors', or 'quit' to end the game.")
    while True:
        player_choice = input("Your choice: ").lower() # Get player's choice

        if player_choice == "quit":
            break # Exit the game loop

        # Validate player's input
        if player_choice not in choices:
            print("Invalid choice. Please choose 'rock', 'paper', 'scissors'.")
            continue # Ask for input again

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        # Determine the winnerof the round
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice  == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

    rounds += 1
    print(f"Score - You: {player_score}, Computer: {computer_score} (Rounds: {rounds})\n")

    print ("\n --- Game Over ---")
    print(f"Final Score - You: {player_score}, Computer: {computer_score}")

    # Declare overall winner
    if player_score > computer_score:
        print("Congratulations! You won the game overall!!")
    elif player_score < computer_score: 
        print("Computer won the game overall. Better luck next time!")
    else: 
        print("The game ended in a tie overall!")


if __name__ == "__main__":
    rock_paper_scissors()