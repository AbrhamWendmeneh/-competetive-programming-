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
        
        def checkVal(root):
            
            result=[]
            stack=[root]
            
            while stack:
                
                node= stack.pop()
                
                if node.left is None and node.right is None:
                    
                    result.append(node.val)
                if node.right:
                    
                    stack.append(node.right)
                    
                if node.left:
                    
                    stack.append(node.left)
                    
            return result
        
        return checkVal(root1)== checkVal(root2)  
    
    
'''
this is the efficient one beside the first one 
  '''  
        