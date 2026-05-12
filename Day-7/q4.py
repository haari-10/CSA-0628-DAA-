from itertools import permutations

def tsp(graph):

    n = len(graph)

    vertices = list(range(1, n))

    minimum = float('inf')

    for perm in permutations(vertices):

        current = 0
        k = 0

        for j in perm:
            current += graph[k][j]
            k = j

        current += graph[k][0]

        minimum = min(minimum, current)

    return minimum


graph = [
    [0,10,15,20],
    [10,0,35,25],
    [15,35,0,30],
    [20,25,30,0]
]

print("Minimum Distance =", tsp(graph))