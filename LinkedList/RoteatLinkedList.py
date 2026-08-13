class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def roteat(head,k):
 
 for _ in range(k):
    prev = None
    curr = head

    if not head or not head.next:
       return head
    
    while curr.next :
       prev = curr
       curr = curr.next

    prev.next = None
    curr.next = head
    head = curr

 return head

        
def printLL(head):
    while  head:
        print(head.data,end = " ")
        head = head.next
    


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)


result = roteat(head,1)
print("Roatat list is:")
printLL(result)