class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
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

        