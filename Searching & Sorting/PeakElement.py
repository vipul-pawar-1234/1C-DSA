def findPeak(arr):
    for i in range(1,len(arr)-1):
        if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
            return arr[i]
        
arr = [1,2,9,15,6]

print("Peak element is:",findPeak(arr))