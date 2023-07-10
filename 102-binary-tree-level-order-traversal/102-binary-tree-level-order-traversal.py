# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[]
        queue=deque()
        queue.append(root)
        
        while queue:
            
            level_val=[]
            level_siz=len(queue)
            for _ in range(level_siz):
                value=queue.popleft()
                level_val.append(value.val)
                
                if value.left:
                    queue.append(value.left)
                if value.right:
                    queue.append(value.right)
                    
            result.append(level_val)
            
        return result