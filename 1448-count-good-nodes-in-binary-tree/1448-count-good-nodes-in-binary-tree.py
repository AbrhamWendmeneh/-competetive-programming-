# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        stack=[]
        max_val= float('-inf')
        stack.append((root,max_val))
        count= 0
        
        
        while stack:
            
            node,max_val=stack.pop()
            
            if node.val >= max_val:
                
                max_val= node.val
                
                count+=1
                
            if node.right:
                
                stack.append((node.right,max_val))
                
            if node.left:
                
                stack.append((node.left,max_val))
                
        return count
                    
                
                
                
        