def count_vowels(text):
    """Counts the number of vowels in a given string."""
    vowels = "aeiou"
    count = 0
    for char in text.lower():  # Convert to lowercase for case-insensitivity
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    user_string = input("Enter a word or phrase: ")
    vowel_count = count_vowels(user_string)
    print(f"The number of vowels is: {vowel_count}")