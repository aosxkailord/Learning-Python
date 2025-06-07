from typing import Union # ✨ We import Union for type hinting when a variable can be one of several types.

def double_value(num: Union[int, float]) -> Union[int, float]:
    """
    Doubles a given numeric value (integer or float).

    Args:
        num (Union[int, float]): The number to be doubled. Can be an integer or a float.

    Returns:
        Union[int, float]: The doubled value. The type matches the input type (int if int, float if float).
    """
    # ✖️ We simply multiply the input number by 2 to double it.
    doubled_num: Union[int, float] = num * 2
    return doubled_num

def double_it_app() -> None:
    """
    The main application function for the 'Double It!' program.
    It prompts the user for a number, attempts to double it, and prints the result.
    Includes error handling for invalid input.
    """
    print("✨ Welcome to the 'Double It!' app! ✨")
    print("I can double any whole number or decimal number you give me. 🔢")

    while True: # 🔄 We use a loop to allow the user to try again if input is invalid.
        user_input_str: str = input("\nPlease enter a number to double (or type 'quit' to exit): ").strip() # 🗣️ Get input from the user and remove any leading/trailing spaces.

        if user_input_str.lower() == 'quit': # 🛑 Check if the user wants to exit.
            print("Exiting 'Double It!' app. Goodbye! 👋")
            break # Exit the loop and end the program.

        try:
            # Try to convert the input string to an integer first.
            # If it's a whole number, we prefer to keep it as an integer.
            number_to_double: Union[int, float] = int(user_input_str) # Attempt to convert to int
            print(f"Recognized input as an integer. 🤓")

        except ValueError:
            # If it fails to convert to an integer, try converting to a float (for decimals).
            try:
                number_to_double = float(user_input_str) # Attempt to convert to float
                print(f"Recognized input as a decimal number. 🧐")
            except ValueError:
                # If it's neither an int nor a float, it's invalid input.
                print("🚫 Invalid input! Please enter a valid number (e.g., 5, 10.5) or 'quit'.")
                continue # Skip the rest of this loop iteration and ask for input again.
        
        # 🎉 If we successfully got a number, let's double it!
        result: Union[int, float] = double_value(number_to_double)
        print(f"Your number: {number_to_double}")
        print(f"Doubled: {result} 🤩") # 🚀 Print the exciting doubled result!
        
        # No break here, so the user can continue doubling numbers until they 'quit'.

if __name__ == "__main__":
    # 🏁 This ensures our 'double_it_app()' function runs only when the script is executed directly.
    double_it_app()