class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        for num in nums:
            counts[num] += 1
        print(counts)
        
        i = 0
        j = 0
        while j < len(counts):
            while counts[j] > 0:
                nums[i] = j
                i += 1
                counts[j] -= 1
            j += 1