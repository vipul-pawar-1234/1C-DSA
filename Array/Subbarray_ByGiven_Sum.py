arr = [2,-3,4,6-3,-4,6,9]
countSum = 0
max = 0

for i in range (len(arr)):
    countSum += arr[i]

    if countSum > max:
        max = countSum

    elif countSum < 0:
        countSum = 0

print(max)


    
