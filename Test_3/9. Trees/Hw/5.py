#Considering the case where may be unbalanced a.k.a not sufficient to check until we hit None
# Recursively traverse; for each subtree return max depth on left and right


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)


