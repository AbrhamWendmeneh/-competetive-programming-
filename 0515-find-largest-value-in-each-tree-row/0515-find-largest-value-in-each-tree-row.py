# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        queue=deque()
        queue.append(root)
        result=[]
        
        while queue:
            
            size=len(queue)
            level=[]
            
            for _ in range(size):
                
                curr_node=queue.popleft()
                
                level.append(curr_node.val)
                
                if curr_node.left:
                    
                    queue.append(curr_node.left)
                    
                if curr_node.right:
                    
                    queue.append(curr_node.right)
                    
            result.append(max(level))
            
        return result