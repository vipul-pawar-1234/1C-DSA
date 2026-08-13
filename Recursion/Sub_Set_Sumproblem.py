def subSet(arr,target,index):
    if target == 0:
        return True
    
    if target<0:
        return False
    
    if index == len(arr):
        return False
    
    if subSet(arr,target - arr[index] , index+1):
        return True
    
    if subSet(arr, target , index+1):
        return True
    
    return False



arr = [3, 34, 4, 12, 5, 2]
target = 9

print(subSet(arr,target,0))