class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def zigzagTraversal(root):
    if root is None:
        return []

    queue = []
    front = 0

    queue = queue + [root]

    ans = []
    lefttoRight = True

    while front < len(queue):

        level = []

        levelStart = front
        levelEnd = len(queue)

        while front < levelEnd:

            node = queue[front]
            front += 1

            level = level + [node.data]

            if node.left:
                queue = queue + [node.left]

            if node.right:
                queue = queue + [node.right]

        if lefttoRight == False:

            temp = []

            for i in range(len(level) - 1, -1, -1):
                temp = temp + [level[i]]

            level = temp

        ans = ans + [level]

        lefttoRight = not lefttoRight

    return ans


root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

root.right.left = Node(6)
root.right.right = Node(7)

ans = zigzagTraversal(root)

for i in ans:
    print(i)