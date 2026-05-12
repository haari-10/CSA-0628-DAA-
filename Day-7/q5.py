from itertools import permutations

cities = ['A','B','C','D','E']

dist = {
('A','B'):10, ('A','C'):15,
('A','D'):20, ('A','E'):25,

('B','C'):35, ('B','D'):25,
('B','E'):30,

('C','D'):30, ('C','E'):20,

('D','E'):15
}

for (u,v), w in list(dist.items()):
    dist[(v,u)] = w


def get_distance(path):

    total = 0

    for i in range(len(path)-1):
        total += dist[(path[i], path[i+1])]

    total += dist[(path[-1], path[0])]

    return total


minimum = float('inf')
best_path = None

for perm in permutations(cities[1:]):

    path = ['A'] + list(perm)

    d = get_distance(path)

    if d < minimum:
        minimum = d
        best_path = path


print("Shortest Route =", best_path)
print("Distance =", minimum)