class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        
    def get(self, index: int) -> int:
        current = self.head.next
        i = 0
        while (i < index and current):
            current = current.next
            i += 1
        if current: 
            return current.val
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next = newNode
        if (newNode.next):
            newNode.next.prev = newNode
        if (self.head == self.tail):
            self.tail = newNode
        
    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        
    def addAtIndex(self, index: int, val: int) -> None:
        newNode = ListNode(val)
        current = self.head.next
        i = 0
        while (i < index and current):
            current = current.next
            i += 1
        if (current):
            newNode.prev = current.prev
            newNode.next = current
            if current.prev:
                current.prev.next = newNode
            else:
                self.head = newNode
            current.prev = newNode
        else:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode

        
    def deleteAtIndex(self, index: int) -> None:
        current = self.head.next
        i = 0
        while (i < index and current):
            current = current.next
            i += 1
        if (current):
            current.prev.next = current.next
            if (current.next):
                current.next.prev = current.prev
            else:
                self.tail = current.prev
    
    def printList(self) -> None:
        current = self.head.next
        arr = []
        while current:
            arr.append(current.val)
            current = current.next
        print(arr)

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)