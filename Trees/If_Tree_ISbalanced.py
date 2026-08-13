class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    
    return max(height(root.left),height(root.right))+1


def isBalanced(root):
    if root is None:
        return True
    
    if abs (height(root.left) - height(root.right) ) > 1:
        return False
    
    return isBalanced(root.left) and isBalanced(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

if isBalanced(root):
    print("Tree is Balanced")

else:
    print("Tree is not balanced ")

