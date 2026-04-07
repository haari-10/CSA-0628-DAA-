def binarySearch(arr, key):
    arr.sort()
    l, r = 0, len(arr)-1
    while l <= r:
        m = (l+r)//2
        if arr[m] == key:
            return m
        elif arr[m] < key:
            l = m+1
        else:
            r = m-1
    return -1

arr = [3,4,6,-9,10,8,9,30]
key = 10
res = binarySearch(arr, key)
print("Found at position", res if res != -1 else "Not found")