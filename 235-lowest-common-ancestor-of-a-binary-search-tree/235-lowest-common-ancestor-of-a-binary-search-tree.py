# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode': 
        
        #the techinique that I used is that first I try to identify the case of           the value of the given elements are below above to the root element and           then if it is below we need to traverse to the left side of the root in           which the right side is not our concern and if if the value the p and q           are greater than the given root we need to traverse through the right             side of the root in which the left side is not out concern and the third         condition we need to consider is if the root value is between them we             know that the number that we want is find and it is the lowest common             ancestor for the given values p and q 
        
        
        if p.val < root.val and q.val <root.val:
            
            return self.lowestCommonAncestor(root.left,p,q)
        
        elif p.val > root.val and q.val > root.val:
            
            return self.lowestCommonAncestor(root.right,p,q)
        
        return root