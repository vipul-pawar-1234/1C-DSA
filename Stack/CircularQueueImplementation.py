size = 5
arr = [0] * size

front = 0
rear = 0
count = 0

def enqueue(data):
    global rear, count

    arr[rear] = data
    print("Element is added in queue")
    rear = (rear + 1) % size
    count += 1



def dequeue():
    global front, count

    print("Deleted:", arr[front])

    front = (front + 1) % size
    count -= 1

def peek():
    print("Top element is:", arr[front])

def display():

    i = front

    for j in range(count):
        print(arr[i], end=" ")
        i = (i + 1) % size
    print()

enqueue(10)
enqueue(20)
enqueue(30)
enqueue(40)

peek()
dequeue()
display()