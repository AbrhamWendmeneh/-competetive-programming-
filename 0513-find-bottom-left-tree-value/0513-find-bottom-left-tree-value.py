# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
       
        if not root:
            return None
        queue=deque()
        queue.append(root)
        while queue:
            curr_left=queue[0]
            size=len(queue)
            for _ in range(size):
                node= queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            left_most_val=curr_left.val
        return left_most_val

  