class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def checkPalindrom(head):
    stack = []
    
    curr = head
    while curr:
        stack = stack + [curr.data]
        curr = curr.next

    curr = head
    while stack:

        top = stack[-1]
        stack = stack[:-1]

        if curr.data != top:
           return False
        curr = curr.next
        
    return True


head = Node(2)
head.next = Node(1)
head.next.next = Node(1)
head.next.next.next = Node(2)

if checkPalindrom(head):
    print("Linked list is Palindrom")
else:
    print("Not a Palindrom")