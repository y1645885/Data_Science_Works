# Python 3
# binary.py
def binary_search(seq, element, r):
    l = 0
    while l <= r:
        mid = (l + r) // 2
        if element > seq[mid]:
            l = mid + 1
        elif element < seq[mid]:
            r = mid - 1
        else:
            return mid
    return -1

def main():
    seq = list(map(int, input().split()))[1:]
    search_seq = list(map(int, input().split()))[1:]
    n = len(seq)

    soln = []
    for i in search_seq:
        ans = binary_search(seq, i, n - 1)
        soln.append(ans)

    print(' '.join(map(str, soln)))

if __name__ == "__main__":
    main()
