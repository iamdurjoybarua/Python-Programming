# factorialcalculator.py

This program calculates the factorial of a non-negative integer. It serves as a great example for demonstrating two different fundamental approaches to solving a problem: an iterative method and a recursive method.

---

##  Key Features:

- **Iterative Factorial**: Calculates the factorial using a simple `for` loop, which is straightforward and easy to understand.

- **Recursive Factorial**: Calculates the factorial by defining a function that calls itself, showcasing the concept of recursion with a clear base case (`if n == 0`).

- **Input Validation**: Uses a `try-except` block to gracefully handle non-integer input from the user, preventing the program from crashing.

---

##  How to Run:

1. Save the code as `factorial_calculator.py`.

2. Open your terminal or command prompt.

3. Run the script with the following command:

   ```bash
   python factorial_calculator.py
   ```

4. The program will prompt you to:

   ```
   Enter a non-negative integer:
   ```

---

##  Example Usage:

```bash
Enter a non-negative integer: 5
Factorial of 5 (iterative): 120
Factorial of 5 (recursive): 120
```

---

##  Potential Enhancements:

- Add a loop to allow the user to calculate factorials for multiple numbers without restarting the program.

- Implement a check to ensure the input number is non-negative before calling the functions.

- Add a graphical user interface (GUI) to make the program more user-friendly.
