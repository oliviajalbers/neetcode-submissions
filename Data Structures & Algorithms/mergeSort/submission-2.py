# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # base case
        if len(pairs) <= 1:
            return pairs
        # merge sort
        start = 0
        end = len(pairs)
        mid = end // 2
        left = self.mergeSort(pairs[start:mid])
        right = self.mergeSort(pairs[mid:end])
        # merge
        return self.merge(left, right)
    def merge(self, left: List[Pair], right: List[Pair]):
        pairs = [None] * (len(left) + len(right))
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                pairs[k] = left[i]
                i += 1
            else:
                pairs[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            pairs[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            pairs[k] = right[j]
            j += 1
            k += 1
        
        return pairs

