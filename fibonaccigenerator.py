def fibonacci(n):
    a, b = 0, 1
    if n <= 0:
        print("Please enter a positive integer.")
    elif n == 1:
        print("Fibonacci sequence up to 1:")
        print(a)
    else:
        print("Fibonacci sequence:")
        for _ in range(n):
            print(a, end=" ")
            a, b = b, a + b
fibonacci(10)