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
        length = len(queue)
        while length > 0:
            for i in range(length):
                current = queue.popleft()
                if i == length - 1:
                    result.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            length = len(queue)
        return result
        