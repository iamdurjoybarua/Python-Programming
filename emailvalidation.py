import re

def is_valid_email(email):
    """
    Checks if a string is a valid email address using a basic regex.
    This regex is simple and covers most common cases.
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None

if __name__ == "__main__":
    email_address = input("Enter an email address: ")
    if is_valid_email(email_address):
        print("This is a valid email address. ✅")
    else:
        print("This is not a valid email address. ❌")