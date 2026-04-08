def rob(nums):
    def solve(arr):
        prev = curr = 0
        for x in arr:
            prev, curr = curr, max(curr, prev + x)
        return curr
    if len(nums) == 1:
        return nums[0]
    return max(solve(nums[:-1]), solve(nums[1:]))

print(rob([2,3,2]))