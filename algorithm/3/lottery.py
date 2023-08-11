# Inputs
s, p = map(int, input().split())

segments = [tuple(map(int, input().split())) for _ in range(s)]
points = list(map(int, input().split()))

# Merge segments and points, marking them as 'l' for left endpoint, 'r' for right endpoint, and 'p' for point.
master_list = [(a, 'l') for a, _ in segments] + [(b, 'r') for _, b in segments] + [(i, 'p') for i in points]
master_list.sort()

segment_count = 0
point_segment_map = {}
for val, typ in master_list:
    if typ == 'l':
        segment_count += 1
    elif typ == 'r':
        segment_count -= 1
    else:
        point_segment_map[val] = segment_count

result = [str(point_segment_map[i]) for i in points]
print(' '.join(result))
