def findPaths(m, n, N, i, j):
    dp = [[0]*n for _ in range(m)]
    dp[i][j] = 1
    count = 0
    for _ in range(N):
        temp = [[0]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                if dp[r][c]:
                    val = dp[r][c]
                    if r == 0: count += val
                    else: temp[r-1][c] += val
                    if r == m-1: count += val
                    else: temp[r+1][c] += val
                    if c == 0: count += val
                    else: temp[r][c-1] += val
                    if c == n-1: count += val
                    else: temp[r][c+1] += val
        dp = temp
    return count

print(findPaths(2,2,2,0,0))