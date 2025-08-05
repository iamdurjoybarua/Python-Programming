# palindromechecker.py

# This program checks if a user-provided word or phrase is a palindrome.
# A palindrome is a sequence that reads the same backward as forward.

# Define a function named 'is_palindrome' that takes one argument, 's' (for string).
def is_palindrome(s):
    # Step 1: Pre-process the string for an accurate check.
    # The .replace(" ", "") method removes all spaces.
    # The .lower() method converts the string to lowercase.
    # This ensures that "Racecar" and "race car" are both correctly identified as palindromes.
    processed_string = s.replace(" ", "").lower()
    
    # Step 2: Compare the processed string with its reverse.
    # [::-1] is a Python slice that creates a reversed copy of the string.
    # The function returns True if the string is the same as its reverse, otherwise False.
    return processed_string == processed_string[::-1]

# Prompt the user to enter a word or phrase and store it in the 'user_input' variable.
user_input = input("Enter a word or phrase: ")

# Call the 'is_palindrome' function with the user's input.
# The 'if' statement executes the code block based on the function's return value (True or False).
if is_palindrome(user_input):
    # If the function returns True, print a message confirming it's a palindrome.
    print(f"'{user_input}' is a palindrome.")
else:
    # If the function returns False, print a message stating it's not a palindrome.

    print(f"'{user_input}' is not a palindrome.")
