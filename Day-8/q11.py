
import heapq

def networkDelayTime(times, n, k):

    graph = [[] for _ in range(n+1)]

    for u,v,w in times:

        graph[u].append((v,w))

    pq = [(0,k)]

    dist = [float('inf')] * (n+1)

    dist[k] = 0

    while pq:

        time,node = heapq.heappop(pq)

        for nei,w in graph[node]:

            newTime = time + w

            if newTime < dist[nei]:

                dist[nei] = newTime

                heapq.heappush(pq,
                               (newTime, nei))

    answer = max(dist[1:])

    return answer if answer != float('inf') else -1


times = [[2,1,1],
         [2,3,1],
         [3,4,1]]

print(networkDelayTime(times, 4, 2))