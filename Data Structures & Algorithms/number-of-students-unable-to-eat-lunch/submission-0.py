class Node:
    def __init__ (self, value):
        self.value = value
        self.next = None

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_count = len(students)
        student_deque = deque(students)
        result = student_count
        for sandwich in sandwiches:
            count = 0
            while count < student_count and student_deque[0] != sandwich:
                current = student_deque.popleft()
                student_deque.append(current)
                count += 1
            if student_deque[0] == sandwich:
                student_deque.popleft()
                result -= 1
                student_count -= 1
            else: 
                break
        return result