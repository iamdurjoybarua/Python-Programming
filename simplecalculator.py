# calculator.py

# This program is a simple command-line calculator that performs basic arithmetic operations.

# --- Function Definitions ---
# The following functions define the four basic arithmetic operations.

# Defines a function to add two numbers.
def add(x, y):
    return x + y

# Defines a function to subtract two numbers.
def subtract(x, y):
    return x - y

# Defines a function to multiply two numbers.
def multiply(x, y):
    return x * y

# Defines a function to divide two numbers.
def divide(x, y):
    # Note: This function will raise a ZeroDivisionError if the user enters 0 for y.
    return x / y

# --- User Interface and Input ---
# These lines display the menu and get input from the user.
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Prompts the user to select an operation and stores their choice.
choice = input("Enter choice(1/2/3/4): ")

# Prompts the user for two numbers.
# float() is used to convert the input to a floating-point number,
# which allows for decimal values.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# --- Conditional Logic for Operations ---
# An if-elif-else block checks the user's choice and calls the appropriate function.

# If the user chose '1', call the add() function.
if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
# If the user chose '2', call the subtract() function.
elif choice == '2':
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
# If the user chose '3', call the multiply() function.
elif choice == '3':
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
# If the user chose '4', call the divide() function.
elif choice == '4':
    print(f"{num1} / {num2} = {divide(num1, num2)}")
# If the choice is not 1, 2, 3, or 4, print an error message.
else:
    print("Invalid Input")