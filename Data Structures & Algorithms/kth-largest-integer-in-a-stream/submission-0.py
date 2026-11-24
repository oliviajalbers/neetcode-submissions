class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k
        for num in nums:
            self.add(num)
        

    def add(self, val: int) -> int:
        self.push(val)
        return self.heap[1]
        
    def push(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        while i > 1:
            if self.heap[i] < self.heap[i // 2]:
                temp = self.heap[i // 2]
                self.heap[i // 2] = self.heap[i]
                self.heap[i] = temp
                i = i // 2
            else:
                break
        while len(self.heap) > (self.k + 1):
            self.pop()
    
    def pop(self):
        if len(self.heap) == 1:
            return None
        elif len(self.heap) == 2:
            return self.heap.pop()
        else:
            res = self.heap[1]
            self.heap[1] = self.heap.pop()
            i = 1
            while 2 * i < len(self.heap):
                if (2 * i + 1) < len(self.heap) and self.heap[2 * i + 1] < self.heap[2 * i] and self.heap[i] > self.heap[2 * i + 1]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2 * i + 1]
                    self.heap[2 * i + 1] = temp
                    i = 2 * i + 1
                elif self.heap[i] > self.heap[2 * i]:
                    temp = self.heap[i]
                    self.heap[i] = self.heap[2 * i]
                    self.heap[2 * i] = temp
                    i = 2 * i
                else:
                    break
            return res

