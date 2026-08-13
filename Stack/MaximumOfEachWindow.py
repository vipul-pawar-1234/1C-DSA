def slidingWindow(arr,k):
   
    ans = []

    for i in range(len(arr) - k+1):
        maximum = arr[i]

        for j in range(i,k+i):
            if maximum < arr[j]:
                maximum = arr[j]
        
        ans = ans + [maximum]
    
    return ans



arr = [1,3,-2,-3,5,3,6,7]
k = 4

print(slidingWindow(arr,k))
