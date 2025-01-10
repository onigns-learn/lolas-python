
# Asks the user to input their name and their favorite number.
# Stores the inputs in variables of appropriate types.
# Creates a list of greetings: ["Hello", "Hi", "Hey", "Greetings"].
# Selects a greeting based on the user's favorite number (use the remainder when dividing the number by the list length).
# Prints the selected greeting followed by the user's name, formatted like:
# 	Hey Alex! It's nice to meet you.



print("I am a Greeting Generator")

name = input("Enter your name: ")
fav_number = int(input("Enter your favourite number: "))

greetings = ["Hello", "Hi", "Hey", "Greetings"]

selected_greeting = greetings[fav_number % len(greetings)]

print(selected_greeting, name, "! It's nice to meet you")
