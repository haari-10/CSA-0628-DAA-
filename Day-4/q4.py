import itertools
import math

def distance(c1, c2):
    return math.dist(c1, c2)

def tsp(cities):
    start = cities[0]
    others = cities[1:]
    min_path = None
    min_dist = float('inf')
    
    for perm in itertools.permutations(others):
        path = [start] + list(perm) + [start]
        dist = 0
        for i in range(len(path)-1):
            dist += distance(path[i], path[i+1])
        if dist < min_dist:
            min_dist = dist
            min_path = path
    return min_dist, min_path

cities1 = [(1,2),(4,5),(7,1),(3,6)]
cities2 = [(2,4),(8,1),(1,7),(6,3),(5,9)]

print("Test Case 1:", tsp(cities1))
print("Test Case 2:", tsp(cities2))