class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxNum = max(arr)
        maxLocation = arr.index(maxNum)
        for i in range(n-1):
            if i < maxLocation:
                arr[i] = maxNum
            else:
                maxNum = max(arr[i+1:n])
                maxLocation = arr[i+1:n].index(maxNum)
                arr[i] = maxNum
        arr[n-1] = -1
        return arr


        