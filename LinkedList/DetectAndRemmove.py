class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def detectRemoveLoop(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            break
    else:
        return head
    slow = head

    while slow != fast:
            slow = slow.next
            fast = fast.next

    loop_start = slow
    temp = loop_start

    while temp.next != loop_start:
      temp = temp.next
    temp.next = None

    return head

def printList(head):
    while head:
        print(head.data, end = " -> ")
        head = head.next

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

head.next.next.next.next.next = head.next.next
print("hello")
result = detectRemoveLoop(head)
print("Your List is:")
printList(result)