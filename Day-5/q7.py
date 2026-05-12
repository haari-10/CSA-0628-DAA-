arr = [5,10,15,20,25,30,35,40,45]

key = 20

low = 0
high = len(arr) - 1

count = 0

while low <= high:

    mid = (low + high) // 2

    count += 1

    if arr[mid] == key:
        print("Position =", mid + 1)
        print("Comparisons =", count)
        break

    elif arr[mid] < key:
        low = mid + 1

    else:
        high = mid - 1