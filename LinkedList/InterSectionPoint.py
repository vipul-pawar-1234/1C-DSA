class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def getInterSection(headA,headB):
    sett = set()

    current = headA
    while current:
        sett = sett |{current}
        current = current.next
    
    current = headB
    while current:
        if current in sett:
            return current
        current = current.next
    return None

common1 = Node(7)
common2 = Node(8)
common3 = Node(9)

common1.next = common2
common2.next = common3

headA = Node(1)
headA.next = Node(2)
headA.next.next = Node(3)
headA.next.next.next = common1

headB = Node(4)
headB.next = Node(5)
headB.next.next = common1


result = getInterSection(headA,headB)

if result:
    print("Intersection is:",result.data)
else:
    print("Not Intersection")


