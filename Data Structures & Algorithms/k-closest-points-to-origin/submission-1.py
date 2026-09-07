import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # call quickSort on List
        self.quickSort(points, 0, len(points) - 1)
        # return the first k
        return points[:k]

    def quickSort(self, points, start, end):
        # base case
        if (end - start) <= 0:
            return points
        left = start
        pivot = points[end]
        for i in range(start, end):
            if self.getDistance(points[i][0], points[i][1]) < self.getDistance(pivot[0], pivot[1]):
                temp = points[left]
                points[left] = points[i]
                points[i] = temp
                left += 1
        # swap pivot
        temp = points[left]
        points[left] = pivot
        points[end] = temp
        # recursive callse
        self.quickSort(points, start, left - 1)
        self.quickSort(points, left + 1, end)
        # return


    def getDistance(self, x, y):
        return math.sqrt(x ** 2 + y ** 2)



        