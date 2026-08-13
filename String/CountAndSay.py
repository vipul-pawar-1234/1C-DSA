s = "1"
for _ in range (4):
   

    result = ""
    count = 1
    for i in range (1,len(s)):

        if s[i-1] == s[i]:
            count +=1

        else:
            result+=str(count)
            result+=s[i-1]
            count = 1

    result+=str(count)
    result+=s[-1]
    s=result

print(s)