import random
import string

def generate_password(length):
    # Combine all possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters for the password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Generate a password with a length of 12
password = generate_password(12)
print(f"Generated password: {password}")