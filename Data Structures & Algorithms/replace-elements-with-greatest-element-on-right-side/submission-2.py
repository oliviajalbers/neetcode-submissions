class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n
        i = n - 1
        currentMax = -1
        while i > -1:
            ans[i] = currentMax
            if arr[i] > currentMax:
                currentMax = arr[i]
            i -= 1
        return ans
            




        