import requests
import math

moby_url = 'https://gutenberg.org/files/2701/2701-0.txt'
with requests.get(moby_url, stream=True) as net:
    net_iter = net.iter_lines(decode_unicode=True)
    words = [word.lower() for line in net_iter
             for token in line.split()
             if (word := token.rstrip(' .,-')).isalpha()]

#1. TOTAL
print("TOTAL:", len(words))

#2 Binary tree 
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

root = None
for w in words:
    root = insert(root, w)

# Step 3: TREE SIZE
def get_size_2(node):
    if not node:
        return 0
    return 1 + get_size_2(node.left) + get_size_2(node.right)

size = get_size_2(root)
print("Number of unique words:", size)

#4: SMALLEST AND LARGEST
min_depth = math.ceil(math.log2(size + 1)) # not sure if ceil or floor
max_depth = size
print("Smallest possible depth:", min_depth)
print("Largest possible depth:", max_depth)

#5: ACTUAL DEPTH
def max_depth(node):
    if not node:
        return 0
    return 1 + max(max_depth(node.left), max_depth(node.right))


depth = max_depth(root)
print("Actual depth of the BT:", depth)

#6: Print 10 lexicographically smallest words
def inorder(node, result):
    if not node:
        return
    inorder(node.left, result)
    result.append(node.value)
    inorder(node.right, result)

result = []
inorder(root, result)
print("10 lexicographically smallest words:", result[:10])
