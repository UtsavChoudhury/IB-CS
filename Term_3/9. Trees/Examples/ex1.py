class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

# advanced generator technique returning iterable
# giving more elements at request
def inorder(node):
    if node.left != None:
        yield from inorder(node.left)
    yield node.value
    if node.right != None:
        yield from inorder(node.right)


def minimum(node):
    if node.left == None:
        return node.value
    else:
        return minimum(node.left)

def add(node, value):
    if node.value == value:
        return 
    elif value < node.value:
        if node.left != None:
            add(node.left, value)
        else:
            node.left = Node(value)
    else:
        if node.right != None:
            add(node.right, value)
        else:
            node.right = Node(value)


root = Node(19)
for v in [1, 2, 3, 4, 5, 6, 7]:
    add(root, v)

print(list(inorder(root)))