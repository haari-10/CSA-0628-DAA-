dictionary = {
    "i","like","sam","sung",
    "samsung","mobile","ice",
    "cream","icecream","man",
    "go","mango"
}

def can_segment(s):

    if len(s) == 0:
        return True

    for i in range(1, len(s)+1):

        if s[:i] in dictionary and can_segment(s[i:]):
            return True

    return False


print(can_segment("ilike"))
print(can_segment("ilikesamsung"))