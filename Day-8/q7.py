import heapq

def maxProbability(n, edges, succProb, start, end):

    graph = [[] for _ in range(n)]

    for (u,v), p in zip(edges, succProb):

        graph[u].append((v,p))
        graph[v].append((u,p))

    pq = [(-1, start)]

    prob = [0]*n

    prob[start] = 1

    while pq:

        p, node = heapq.heappop(pq)

        p = -p

        if node == end:
            return p

        for nei, edgeProb in graph[node]:

            newProb = p * edgeProb

            if newProb > prob[nei]:

                prob[nei] = newProb

                heapq.heappush(pq,
                               (-newProb, nei))

    return 0


n = 3

edges = [[0,1],[1,2],[0,2]]

succProb = [0.5,0.5,0.2]

print(maxProbability(n, edges,
                     succProb, 0, 2))