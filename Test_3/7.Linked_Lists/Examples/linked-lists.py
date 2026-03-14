class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None
        
    def add(self, value):
        if self.next_node == None:
            self.next_node = Node(value)
        else:
            self.next_node.add(value)
            
    def __str__(self):
        value_strs = []
        node = self
        while True:
            value_strs.append(str(node.value))
            node = node.next_node
            if node == None:
                break
        return ' '.join(value_strs)

def find_recur(node, value):
    if node == None:
        return False
    if node.value == value:
        return True
    return find_recur(node.next_node, value)



def find_iter(node, value):
    while True:
        if node == None:
            return False
        if node.value == value:
            return True
        node = node.next_node

head = Node(5)
head.add(-1)
head.add(19)
print(head)
