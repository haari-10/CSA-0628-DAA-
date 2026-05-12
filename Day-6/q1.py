def median_of_medians(arr, k):

    if len(arr) <= 5:
        return sorted(arr)[k]

    groups = [arr[i:i+5] for i in range(0, len(arr), 5)]

    medians = [sorted(group)[len(group)//2] for group in groups]

    pivot = median_of_medians(medians, len(medians)//2)

    low = [x for x in arr if x < pivot]
    high = [x for x in arr if x > pivot]
    equal = [x for x in arr if x == pivot]

    if k < len(low):
        return median_of_medians(low, k)

    elif k < len(low) + len(equal):
        return pivot

    else:
        return median_of_medians(high, k - len(low) - len(equal))


arr = [12, 3, 5, 7, 19]
k = 2

print("K-th Smallest Element =", median_of_medians(arr, k-1))