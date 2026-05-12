INF = float('inf')

n = 5

dist = [[INF]*n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

edges = [
    (0,1,2),
    (0,4,8),
    (1,2,3),
    (1,4,2),
    (2,3,1),
    (3,4,1)
]

for u,v,w in edges:
    dist[u][v] = w
    dist[v][u] = w

for k in range(n):
    for i in range(n):
        for j in range(n):

            dist[i][j] = min(dist[i][j],
                             dist[i][k] + dist[k][j])

print("Shortest Path Matrix:")

for row in dist:
    print(row)