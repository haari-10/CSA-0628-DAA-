def gameOfLife(board):
    m, n = len(board), len(board[0])
    dirs = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    copy = [row[:] for row in board]
    for i in range(m):
        for j in range(n):
            live = 0
            for dx, dy in dirs:
                x, y = i+dx, j+dy
                if 0 <= x < m and 0 <= y < n and copy[x][y] == 1:
                    live += 1
            if copy[i][j] == 1 and (live < 2 or live > 3):
                board[i][j] = 0
            elif copy[i][j] == 0 and live == 3:
                board[i][j] = 1
    return board

print(gameOfLife([[0,1,0],[0,0,1],[1,1,1],[0,0,0]]))