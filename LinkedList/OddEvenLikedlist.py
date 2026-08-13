class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def oddEven(head):

    if not head or not head.next:
        return head
    
    odd = head
    even =  head.next
    evenHead = even

    while even and even.next:
        odd.next = even.next
        odd = odd.next

        even.next = odd.next
        even = even.next
    odd.next = evenHead
    return head

def printLinked(head):
    while head:
        print(head.data,end = " -> ")
        head = head.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

result = oddEven(head)
printLinked(result)