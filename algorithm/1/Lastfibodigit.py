# Lastfibodigit
def last_digit_fibo(n):
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(n-1):
        c = (a + b) % 10
        a, b = b, c
    
    return c

# Prompt the user for input
n = int(input())

# Calculate and print the last digit of the Fibonacci number
result = last_digit_fibo(n)
print(result)
