# factorial_calculator.py

# This program calculates the factorial of a non-negative integer using two different methods:
# an iterative approach and a recursive approach.

# --- Iterative approach ---
# This function uses a loop to calculate the factorial.
def factorial_iterative(n):
    # Factorial is not defined for negative numbers, so we handle this edge case.
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    # The factorial of 0 is 1. We also initialize the result to 1 for the loop.
    result = 1
    
    # We loop from 1 up to n (inclusive) and multiply the result by each number.
    for i in range(1, n + 1):
        result *= i
        
    return result

# --- Recursive approach ---
# This function calls itself to calculate the factorial.
def factorial_recursive(n):
    # Handle the edge case for negative numbers.
    if n < 0:
        return "Factorial is not defined for negative numbers."
    
    # Base case: The factorial of 0 is 1. This is the condition that stops the recursion.
    if n == 0:
        return 1
    # Recursive step: The factorial of n is n multiplied by the factorial of (n-1).
    else:
        return n * factorial_recursive(n - 1)

# --- Main part of the program ---
# Get user input for a non-negative integer.
# We use a try-except block to handle potential ValueError if the user enters non-integer input.
try:
    number = int(input("Enter a non-negative integer: "))

    # Print the result from both the iterative and recursive functions.
    print(f"Factorial of {number} (iterative): {factorial_iterative(number)}")
    print(f"Factorial of {number} (recursive): {factorial_recursive(number)}")

except ValueError:
    print("Invalid input. Please enter a valid non-negative integer.")