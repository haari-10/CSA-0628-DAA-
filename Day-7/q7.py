def length_of_longest_substring(s):

    seen = {}

    left = 0
    maximum = 0

    for right in range(len(s)):

        if s[right] in seen and seen[s[right]] >= left:
            left = seen[s[right]] + 1

        seen[s[right]] = right

        maximum = max(maximum, right-left+1)

    return maximum


print(length_of_longest_substring("abcabcbb"))
print(length_of_longest_substring("bbbbb"))
print(length_of_longest_substring("pwwkew"))