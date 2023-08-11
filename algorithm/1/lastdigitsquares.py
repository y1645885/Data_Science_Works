# lastdigitsquares

def fibonacci_last_digit(n):
    a, b = 0, 1
    for _ in range(2, n + 1):
        c = (a + b) % 10
        b, a = c, b
    return c

n = int(input())
lesser_n = n % 60
lesser_nplus = (n + 1) % 60

if lesser_n <= 1:
    a = lesser_n
else:
    a = fibonacci_last_digit(lesser_n)
    
if lesser_nplus <= 1:
    b = lesser_nplus
else:
    b = fibonacci_last_digit(lesser_nplus)

result = (a * b) % 10
print(result)
