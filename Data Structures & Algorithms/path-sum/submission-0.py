# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        actualSum = 0
        def findPath(root, targetSum, actualSum):
            if not root:
                return False
            actualSum += root.val
            if not root.left and not root.right and actualSum == targetSum:
                return True
            if findPath(root.left, targetSum, actualSum):
                return True
            if findPath(root.right, targetSum, actualSum):
                return True
            actualSum -= root.val
            return False
        return findPath(root, targetSum, actualSum)



        