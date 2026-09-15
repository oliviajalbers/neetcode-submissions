class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        stop = len(nums) - 1
        while start <= stop:
            middle = (start + stop) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                stop = middle - 1
            else:
                start = middle + 1  
        return -1