INF = float('inf')

def findTheCity(n, edges, threshold):

    dist = [[INF]*n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u,v,w in edges:
        dist[u][v] = w
        dist[v][u] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):

                dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j])

    answer = -1
    minimum = INF

    for i in range(n):

        count = 0

        for j in range(n):

            if dist[i][j] <= threshold:
                count += 1

        if count <= minimum:

            minimum = count
            answer = i

    return answer


n = 4

edges = [[0,1,3],
         [1,2,1],
         [1,3,4],
         [2,3,1]]

print(findTheCity(n, edges, 4))