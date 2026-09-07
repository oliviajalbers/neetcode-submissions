class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        studentsLeft = len(students)
        studentCount = {}
        for student in students:
            if student not in studentCount:
                studentCount[student] = 0
            studentCount[student] += 1
        
        for sandwich in sandwiches:
            if sandwich in studentCount and studentCount[sandwich] > 0:
                studentCount[sandwich] -= 1
                studentsLeft -= 1
            else:
                return studentsLeft
        
        return studentsLeft