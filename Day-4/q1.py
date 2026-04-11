import math

points = [(1, 2), (4, 5), (7, 8), (3, 1)]

min_dist = float('inf')
pair = None

for i in range(len(points)):
    for j in range(i + 1, len(points)):
        d = math.dist(points[i], points[j])
        if d < min_dist:
            min_dist = d
            pair = (points[i], points[j])

print("Closest pair:", pair[0], "-", pair[1])
print("Minimum distance:", min_dist)