# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        # for this question we have to use some form of traversal 
        #  right, root, left
        # which means first we have to traverse through the right most value 
        # and we then accumulate the sum of the values for each of the root values in 
        # the dictionary so as to do the next sum value
        
        
        dict_val={"sum":0}
        
        def helper(node):
            
            if not node:
                
                return None
            
            helper(node.right)
            
            dict_val["sum"]+=node.val
            
            node.val=dict_val["sum"]
            
            helper(node.left)
            
        helper(root)
        
        return root
        
        