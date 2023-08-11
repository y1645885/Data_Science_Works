# python3
# maxadrevenue.py
'''n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
a.sort()
b.sort()
ans = sum([a[i]*b[i] for i in range(n)])
print(ans)'''


n = int(input())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]

a.sort()
b.sort()

total_revenue = sum([a[i] * b[i] for i in range(n)])

print(total_revenue)
