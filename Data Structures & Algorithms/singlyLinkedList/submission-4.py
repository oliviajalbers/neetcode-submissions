class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = Node(0)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        current = self.head.next
        i = 0
        while current:
            if (i == index):
                print(self.getValues())
                return current.val
            i += 1
            current = current.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head.next
        self.head.next = newNode
        if (self.head == self.tail):
            self.tail = newNode
        print(self.getValues())
        
    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = None
        self.tail.next = newNode
        self.tail = newNode
        print(self.getValues())
        
    def remove(self, index: int) -> bool:
        prev = self.head
        current = self.head.next
        i = 0
        while current:
            if (i == index):
                prev.next = current.next
                if (self.tail == current):
                    self.tail = prev
                print(self.getValues())
                return True
            i += 1
            prev = prev.next
            current = current.next
        return False

    def getValues(self) -> List[int]:
        values = []
        current = self.head.next
        while current:
            values.append(current.val)
            current = current.next
        return values

        
