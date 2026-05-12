INF = float('inf')

routers = 6

dist = [[INF]*routers for _ in range(routers)]

for i in range(routers):
    dist[i][i] = 0

edges = [
    (0,1,1),
    (0,2,5),
    (1,2,2),
    (1,3,1),
    (2,4,3),
    (3,4,1),
    (3,5,6),
    (4,5,2)
]

for u,v,w in edges:
    dist[u][v] = w
    dist[v][u] = w

def floyd(d):

    n = len(d)

    for k in range(n):
        for i in range(n):
            for j in range(n):

                d[i][j] = min(d[i][j],
                              d[i][k] + d[k][j])

floyd(dist)

print("A to F before failure =", dist[0][5])

# Remove B-D link
dist[1][3] = INF
dist[3][1] = INF

floyd(dist)

print("A to F after failure =", dist[0][5])