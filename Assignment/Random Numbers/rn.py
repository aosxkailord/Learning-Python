import random # 🎲 This module is our toolkit for all things random!
from typing import List, Any # ✨ Type hints for lists of any type.

def generate_random_integer(min_val: int, max_val: int) -> int:
    """
    Generates a random integer within a specified inclusive range.

    Args:
        min_val (int): The minimum (inclusive) value for the random integer.
        max_val (int): The maximum (inclusive) value for the random integer.

    Returns:
        int: A random integer between min_val and max_val (inclusive).
    """
    # 🔢 random.randint(a, b) returns a random integer N such that a <= N <= b.
    return random.randint(min_val, max_val)

def generate_random_float_0_to_1() -> float:
    """
    Generates a random floating-point number between 0.0 (inclusive) and 1.0 (exclusive).

    Returns:
        float: A random float in the range [0.0, 1.0).
    """
    # 📈 random.random() returns a random float in the range [0.0, 1.0).
    return random.random()

def generate_random_float_range(min_val: float, max_val: float) -> float:
    """
    Generates a random floating-point number within a specified inclusive range.

    Args:
        min_val (float): The minimum (inclusive) value for the random float.
        max_val (float): The maximum (inclusive) value for the random float.

    Returns:
        float: A random float between min_val and max_val (inclusive).
    """
    # 📊 random.uniform(a, b) returns a random float N such that a <= N <= b.
    return random.uniform(min_val, max_val)

def pick_random_choice(items: List[Any]) -> Any:
    """
    Picks a random element from a non-empty list.

    Args:
        items (List[Any]): The list from which to pick a random item.

    Returns:
        Any: A randomly selected item from the list.
    """
    if not items: # ⚠️ Always good to check if the list is empty before picking!
        raise ValueError("Cannot pick from an empty list.")
    # 🎯 random.choice(sequence) returns a randomly selected element from a non-empty sequence.
    return random.choice(items)

def shuffle_list_in_place(data_list: List[Any]) -> None:
    """
    Shuffles the elements of a list randomly in place (modifies the original list).

    Args:
        data_list (List[Any]): The list to be shuffled.
    """
    print(f"List before shuffling: {data_list} ➡️")
    # 🔀 random.shuffle(x) shuffles the sequence x in place.
    # It modifies the original list directly and doesn't return a new one.
    random.shuffle(data_list)
    print(f"List after shuffling: {data_list} ✨")

def random_numbers_app() -> None:
    """
    The main application function demonstrating various random number generations.
    """
    print("Welcome to the Random Numbers Generator! 🎲")
    print("Let's explore the magic of randomness in Python. 🔮\n")

    # --- Random Integer ---
    print("--- Random Integer Generation ---")
    min_int: int = 1
    max_int: int = 100
    random_int: int = generate_random_integer(min_int, max_int)
    print(f"Random integer between {min_int} and {max_int}: {random_int} 🔢")

    dice_roll: int = generate_random_integer(1, 6)
    print(f"Rolling a dice: {dice_roll} 🎲\n")

    # --- Random Float (0.0 to 1.0) ---
    print("--- Random Float (0.0 to 1.0) Generation ---")
    random_float_0_1: float = generate_random_float_0_to_1()
    print(f"Random float between 0.0 and 1.0: {random_float_0_1:.4f} 📈 (showing 4 decimal places)\n")

    # --- Random Float (Custom Range) ---
    print("--- Random Float (Custom Range) Generation ---")
    min_float: float = 10.0
    max_float: float = 20.0
    random_float_custom: float = generate_random_float_range(min_float, max_float)
    print(f"Random float between {min_float} and {max_float}: {random_float_custom:.2f} 📊\n")

    # --- Random Choice from a List ---
    print("--- Random Choice from a List ---")
    colors: List[str] = ["Red ❤️", "Green 💚", "Blue 💙", "Yellow 💛", "Purple 💜"]
    chosen_color: str = pick_random_choice(colors)
    print(f"Our lucky color for today is: {chosen_color} 🎉")

    fruits: List[str] = ["Apple 🍎", "Banana 🍌", "Cherry 🍒"]
    chosen_fruit: str = pick_random_choice(fruits)
    print(f"Let's grab a random fruit: {chosen_fruit} 😋\n")
    
    # Example of handling an empty list for random.choice
    # try:
    #     pick_random_choice([])
    # except ValueError as e:
    #     print(f"Error: {e} 🚫")


    # --- Shuffle a List ---
    print("--- Shuffling a List ---")
    my_list: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffle_list_in_place(my_list) # This function modifies my_list directly
    print("Shuffling done! 👍\n")
    
    # Another shuffle example
    card_deck: List[str] = ["Ace♠️", "King♥️", "Queen♦️", "Jack♣️", "Ten♠️"]
    shuffle_list_in_place(card_deck)
    print("Deck shuffled! Ready for a game? 🃏")

if __name__ == "__main__":
    # 🏁 This ensures our 'random_numbers_app()' function runs only when the script is executed directly.
    random_numbers_app()