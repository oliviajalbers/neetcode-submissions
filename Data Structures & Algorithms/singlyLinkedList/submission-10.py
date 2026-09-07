class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def get(self, index: int) -> int:
        i = 0
        current = self.head
        while (current != None):
            if (i == index):
                return current.value
            else:
                i += 1
                current = current.next
        return -1

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        if (self.tail == None):
            self.tail = newNode
        
    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if (self.head == None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        
    def remove(self, index: int) -> bool:
        # if empty
        if (self.head == None):
            return False
        # if length 1
        if (self.head == self.tail and index == 0):
            self.head = None
            self.tail = None
            return True
        # if index 0
        if (index == 0):
            self.head = self.head.next
            return True
        # all other
        prev = self.head
        curr = self.head.next
        i = 1
        while (curr != None):
            if (i == index):
                prev.next = prev.next.next
                if (prev.next == None):
                    self.tail = prev
                return True
            else:
                i += 1
                prev = prev.next
                curr = curr.next
        return False

        
         
        
    def getValues(self) -> List[int]:
        myList = []
        current = self.head
        while (current):
            myList.append(current.value)
            current = current.next
        return myList
        
