class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    
def LCA(root,p,q):
    if root == None:
        return root
    
    if root.data == p or root.data == q:
        return root
    
    left = LCA(root.left,p,q)
    right = LCA(root.right,p,q)

    if left and right:
        return root
    
    if left:
        return left
    
    return right

root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

ans = LCA(root,5,7)

print("Lowest common Ancestor",ans.data)