# python3
# maxprizes.py
'''n = int(input())
if n == 1:
    print(1)
    print(1)
    quit()
W = n
prizes = []
for i in range(1, n):
    if W>2*i:
        prizes.append(i)
        W -= i
    else:
        prizes.append(W)
        break

print(len(prizes))
print(' '.join([str(i) for i in prizes]))'''


n = int(input())

if n == 1:
    print(1)
    print(1)
    quit()

total = n
prizes = []

for i in range(1, n):
    if total > 2 * i:
        prizes.append(i)
        total -= i
    else:
        prizes.append(total)
        break

print(len(prizes))
print(' '.join(map(str, prizes)))
