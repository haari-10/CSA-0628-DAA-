from itertools import combinations

def subset_sums(arr):

    sums = []

    n = len(arr)

    for i in range(n + 1):

        for comb in combinations(arr, i):

            sums.append(sum(comb))

    return sums


def closest_subset_sum(arr, target):

    n = len(arr)

    left = arr[:n//2]
    right = arr[n//2:]

    left_sums = subset_sums(left)
    right_sums = subset_sums(right)

    closest = float('inf')

    for l in left_sums:

        for r in right_sums:

            total = l + r

            if abs(target - total) < abs(target - closest):

                closest = total

    return closest


arr = [45, 34, 4, 12, 5, 2]
target = 42

print("Closest Sum =", closest_subset_sum(arr, target))