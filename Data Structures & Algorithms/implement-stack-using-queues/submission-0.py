class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class MyStack:

    def __init__(self):
        self.head = None
        self.tail = None
        

    def push(self, x: int) -> None:
        newNode = Node(x)
        newNode.next = self.head
        self.head = newNode
        if (self.tail == None):
            self.tail = newNode

    def pop(self) -> int:
        if (self.empty()):
            return None
        current = self.head
        if self.tail == self.head:
            self.tail = self.tail.next
        self.head = self.head.next
        return current.value
        

    def top(self) -> int:
        return self.head.value
        

    def empty(self) -> bool:
        if self.head == None:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()