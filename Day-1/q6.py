def findMax(nums):
    if not nums:
        return None
    nums.sort()
    return nums[-1]

print(findMax([]))
print(findMax([5]))
print(findMax([3,3,3,3,3]))