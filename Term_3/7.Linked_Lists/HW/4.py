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
    

def remove(head, value):
    if head == None:
        return head
    if head.value == value:
        return head.next_node

    curr = head
    while True:
        if curr.next_node == None:
            break
        if curr.next_node.value == value:
            curr.next_node = curr.next_node.next_node
            break 

        curr = curr.next_node

    return head



head = Node(5)
head.add(-1)
head.add(19)
print(head)
