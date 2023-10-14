# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result=[]
        queue=deque()
        queue.append(root)
        
        while queue:
            
            level_val=[]
            size=len(queue)
            
            for _ in range(size):
                
                curr=queue.popleft()
                level_val.append(curr.val)
                
                if curr.left:
                    queue.append(curr.left)
                    
                if curr.right:
                    queue.append(curr.right)
                    
            result.append(level_val)
            
        return result[::-1]
            
        
        