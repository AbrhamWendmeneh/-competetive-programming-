# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        
        value=0
        
        def dfs(root,parent,grdparent):
            
            nonlocal value
            if root is None:
                return 
            if grdparent and grdparent.val %2 ==0:
                
                value+=root.val
                
            dfs(root.left,root,parent)
            dfs(root.right,root,parent)
            
        dfs(root,None,None)
        
        return value
            
                