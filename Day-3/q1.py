def processList(arr):
    if not arr:
        return arr
    return sorted(arr)

print(processList([]))
print(processList([1]))
print(processList([7,7,7,7]))
print(processList([-5,-1,-3,-2,-4]))