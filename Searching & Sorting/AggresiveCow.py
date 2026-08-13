def canPlace(stalls,cow,dis):
    count = 1
    last = stalls[0]

    for i in range(1,len(stalls)):
        if stalls[i] - last >= dis:
            count+=1
            last = stalls[i]

        if count == cow:
            return True
    
    return False

def aggresiveCow(stalls,cow):
    stalls.sort()

    low = 1
    high = stalls[-1] - stalls[0]
    answer = 0
    while low <= high:
        mid = (low+high) // 2

        if canPlace(stalls,cow,mid):
            answer = mid
            low = mid+1
        
        else:
            high = mid-1
    
    return answer

stalls = [1,2,3,4,5]
cow = 4

print("Maximum and Minimum Distance:",aggresiveCow(stalls,cow))
