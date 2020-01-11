class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


first = Node(3)
print(first.data)


class LinkedList:
    def __init__(self):
        self.head = None
