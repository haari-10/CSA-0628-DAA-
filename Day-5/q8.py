arr = [3,9,14,19,25,31,42,47,53]

key = 31

low = 0
high = len(arr) - 1

while low <= high:

    mid = (low + high) // 2

    print("Low =", low,
          "High =", high,
          "Mid =", mid,
          "Value =", arr[mid])

    if arr[mid] == key:
        print("Element found at position", mid + 1)
        break

    elif arr[mid] < key:
        low = mid + 1

    else:
        high = mid - 1