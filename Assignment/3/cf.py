# If/Else Statements
age = 25
if age >= 18:
    print("You're an adult")

elif age >= 13:
    print("You're a teenager")

else:
    print("You're a child")


# For Loops
fruits = ["apple", "banana", "cherry"]
for fruits in fruits:
    print(f"Fruits: {fruits}")


# While Loops
i = 0
while i < 5:
    print(f"Loop iteration: {i}")
    i += 1


# Nested Control Flow
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
