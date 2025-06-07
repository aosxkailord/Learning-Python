import time # ⏱️ We need the 'time' module for the 'sleep' function to pause our countdown.

def liftoff_countdown(start_number: int) -> None:
    """
    Counts down from a specified starting number to zero, then prints "Liftoff!".

    Args:
        start_number (int): The integer number to start the countdown from.
    """
    print(f"🚀 Preparing for liftoff! Countdown from {start_number}...")

    # 🔄 We use a 'for' loop to count down.
    # range(start_number, 0, -1) generates numbers from 'start_number' down to 1 (inclusive).
    # The third argument, -1, tells range to count backwards.
    for count in range(start_number, 0, -1):
        print(f"{count}...") # 🔢 Print the current countdown number.
        time.sleep(1)       # ⏳ Pause the program for 1 second. This makes it feel like a real countdown!

    print("BLAST OFF! 🚀🚀🚀") # 🎉 The final exciting message when the countdown reaches zero.

def liftoff_app() -> None:
    """
    The main application function for the Liftoff Countdown.
    It prompts the user for a starting number for the countdown, or uses a default.
    """
    print("Welcome to the Liftoff Countdown App! 🚀")
    print("I'll count down from a number you give me, then shout 'BLAST OFF!'")

    while True: # 🔄 Loop to ensure valid input for the countdown start number.
        user_input_str: str = input("Enter the starting number for countdown (e.g., 10), or 'default' for 5 seconds: ").strip()

        if user_input_str.lower() == 'default':
            start_count: int = 5 # 🎯 Use a default countdown of 5 seconds.
            print("Using default countdown of 5 seconds.")
            break # Exit loop, valid input received.
        
        try:
            start_count = int(user_input_str) # Attempt to convert input to an integer.
            if start_count <= 0: # 🚫 Ensure the number is positive.
                print("Please enter a positive whole number for the countdown. 🙏")
                continue # Ask again.
            break # Exit loop, valid input received.
        except ValueError: # ❌ If conversion fails, it's not a number.
            print("Invalid input! Please enter a whole number or 'default'.")
            continue # Ask again.
            
    liftoff_countdown(start_count) # 📞 Call our countdown function with the chosen number.

if __name__ == "__main__":
    # 🏁 This ensures our 'liftoff_app()' function runs only when the script is executed directly.
    liftoff_app()