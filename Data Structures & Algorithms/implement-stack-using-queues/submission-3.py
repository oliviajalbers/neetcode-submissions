class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        newQ = deque()
        while not self.empty():
            val = self.q.popleft()
            if self.empty():
                self.q = newQ
                return val
            newQ.append(val)
        

    def top(self) -> int:
        newQ = deque()
        val = None
        while not self.empty():
            val = self.q.popleft()
            newQ.append(val)
        self.q = newQ
        return val

    def empty(self) -> bool:
        if not self.q:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()