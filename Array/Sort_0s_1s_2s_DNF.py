arr = [2,2,0,1,0,2,0,0,1]
print("Array before sorting",arr)
zero = 0
one = 0
two = 0
for i in range(len(arr)):
    if arr[i] == 0:
        zero+=1
    elif arr[i] == 1:
        one+=1
    else:
        two+=1

for i in range(len(arr)):
    if zero>0:
        arr[i]=0
        zero-=1
    elif one>0:
        arr[i]=1
        one-=1
    else:
        arr[i]=2
        two-=1
print("Array after sorting",arr)

