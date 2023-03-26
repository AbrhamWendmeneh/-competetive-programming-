# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        if root is None:
            
            return False
        
        else:
            
            if root.right is None and root.left is None and root.val==targetSum:
                
                return True
            
            else:
                
                return self.hasPathSum(root.left,(targetSum-root.val)) or self.hasPathSum(root.right,(targetSum-root.val))
                
                
                
'''
the following code is recursive type in which it tries to find the value of target sum is found in the tree given in the question and then it returns true if the required value is found in the tree otherwise it returns false in the final stage after evaluating all nodes that are found in the tree 
 the last else statement is used in this case that evalutes root.left val and targetval 
 
 
'''