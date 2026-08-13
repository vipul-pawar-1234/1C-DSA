list = [2,4,3,7,5,8,6]
target = 7
n = len(list)
for i in range(n):
    if target == list[i]+list[i+1] :
        print("Index of number is",i , i+1)
        break


