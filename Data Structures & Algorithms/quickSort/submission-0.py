# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quickSortHelper(pairs, 0, len(pairs) - 1);
    def quickSortHelper(self, arr, start, end):
        # base case
        if end - start <= 0:
            return arr
        
        pivot = arr[end]
        left = start

        for i in range(start, end):
            if arr[i].key < pivot.key:
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1
        # swap pivot
        arr[end] = arr[left]
        arr[left] = pivot

        
        self.quickSortHelper(arr, start, left - 1)
        self.quickSortHelper(arr, left + 1, end)

        return arr


        