# numberguessinggame.py

# This program is a classic number guessing game. The computer picks a random number,
# and the user tries to guess it.

import random # Imports the 'random' module to generate a random number.

# Generate a random integer between 1 and 100 (inclusive).
# This is the secret number the user needs to guess.
secret_number = random.randint(1, 100) 

guess = None # Initializes the 'guess' variable. It's set to None to start the while loop.
attempts = 0 # Initializes a counter for the number of attempts.

print("I'm thinking of a number between 1 and 100.") # A friendly message to the user.

# The main game loop continues as long as the user's guess is not equal to the secret number.
while guess != secret_number:
    try:
        # Get the user's guess and convert it to an integer.
        # This line might raise a ValueError if the user enters non-numeric text.
        guess = int(input("Enter your guess: "))
        
        attempts += 1 # Increment the attempt counter for each valid guess.

        # Check if the guess is too low, too high, or correct.
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            # This block runs when the user guesses correctly.
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
    
    except ValueError:
        # This block catches the ValueError if the user enters something that can't be
        # converted to an integer, preventing the program from crashing.

        print("Invalid input. Please enter a number.")
