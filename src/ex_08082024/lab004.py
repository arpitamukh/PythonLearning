import sys

# Example 1: Basic usage with multiple objects
print("Hello", "world", 123)

# Example 2: Using a custom separator
print("Hello", "world", 123, sep='---')

# Example 3: Using a custom end character
print("Hello", "world", 123, end='!!!\n')

# Example 4: The output is written to a file named "output.txt"instead of the console.
with open('output.txt','w') as file:
    print("Hello", "world", 1234, sep='---', end='!', file=file,flush=True)

# Example 5: Forcibly flushing the output
print("Hello", "world", 123, flush=True)