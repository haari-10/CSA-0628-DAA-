def firstPalindrome(words):
    for w in words:
        if w == w[::-1]:
            return w
    return ""

print(firstPalindrome(["abc","car","ada","racecar","cool"]))