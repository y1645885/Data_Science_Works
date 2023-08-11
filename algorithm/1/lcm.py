# lcm

def euclid_gcd(a, b):
    if b == 0:
        return a
    c = a % b
    return euclid_gcd(b, c)

def lcm(a, b):
    if a > b:
        gcd = euclid_gcd(a, b)
    else:
        gcd = euclid_gcd(b, a)
    return a * b // gcd

# Prompt the user for input of two numbers
a, b = map(int, input().split())

# Calculate and print the LCM
lcm_value = lcm(a, b)
print(flcm_value)
