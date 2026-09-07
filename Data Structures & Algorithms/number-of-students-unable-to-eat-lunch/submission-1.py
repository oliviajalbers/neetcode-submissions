class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        dq = deque(students)
        studentCount = len(students)
        didntTake = 0
        i = 0
        while i < len(sandwiches) and didntTake < studentCount:
            if dq[0] == sandwiches[i]:
                dq.popleft()
                i += 1
                didntTake = 0
                studentCount -= 1
            else:
                choice = dq.popleft()
                dq.append(choice)
                didntTake += 1
        return len(dq)
        