class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class Deque:
    
    def __init__(self):
        self.head = Node('head')
        self.tail = Node('tail')
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False
        
    def append(self, value: int) -> None:
        newNode = Node(value)
        newNode.prev = self.tail.prev
        newNode.next = self.tail
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        
    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        newNode.prev = self.head
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode
        
    def pop(self) -> int:
        if self.isEmpty():
            return(-1)
        value = self.tail.prev.val
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        return value
        

    def popleft(self) -> int:
        if self.isEmpty():
            return(-1)
        value = self.head.next.val
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        return value

        
