arr = [3,2,6,4,9,1,8,7,3,7]
target = 10


for i in range(len(arr)-1):
     if arr[i] + arr[i+1] == target:
        print(arr[i],arr[i+1])
