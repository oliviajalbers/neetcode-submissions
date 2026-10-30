# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = deque()
        if root:
            queue.append(root)
        current = None
        length = len(queue)
        while queue:
            for i in range(length):
                current = queue.popleft() 
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            result.append(current.val)
            length = len(queue)
        return result
        