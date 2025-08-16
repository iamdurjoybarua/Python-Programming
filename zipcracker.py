# WARNING: This program is for educational purposes only.
# Do not use it on files you do not have explicit permission to access.

import zipfile

def crack_zip(zip_file_path, wordlist_path):
    """Attempts to crack a password-protected ZIP file."""
    try:
        zip_file = zipfile.ZipFile(zip_file_path)
    except FileNotFoundError:
        print(f"Error: ZIP file not found at {zip_file_path}")
        return

    try:
        with open(wordlist_path, 'r') as wordlist:
            for line in wordlist:
                password = line.strip()
                try:
                    zip_file.extractall(pwd=password.encode())
                    print(f"Password found! -> {password}")
                    return
                except (RuntimeError, zipfile.BadZipFile):
                    # Continue trying the next password
                    continue
    except FileNotFoundError:
        print(f"Error: Wordlist file not found at {wordlist_path}")
        return

    print("Password not found in the wordlist.")

if __name__ == "__main__":
    zip_path = input("Enter the path to the ZIP file: ")
    wordlist_path = input("Enter the path to the wordlist file: ")
    crack_zip(zip_path, wordlist_path)