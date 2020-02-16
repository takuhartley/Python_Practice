class Node:
    def __init__(self, data=None, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def getNext(self):
        return self.nextNode

    def setNext(self, newNext):
        self.nextNode = newNext


first = Node(3)
print(first.data)


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, data):
    newNode = Node(data)
    newNode.set_next(self.head)
    self.head = new_node

    def printSLL(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next

    def search(self, data):
        if(self.head == None):
            print("No Data in Linked List")

    def delete(self, data):
        current = self.head
        previous = None
        found = False
    while current and found is False:
        if current.getData == data:
            found = True
        else:
            previous = current
            current = current.get_next()
    if current is None:
        raise ValueError("Data not in list")
    if previous is None:
        self.head = current.get_next()
    else:
        previous.set_next(current.get_next())


LL = SinglyLinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.printLL()
