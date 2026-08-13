class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def deleteElement(head,n):

    length = 0

    curr = head
    while curr:
        length+=1
        curr = curr.next

    curr = head
    for i in range (length-n-1):
        curr = curr.next
    curr.next = curr.next.next

    return head
def printList(head):
    while head:
        print(head.data,end= " ")
        head = head.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

result = deleteElement(head,3)
printList(result)