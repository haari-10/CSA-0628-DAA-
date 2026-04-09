def stringMatching(words):
    res=[]
    for i in range(len(words)):
        for j in range(len(words)):
            if i!=j and words[i] in words[j]:
                res.append(words[i])
                break
    return res

print(stringMatching(["mass","as","hero","superhero"]))