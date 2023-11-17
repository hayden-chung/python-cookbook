class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def append_item(self, value):
    if self is None:
        return Node(value)
    
    self.next = append_item(self.next, value)
    return self

l = Node(5)
l = append_item(l, 30)
l = append_item(l, 15)

print(l.next.value)
