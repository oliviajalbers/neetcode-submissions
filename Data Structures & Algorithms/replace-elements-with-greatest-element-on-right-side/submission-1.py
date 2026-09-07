class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0] * len(arr)
        i = len(arr) - 1
        ans[i] = -1
        currentMax = 0
        while i > 0:
            if arr[i] > currentMax:
                currentMax = arr[i]
            i -= 1
            ans[i] = currentMax
        return ans
            




        