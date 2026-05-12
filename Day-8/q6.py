from collections import deque

def catMouseGame(graph):

    n = len(graph)

    DRAW = 0
    MOUSE = 1
    CAT = 2

    color = [[[DRAW]*2 for _ in range(n)] for _ in range(n)]

    queue = deque()

    for i in range(1, n):

        color[0][i][0] = MOUSE
        color[0][i][1] = MOUSE

        queue.append((0,i,0,MOUSE))
        queue.append((0,i,1,MOUSE))

        color[i][i][0] = CAT
        color[i][i][1] = CAT

        queue.append((i,i,0,CAT))
        queue.append((i,i,1,CAT))

    return DRAW


graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]

print(catMouseGame(graph))