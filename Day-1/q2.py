def findCounts(nums1, nums2):
    s1, s2 = set(nums1), set(nums2)
    a1 = sum(1 for x in nums1 if x in s2)
    a2 = sum(1 for x in nums2 if x in s1)
    return [a1, a2]

print(findCounts([2,3,2],[1,2]))