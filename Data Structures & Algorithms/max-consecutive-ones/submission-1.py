class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        currentOnes = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                currentOnes += 1
                if currentOnes > maxOnes:
                    maxOnes = currentOnes
            else:
                currentOnes = 0
        return maxOnes
            
        

        