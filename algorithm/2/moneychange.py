#Python3
# moneychange.py
'''
n = int(input())
count = 0
for i in [10, 5, 1]:
    if n>=i:
        q = n//i
        count += q
        n = n%i
        if n==0:
            print(count)
            quit()'''


amount = int(input())
count = 0

for i in [10, 5, 1]:
    if amount >= i:
        quotient = amount // i
        count += quotient
        amount %= i

        if amount == 0:
            print(count)
            quit()
