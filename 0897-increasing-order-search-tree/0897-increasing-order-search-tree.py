# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        result= TreeNode(0)
        
        current=result
        
        def helper(node):
            
            nonlocal current
            
            if not node:
                
                return
            
            helper(node.left)
            
            current.right= TreeNode(node.val)
            
            current= current.right
            
            helper(node.right)
            
        helper(root)
        
        return result.right
        
        
        
        