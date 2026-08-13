def anagram(str):
    groups = {}

    for word in str:
        char = sorted(word)

        key = ""
        for ch in char:
            key+=ch

        if key in groups:
            groups[key] = groups[key] + [word]

        else:
            groups[key] = [word]

    return list(groups.items())

str = ["eat","tea","tan","ate","nat","bat"]
print(anagram(str))