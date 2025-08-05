# Number Guessing Game

This program is a classic number guessing game. The computer chooses a random number, and the user must guess it. The game provides hints after each guess, telling the user if their guess was too high or too low.

---

##  Key Features:

- **Random Number Generation**: Uses Python's built-in `random` module to select a secret number, ensuring a new game every time.

- **Game Loop**: The core of the game is a `while` loop that continues until the user's guess matches the secret number.

- **Conditional Hints**: Employs `if/elif/else` statements to guide the user with hints like "Too high!" or "Too low!".

- **Error Handling**: A `try-except` block is used to catch invalid, non-numeric input from the user, preventing the program from crashing.

- **Attempt Counter**: Tracks and displays the number of attempts it took to guess the number, adding a fun element of challenge.

---

##  How to Run:

1. Save the code as `numberguessinggame.py`.

2. Open your terminal or command prompt.

3. Run the script with the following command:

   ```bash
   python numberguessinggame.py
   ```

4. The program will prompt you to:

   ```
   Enter your guess:
   ```

---

##  Example Usage:

```bash
I'm thinking of a number between 1 and 100.
Enter your guess: 50
Too low! Try again.
Enter your guess: 75
Too high! Try again.
Enter your guess: forty
Invalid input. Please enter a number.
Enter your guess: 62
Congratulations! You guessed the number in 4 attempts.
```
