# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        if not root1 or not root2:
            
            return 
        
        def helper(root):
            
            result = []
            
            stack = [root]
            
            while stack:
                
                node = stack.pop()
                
                if node.right is None and node.left is None:
                    
                    result.append(node.val)
                    
                if node.left:
                    
                    stack.append(node.left)
                    
                if node.right:
                    
                    stack.append(node.right)
         
            return result
        
                    
        val1 = helper(root1)
        
        val2 = helper(root2)
        
        return val1 == val2
                    
                
                
        

        