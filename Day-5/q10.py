A = [1,2]
B = [-2,-1]
C = [-1,2]
D = [0,2]

count = 0

for i in A:
    for j in B:
        for k in C:
            for l in D:

                if i + j + k + l == 0:
                    count += 1

print("Number of tuples =", count)