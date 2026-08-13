arr = [3,4,2,5,5,1,3]

totalSum = sum(arr)
leftSum = 0

for i in range (len(arr)):
    rightSum = totalSum-leftSum-arr[i]

    if leftSum == rightSum:
        print("Equilibrium index is",i)
        break

    else:
        leftSum+=arr[i]



