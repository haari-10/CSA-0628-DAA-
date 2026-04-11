import math

def dist(p1, p2):
    return math.dist(p1, p2)

def closest_pair(points):
    min_d = float('inf')
    pair = None
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = dist(points[i], points[j])
            if d < min_d:
                min_d = d
                pair = (points[i], points[j])
    return pair, min_d

points = [(10,0),(11,5),(5,3),(9,3.5),(15,3),(12.5,7),(6,6.5),(7.5,4.5)]

pair, d = closest_pair(points)
print(pair, d)
print("Time Complexity: O(n^2)")