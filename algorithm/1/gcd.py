# gcd

def compute_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Prompt the user for input of two numbers
a, b = map(int, input().split())

# Calculate and print the GCD
gcd = compute_gcd(a, b)
print(gcd)
