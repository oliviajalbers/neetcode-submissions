# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        queue = deque()
        level = 0
        if root:
            queue.append(root)
        while len(queue) > 0:
            current_level = []
            for i in range(len(queue)):
                current = queue.popleft()
                current_level.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(current_level)
            level += 1
        return result

        