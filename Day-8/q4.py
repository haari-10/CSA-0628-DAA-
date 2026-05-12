keys = ['A','B','C','D']
freq = [0.1,0.2,0.4,0.3]

n = len(keys)

cost = [[0]*(n+1) for _ in range(n+1)]
root = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    cost[i][i+1] = freq[i]
    root[i][i+1] = i+1

for length in range(2, n+1):

    for i in range(n-length+1):

        j = i + length

        cost[i][j] = float('inf')

        total = sum(freq[i:j])

        for r in range(i+1, j+1):

            c = cost[i][r-1] + cost[r][j] + total

            if c < cost[i][j]:

                cost[i][j] = c
                root[i][j] = r

print("Minimum Cost =", cost[0][n])

print("\nCost Matrix")

for row in cost:
    print(row)

print("\nRoot Matrix")

for row in root:
    print(row)