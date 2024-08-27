def fibonacci(n):
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence


# Example usage:
n = 10  # Number of terms in the Fibonacci series
fib_series = fibonacci(n)
print(fib_series)
