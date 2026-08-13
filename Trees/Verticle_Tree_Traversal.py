class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def verticalTraversal(root):
    if root is None:
        return []

    vertical = {}

    queue = []
    front = 0

    queue = queue + [(root, 0)]

    while front < len(queue):

        node, hd = queue[front]
        front += 1

        if hd not in vertical:
            vertical[hd] = []

        vertical[hd] = vertical[hd] + [node.data]

        if node.left:
            queue = queue + [(node.left, hd - 1)]

        if node.right:
            queue = queue + [(node.right, hd + 1)]

    ans = []

    for hd in sorted(vertical.keys()):
        ans = ans + [vertical[hd]]

    return ans


root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

ans = verticalTraversal(root)

for i in ans:
    print(i)