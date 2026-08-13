def canAllocate(books,students,max_length):
    count = 1
    page = 0

    for book in books:
        if page+book <= max_length:
            page += book
        
        else:
            count += 1
            page = book

    return count <= students
        
def bookAllocate(books,students):
    low = max(books)
    high = sum(books)
    answer = high

    while low <= high:
        mid = (low+high) // 2

        if canAllocate(books,students,mid):
            answer = mid
            high = mid-1
        
        else:
            low = mid+1
            
    return answer

books = [10,20,30,40]
students = 2

print("Minimum and Maximum allocation is:",bookAllocate(books,students))

