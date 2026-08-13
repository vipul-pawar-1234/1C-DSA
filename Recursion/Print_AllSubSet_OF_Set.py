def subSet(arr,index,current):
    if index == len(arr):
        print(current)
        return
    
    current = current+[arr[index]]
    subSet(arr,index+1,current)

    current = current[:-1]
    subSet(arr,index+1,current)
    

arr = [1,2,3]
print("All subset is:")
subSet(arr,0,[])