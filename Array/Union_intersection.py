arr1 = [1,3,2,5,6]
arr2 = [5,2,7,3,5]

ans = []

for i in arr1:
    if i not in ans:
        ans = ans+[i]

for i in arr2:
    if i not in ans:
        ans = ans+[i]

print("Union is:",ans)

ans = []

for i in arr1:
    if i in arr2 and i not in ans:
        ans = ans + [i]

print("InterSection is:",ans)