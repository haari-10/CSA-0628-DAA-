lines = [
    [5,9,3],
    [6,8,4],
    [7,6,5]
]

transfer = [
    [0,2,3],
    [2,0,4],
    [3,4,0]
]

n = 3

dp = [[0]*n for _ in range(3)]

for i in range(3):
    dp[i][0] = lines[i][0]

for j in range(1, n):

    for i in range(3):

        dp[i][j] = min(
            dp[k][j-1] + transfer[k][i]
            for k in range(3)
        ) + lines[i][j]

answer = min(dp[i][n-1] for i in range(3))

print("Minimum Production Time =", answer)