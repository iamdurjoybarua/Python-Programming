#  Palindrome Checker

This is a simple Python script that checks whether a user-provided word or phrase is a **palindrome**. A palindrome is a sequence that reads the same backward as forward, such as `"level"` or `"A man a plan a canal Panama"`.

---

##  Key Features

- **String Pre-processing**:  
  The program removes spaces and converts input to lowercase to ensure case-insensitive and space-insensitive checks. For example, both `"Racecar"` and `"race car"` are identified as palindromes.

- **Efficient Reversal**:  
  Uses Python slicing (`[::-1]`) to reverse the string concisely.

- **Clear Logic**:  
  The core check is done using a dedicated `is_palindrome` function, which returns a `True` or `False` value.

---

##  How to Run

1. Save the code as `palindrome_checker.py`.
2. Open your terminal or command prompt.
3. Run the script using the following command:

```bash
python palindrome_checker.py

Enter a word or phrase:

Enter a word or phrase: racecar
'racecar' is a palindrome.

Enter a word or phrase: hello world
'hello world' is not a palindrome.

Enter a word or phrase: A man a plan a canal Panama
'A man a plan a canal Panama' is a palindrome.
