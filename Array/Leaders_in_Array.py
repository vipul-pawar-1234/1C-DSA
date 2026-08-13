arr = [18,25,6,2]
leader = []
max = 0

for i in range (len(arr)-1,-1,-1):
    if max < arr[i]:
        leader = leader + [arr[i]]
        max = arr[i]


print(leader)