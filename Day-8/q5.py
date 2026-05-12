keys = [10,12,16,21]
freq = [4,2,6,3]

n = len(keys)

cost = [[0]*n for _ in range(n)]

for i in range(n):
    cost[i][i] = freq[i]

for L in range(2, n+1):

    for i in range(n-L+1):

        j = i+L-1

        cost[i][j] = float('inf')

        total = sum(freq[i:j+1])

        for r in range(i, j+1):

            left = cost[i][r-1] if r > i else 0
            right = cost[r+1][j] if r < j else 0

            c = left + right + total

            if c < cost[i][j]:
                cost[i][j] = c

print("Optimal Cost =", cost[0][n-1])

print("\nCost Matrix")

for row in cost:
    print(row)