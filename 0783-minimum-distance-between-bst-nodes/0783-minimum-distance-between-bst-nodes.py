# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        
        result= float('inf')
        prev=None
        
        def helper(node):
            
            nonlocal result, prev
            
            if not node:
                
                return 
            
            helper(node.left)
            
            if prev is not None:
                
                result= min(result, abs(node.val- prev))
                
            prev= node.val
            
            helper(node.right)
            
            return result
            
        helper(root)
        
        return result
            