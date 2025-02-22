def fib(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1
    # Recursive case
    return fib(n - 1) + fib(n - 2)

def print_fib_series(n):
    # Print each Fibonacci number up to n
    for i in range(n):
        print(fib(i), end=" ")  # Print in one line with space between numbers

# Print the first 10 Fibonacci numbers
n = 10
print_fib_series(n)
