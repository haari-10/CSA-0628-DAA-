def quick_sort(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)


arr = [10,16,8,12,15,6,3,9,5]

sorted_array = quick_sort(arr)

print("Sorted Array:", sorted_array)