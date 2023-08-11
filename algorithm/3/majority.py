# Python 3
# majority.py

def divide_and_conquer(seq, l, r):
    if l + 1 == r:
        return seq[l]
    elif l + 2 == r:
        return seq[l]
    m = (l + r) // 2
    left = divide_and_conquer(seq, l, m)
    right = divide_and_conquer(seq, m, r)

    count_left, count_right = 0, 0
    for i in seq[l:r]:
        if i == left:
            count_left += 1
        elif i == right:
            count_right += 1

    if count_left > (r - l) // 2 and left != -1:
        return left
    elif count_right > (r - l) // 2 and right != -1:
        return right
    else:
        return -1

def majority_element_exists(seq):
    n = len(seq)
    return int(divide_and_conquer(seq, 0, n) != -1)

if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split()))

    result = majority_element_exists(seq)
    print(result)
