import random # 🎲 We need this module to pick jokes randomly!
from typing import List, Dict # ✨ Adding type hints for cleaner, more "modern" Python code.

def deliver_joke() -> None:
    """
    Selects a random joke from a predefined list and delivers it to the user.
    It prints the joke's setup and then waits for the user to reveal the punchline.
    """
    # 📚 Our collection of hilarious jokes! Each joke is a dictionary with a 'setup' and 'punchline'.
    jokes: List[Dict[str, str]] = [
        {"setup": "Why don't scientists trust atoms?", "punchline": "Because they make up everything! ⚛️"},
        {"setup": "Why did the scarecrow win an award?", "punchline": "Because he was outstanding in his field! 🌾"},
        {"setup": "What do you call a fake noodle?", "punchline": "An impasta! 🍝"},
        {"setup": "Why don't skeletons fight each other?", "punchline": "They don't have the guts! 💀"},
        {"setup": "Did you hear about the restaurant on the moon?", "punchline": "Great food, no atmosphere! 🌕"},
        {"setup": "How do you organize a space party?", "punchline": "You planet! 🪐"},
        {"setup": "What do you call a lazy kangaroo?", "punchline": "Pouch potato! 🥔"},
    ]

    # 🎰 Let's pick one joke randomly from our list!
    chosen_joke: Dict[str, str] = random.choice(jokes)

    # 🗣️ First, we deliver the setup of the joke.
    print(f"\nJoke time! 🎉")
    print(chosen_joke["setup"])

    # ⏳ We pause and wait for the user to press Enter to reveal the punchline.
    input("Press Enter for the punchline... ")

    # 🥁 And here comes the punchline!
    print(chosen_joke["punchline"])
    print("😂 Hope you liked that one!")

def joke_bot() -> None:
    """
    The main function for our Joke Bot application.
    It continuously asks the user if they want a joke and delivers one until they say no.
    """
    print("Welcome to your personal Joke Bot! 🤖 Get ready to laugh! 😄")

    while True: # 🔄 This loop keeps our bot running until the user decides to stop.
        # ❓ Ask the user if they'd like to hear a joke. We convert their input to lowercase.
        user_response: str = input("\nDo you want to hear a joke? (yes/no): ").lower()

        # ✅ Check if the user said 'yes'.
        if user_response == 'yes':
            deliver_joke() # 🚀 If yes, let's deliver a joke!
        # ❌ Check if the user said 'no'.
        elif user_response == 'no':
            print("Okay, no more jokes for now! Thanks for hanging out. 👋")
            break # 🛑 If no, we break out of the loop, ending the program.
        # 🤔 Handle any other unexpected input.
        else:
            print("Sorry, I didn't understand that. Please type 'yes' or 'no'. 🙏")

if __name__ == "__main__":
    # 🏁 This ensures our 'joke_bot()' function runs only when the script is executed directly.
    joke_bot()