# Mad Libs Python Project

# --- 1. Get Input from the User ---
# We'll use the input() function to ask the user for different types of words.
# The text inside the paranthesis is the prompt shown to the user.
# Whatever the user types will be stored in the variable on the left side of the '='.

print("Let's play Mad Libs! Please provide the following words:")

# Nouns are people, places, or things.
noun1 = input("Enter a noun (person/place/thing): ")
noun2 = input("Enter another noun: ")

# Verbs are action words.
verb1 = input("Eneter a verb (acrtion word): ")
verb2 = input("Enter another verb: ")

# Adjective describes noun (e.g., happy, big, red).
adjective1 = input("Enter an adjective (describing word): ")
adjective2 = input("Enter another adjective: ")

# An exclamation is a sudden cry or remark (e.g., Wow!, Ouch!).
exclamation = input("Enter an exclamation (e.g., Wow!, Ouch!): ")

# --- 2. Create the Story with f-strings ---
# An f-string (formatted string literal) allows you to embed expressions
# insdide string literals by prefixing the string with 'f' or 'F'
# and eriting expressions as '{expressions}'.

# We'll build our Mad Libs story using the words the user provided.
# Notice how the variables (noun1, verb1, etc.) are placed directly inside curly braces {}.
madlib = f"{exclamation}! I can't believe it! Today, I went to the {noun1} and saw a giant {adjective1} {noun2}. " \
         f"It started to {verb1} really fast, so I decided to {verb2} away. " \
         f"It was the most {adjective2} experience of my life!"

# --- 3. Print Results to the Console ---
# Finally, we print the completed Mad Libs story for the user to see.
print("\n--- Your Completed Mad Libs Story ---")
print(madlib)

print("\nThanks for playing!")
