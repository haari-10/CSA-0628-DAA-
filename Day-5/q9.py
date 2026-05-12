points = [[1,3],[-2,2],[5,8],[0,1]]

k = 2

points.sort(key=lambda p: p[0]**2 + p[1]**2)

print("Closest Points:", points[:k])