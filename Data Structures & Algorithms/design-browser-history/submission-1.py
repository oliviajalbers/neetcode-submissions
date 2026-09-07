class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node("dummy")
        self.tail = Node("dummy")
        newNode = Node(homepage)
        newNode.prev = self.head
        newNode.next = self.tail
        self.head.next = newNode
        self.tail.prev = newNode
        self.current = newNode
        self.printHistory()

    def visit(self, url: str) -> None:
        newNode = Node(url)
        newNode.prev = self.current
        newNode.next = self.tail
        self.tail.prev = newNode
        self.current.next = newNode
        self.current = newNode
        self.printHistory()
        
    def back(self, steps: int) -> str:
        i = 0
        while (i < steps and self.current.prev != self.head):
            self.current = self.current.prev
            i += 1
        self.printHistory()
        return self.current.val

        

    def forward(self, steps: int) -> str:
        i = 0
        while (i < steps and self.current.next != self.tail):
            self.current = self.current.next
            i += 1
        self.printHistory()
        return self.current.val
    
    def printHistory(self):
        history = []
        currentSite = self.head.next
        while (currentSite != self.tail):
            history.append(currentSite.val)
            currentSite = currentSite.next
        print(history)
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)