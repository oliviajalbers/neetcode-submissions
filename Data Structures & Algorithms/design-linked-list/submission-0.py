class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        current = self.head.next 
        i = 0
        while (current != self.tail):
            if (index == i):
                return current.val
            current = current.next
            i += 1
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        current = self.head.next
        i = 0
        while (current != self.tail):
            if (i == index):
                newNode.next = current
                newNode.prev = current.prev
                current.prev.next = newNode
                current.prev = newNode
            current = current.next
            i += 1
        if (i == index and current == self.tail):
            newNode.next = self.tail
            newNode.prev = self.tail.prev
            self.tail.prev.next = newNode
            self.tail.prev = newNode


    
    def deleteAtIndex(self, index: int) -> None:
        current = self.head.next
        i = 0
        while (current != self.tail):
            if (i == index):
                current.prev.next = current.next
                current.next.prev = current.prev
            current = current.next
            i += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)