# closePoint.py
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def closest_split_pair(px, py, delta, best_pair):
    mid_x = px[len(px) // 2][0]
    sy = [point for point in py if mid_x - delta <= point[0] <= mid_x + delta]

    best_distance = delta
    for i in range(len(sy) - 1):
        for j in range(i + 1, min(i + 5, len(sy))):  # Check only next 5 points; proof found in literature
            p, q = sy[i], sy[j]
            dist = euclidean_distance(p, q)
            if dist < best_distance:
                best_pair = p, q
                best_distance = dist

    return best_pair[0], best_pair[1], best_distance

def brute_force(ax):
    min_distance = euclidean_distance(ax[0], ax[1])
    p1, p2 = ax[0], ax[1]
    for i in range(len(ax) - 1):
        for j in range(i + 1, len(ax)):
            if i != 0 and j != 1:
                distance = euclidean_distance(ax[i], ax[j])
                if distance < min_distance:
                    min_distance = distance
                    p1, p2 = ax[i], ax[j]
    return p1, p2, min_distance

def closest_pair(px, py):
    if len(px) <= 3:
        return brute_force(px)

    mid = len(px) // 2
    qx, rx = px[:mid], px[mid:]

    midpoint = px[mid][0]
    qy = [point for point in py if point[0] < midpoint]
    ry = [point for point in py if point[0] >= midpoint]

    p1, q1, min_distance1 = closest_pair(qx, qy)
    p2, q2, min_distance2 = closest_pair(rx, ry)

    best_pair, best_distance = (p1, q1), min_distance1
    if min_distance2 < best_distance:
        best_pair, best_distance = (p2, q2), min_distance2

    p3, q3, min_distance3 = closest_split_pair(px, py, best_distance, best_pair)

    if min_distance3 < best_distance:
        return p3, q3, min_distance3
    else:
        return best_pair[0], best_pair[1], best_distance

def solution(points):
    sorted_by_x = sorted(points, key=lambda p: p[0])
    sorted_by_y = sorted(points, key=lambda p: (p[1], p[0]))
    p1, p2, min_distance = closest_pair(sorted_by_x, sorted_by_y)
    return min_distance

# Input
points = []
n = int(input())
for i in range(n):
    points.append([int(i) for i in input().split()])

print(solution(points))
