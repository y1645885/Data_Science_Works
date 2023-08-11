def fibonacci(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    
    return b

# Prompt the user for input
n = int(input())

# Calculate and print the Fibonacci number
result = fibonacci(n)
print(result)
