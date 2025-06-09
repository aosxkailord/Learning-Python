"""
Project: Fahrenheit to Celsius Converter
Author: Kashan Malik

This program helps convert temperatures from the Fahrenheit scale to the Celsius scale.
It focuses on:
1. Taking user input that might be a decimal number (floating-point).
2. Applying a specific mathematical formula for conversion.
3. Displaying the converted temperature clearly.

It's a useful example for handling real-world calculations in Python!
"""

def main() -> None:
    """
    The main function for our temperature conversion tool.
    It prompts for Fahrenheit, performs the calculation, and shows the Celsius equivalent.
    """
    print("Welcome to the Temperature Converter!")
    print("I'll convert a temperature from Fahrenheit to Celsius for you.")
    print("-" * 60) # A nice visual separator

    try:
        # Step 1: Prompt the user for the temperature in Fahrenheit.
        # It's important to note that temperature can often have decimal places,
        # so we'll be expecting a floating-point number.
        fahrenheit_input_str: str = input("Please enter the temperature in Fahrenheit: ")

        # Step 2: Convert the user's input from text to a floating-point number.
        # We use float() here instead of int() because temperatures can have decimals.
        # If the input isn't a valid number, a ValueError will be raised.
        fahrenheit_temp: float = float(fahrenheit_input_str)

        # Step 3: Apply the conversion formula.
        # This is the core calculation. The '.0' after 5 and 9 ensures that
        # Python performs floating-point division, giving us precise results.
        degrees_celsius: float = (fahrenheit_temp - 32) * 5.0 / 9.0

        # Step 4: Display the result.
        # We'll use an f-string to format the output exactly as requested,
        # showing both the original Fahrenheit temperature and the calculated Celsius one.
        # The original Fahrenheit is also displayed as a float (e.g., 76.0) for consistency.
        print(f"Temperature: {fahrenheit_temp}F = {degrees_celsius}C")
        print("\nConversion complete! Hope that was helpful.")

    except ValueError:
        # This block catches errors if the user inputs something that isn't a valid number.
        print("\nError: Invalid input! Please enter a numerical value for the temperature.")
        print("For example, try '76' or '98.6'.")
    except Exception as e:
        # A general catch-all for any other unexpected issues.
        print(f"\nAn unexpected problem occurred: {e}")
        print("Please try running the program again.")

# This is the standard entry point for Python scripts.
# It ensures our 'main()' function is called when the script is run directly.
if __name__ == '__main__':
    main()
