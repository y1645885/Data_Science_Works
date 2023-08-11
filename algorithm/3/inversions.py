def merge(left, right):
    i, j, inversion_counter = 0, 0, 0
    final = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            final.append(left[i])
            i += 1
        else:
            final.append(right[j])
            inversion_counter += len(left) - i
            j += 1

    final += left[i:]
    final += right[j:]

    return final, inversion_counter

def mergesort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2
    left, left_count = mergesort(arr[:mid])
    right, right_count = mergesort(arr[mid:])
    sorted_arr, merge_count = merge(left, right)

    total_count = left_count + right_count + merge_count
    return sorted_arr, total_count

if __name__ == "__main__":
    n = int(input())
    seq = list(map(int, input().split()))

    sorted_seq, inversion_count = mergesort(seq)
    print(inversion_count)
