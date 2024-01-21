# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        
        queue = deque()
        
        queue.append(root)
        
        curr_level = 0
        
        while queue:
            
            size = len(queue)
            
            if curr_level%2==0:
                
                prev_val = float('-inf')
                
            else:
                
                prev_val = float('inf')
                
            for _ in range(size):
                
                node = queue.popleft()
                
                if curr_level % 2 == 0:
                    
                    if node.val % 2 == 0 or prev_val >= node.val:
                        
                        return False
                    
                else:
                    
                    if node.val % 2 !=0 or prev_val <= node.val:
                        
                        return False 
                    
                if node.left:
                    
                    queue.append(node.left)
                    
                if node.right:
                    
                    queue.append(node.right)
                    
                prev_val = node.val
                    
            curr_level += 1
            
        return True