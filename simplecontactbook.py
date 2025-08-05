# simplecontactbook.py

# This program is a simple command-line contact book application.
# It allows a user to add, view, and search for contacts.
# The program uses a dictionary to store contact names and phone numbers.

# Initialize an empty dictionary to store contacts.
# The key will be the contact's name (a string), and the value will be the phone number (a string).
contacts = {}

# --- Function Definitions ---
# The following functions handle the core functionalities of the contact book.

# Defines a function to add a new contact.
def add_contact():
    # Prompts the user for the contact's name and phone number.
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    
    # Adds a new key-value pair to the 'contacts' dictionary.
    contacts[name] = phone
    
    # Prints a confirmation message.
    print(f"Contact '{name}' added.")

# Defines a function to display all contacts.
def view_contacts():
    # Checks if the dictionary is empty.
    if not contacts:
        print("No contacts found.")
        # The 'return' statement exits the function early if there are no contacts.
        return
    
    print("--- Your Contacts ---")
    # Iterates through each key-value pair in the 'contacts' dictionary.
    # The .items() method returns a view object that displays a list of a given dictionary's key-value tuple pairs.
    for name, phone in contacts.items():
        print(f"Name: {name}, Phone: {phone}")

# Defines a function to search for a specific contact.
def search_contact():
    # Prompts the user for the name of the contact to search for.
    name = input("Enter the name to search: ")
    
    # Checks if the entered name exists as a key in the 'contacts' dictionary.
    if name in contacts:
        # If the name is found, prints the name and its corresponding phone number.
        print(f"Name: {name}, Phone: {contacts[name]}")
    else:
        # If the name is not found, prints a message indicating that.
        print(f"Contact '{name}' not found.")

# --- Main Program Loop ---
# This 'while True' loop keeps the program running until the user decides to exit.
while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Exit")
    
    # Get the user's menu choice.
    choice = input("Enter your choice: ")
    
    # An if-elif-else block to handle the user's choice.
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        print("Exiting...")
        # The 'break' statement terminates the 'while' loop, ending the program.
        break
    else:
        # Handles any invalid input from the user.

        print("Invalid choice. Please try again.")
