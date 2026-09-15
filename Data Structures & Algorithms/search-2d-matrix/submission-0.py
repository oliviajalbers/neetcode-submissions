class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            left = 0
            right = len(matrix[i]) - 1
            while left <= right:
                middle = (left + right) // 2
                if target < matrix[i][middle]:
                    right = middle - 1
                elif target > matrix[i][middle]:
                    left = middle + 1
                else:
                    return True
        return False
        