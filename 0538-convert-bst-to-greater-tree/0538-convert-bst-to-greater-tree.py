# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        dict_val={"sum":0}
        
        def helper(node):
            
            if not node:
                
                return None
            
            helper(node.right)
            
            dict_val["sum"]+= node.val
            
            node.val= dict_val["sum"]
            
            helper(node.left)
            
        helper(root)
        
        return root