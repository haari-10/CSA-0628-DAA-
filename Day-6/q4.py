from itertools import combinations

def subset_sums(arr):

    sums = []

    for i in range(len(arr) + 1):

        for comb in combinations(arr, i):

            sums.append(sum(comb))

    return sums


def exact_subset_sum(arr, target):

    n = len(arr)

    left = arr[:n//2]
    right = arr[n//2:]

    left_sums = subset_sums(left)
    right_sums = subset_sums(right)

    right_set = set(right_sums)

    for s in left_sums:

        if target - s in right_set:
            return True

    return False


arr = [1, 3, 9, 2, 7, 12]
target = 15

print(exact_subset_sum(arr, target))