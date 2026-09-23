class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        return self.binarySearch(piles, 1, max(piles), h)
    
    
    def binarySearch(self, piles, low, high, h):
        result = high
        while low <= high:
            mid = (low + high) // 2
            actualHours = 0
            for pile in piles:
                actualHours += math.ceil(pile / mid)
            if actualHours <= h:
                result = min(result, mid)
                high = mid - 1
            else:
                low = mid + 1
        return result

        