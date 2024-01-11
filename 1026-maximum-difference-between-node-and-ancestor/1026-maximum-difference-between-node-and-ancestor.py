# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        def helper(node,min_val, max_val):
            
            if node is None:
                return abs(min_val - max_val)
            
            min_val = min(min_val, node.val)
            max_val = max(max_val, node.val)
            
            return max(helper(node.left, min_val, max_val), helper(node.right, min_val, max_val))
        return helper(root, (10**5)+1, -1)
            
                
                
            
        