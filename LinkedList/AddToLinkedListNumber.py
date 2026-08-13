class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def addListSum(l1,l2):
    dummy = Node(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        sum = carry
        if l1:
            sum += l1.data
            l1 = l1.next
        if l2:
            sum += l2.data
            l2 = l2.next

        carry = sum // 10
        digit = sum % 10

        current.next = Node(digit)        
        current = current.next
    
    return dummy.next

def printsum(head):
    while head:
        print(head.data , end = " ")
        head = head.next

l1 = Node(4)
l1.next = Node(4)
l1.next.next = Node(4) # l1 = 4 -> 4 -> 4

l2 = Node(4)
l2.next = Node(4)
l2.next.next = Node(4) # l2 = 4 -> 4 -> 4 

result = addListSum(l1,l2)

print("Your Linked List Sum is:")
printsum(result)

