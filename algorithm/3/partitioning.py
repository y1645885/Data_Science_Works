def partition3(A):
    total_sum = sum(A)
    n = len(A)

    if total_sum % 3 != 0:
        return 0

    target = total_sum // 3
    count = [0] * (target + 1)
    count[0] = 1
    for i in A:
        for j in range(target, i - 1, -1):
            if count[j - i]:
                count[j] += count[j - i]
            if count[target] > 2:
                return 1
    return 0

if __name__ == '__main__':
    n = int(input())
    A = list(map(int, input().split()))
    print(partition3(A))
