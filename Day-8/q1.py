INF = float('inf')

n = 4

dist = [
    [0, 3, INF, INF],
    [INF, 0, 1, 4],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

print("Before:")

for row in dist:
    print(row)

for k in range(n):
    for i in range(n):
        for j in range(n):

            dist[i][j] = min(dist[i][j],
                             dist[i][k] + dist[k][j])

print("\nAfter:")

for row in dist:
    print(row)