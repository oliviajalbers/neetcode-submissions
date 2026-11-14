class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        
        def dfs(i, current, currentSum):
            if currentSum == target:
                results.append(current.copy())
                return
            if i >= len(nums) or currentSum > target:
                return
            current.append(nums[i])
            dfs(i, current, currentSum + nums[i])
            current.pop()
            dfs(i+1, current, currentSum)
        
        dfs(0, [], 0)
        return results
        