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
        
        queue = deque([root])
        
        result = []
        
        while queue:
            
            size = len(queue)
            temp = float(-inf)
            
            for _ in range(size):
                
                node_val = queue.popleft()
                temp = max(node_val.val, temp)
                
                if node_val.left:
                    queue.append(node_val.left)
                if node_val.right:
                    queue.append(node_val.right)
                          
            result.append(temp)
            
        return result
                
        