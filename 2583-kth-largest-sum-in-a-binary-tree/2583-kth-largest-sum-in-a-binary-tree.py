# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return 0
        
        queue=deque()
        queue.append(root)
        result=[]
        
        while queue:
            
            level=[]
            size=len(queue)
            
            for _ in range(size):
                
                node =  queue.popleft()                
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(sum(level))
            
        if len(result) >=k:
            return sorted(result)[-k]
            
        else: return -1
                
                