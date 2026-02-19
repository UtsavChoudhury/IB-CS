# Recursively visit each sub-tree and return the size of each.

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

def get_size_1(node):
    sum = 0
    if not node:
        return 0
    sum += 1
    if node.left:
        sum += get_size_1(node.left) 
    if node.right:
        sum += get_size_1(node.right)
    return sum

def get_size_2(node):
    if not node:
        return 0
    return 1 + get_size_2(node.left) + get_size_2(node.right)



root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.right = Node(20)


print(get_size_1(root))

print(get_size_2(root))
