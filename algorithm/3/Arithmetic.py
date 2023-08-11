# Uses python3
import math
import re

def calculate(a, b, op):
    operations = {'+': a + b, '-': a - b, '*': a * b}
    return operations[op]


def get_min_and_max(min_values, max_values, i, j, operators):
    min_value = math.inf
    max_value = -math.inf
    for k in range(i, j):
        a = calculate(max_values[i][k], max_values[k+1][j], operators[k])
        b = calculate(max_values[i][k], min_values[k+1][j], operators[k])
        c = calculate(min_values[i][k], max_values[k+1][j], operators[k])
        d = calculate(min_values[i][k], min_values[k+1][j], operators[k])
        min_value = min(min_value, a, b, c, d)
        max_value = max(max_value, a, b, c, d)
    return min_value, max_value


def get_maximum_value(operands, operators):
    num_operands = len(operands)
    min_values = [[0]*num_operands for _ in range(num_operands)]
    max_values = [[0]*num_operands for _ in range(num_operands)]

    for i in range(num_operands):
        min_values[i][i] = max_values[i][i] = operands[i]

    for s in range(1, num_operands):
        for i in range(num_operands - s):
            j = i + s
            min_values[i][j], max_values[i][j] = get_min_and_max(min_values, max_values, i, j, operators)

    return max_values[0][num_operands - 1]


if __name__ == "__main__":
    expression = input().strip()
    operands = list(map(int, re.findall(r'\d+', expression)))
    operators = re.findall(r'[-+*]', expression)

    print(get_maximum_value(operands, operators))
