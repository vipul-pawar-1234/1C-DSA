def findLogetSubString(str):
    sett = set()
    left = 0
    max_length = 0

    for right in range(len(str)):

        while str[right] in sett:
            sett = sett-{str[left]}
            left+=1

        sett = sett | {str[right]}

    max_length = max(max_length,right-left+1)
    return max_length

str = "aabbbacb"
print("Longest SubString Length is:",findLogetSubString(str))
