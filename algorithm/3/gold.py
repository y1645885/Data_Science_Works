# Discrete Knapsack problem without repetition
def maxGoldWeight(W, n, items):
    value = [[0 for _ in range(n+1)] for _ in range(W+1)]
    for i in range(1, W+1):
        for j in range(1, n+1):
            value[i][j] = value[i][j-1]
            if items[j-1]<=i:
                temp = value[i-items[j-1]][j-1] + items[j-1]
                if temp > value[i][j]:
                    value[i][j] = temp
    return (value[W][n], value)

def printItems(value, items, i, j, arr):
    if i < 0 or j < 0:
        arr.reverse()
        return arr
    if value[i][j] == value[i][j-1]:
        arr.append(0)
        return printItems(value, items, i, j-1, arr)
    else:
        arr.append(1)
        return printItems(value, items, i-items[j-1], j-1, arr)
        
if __name__ == '__main__':
    W, n = map(int, input().split())
    item_weights = list(map(int, input().split()))
    max_weight, Matrix = maxGoldWeight(W, n, item_weights)
    bool_vector = printItems(Matrix, item_weights, W, n, [])
    optimal = [str(j) for i, j in enumerate(item_weights) if bool_vector[i]]
    print(f"Max Weights in knapsack of capacity {W}: {' '.join(optimal)}")
