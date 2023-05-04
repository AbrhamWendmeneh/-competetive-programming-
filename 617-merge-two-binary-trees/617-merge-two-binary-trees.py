# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
         #the case behind this problem is that to form new binary tree from two given binary trees so that we have to set some conditions 
        
        #if there is no root1 we can return root2 
        if not root1:
            return root2
        
        #if there is no root2 we can return the value of root1
        if not root2:
            return root1
        
        #in this case we have to go the addition of values in the tree to answere the question and I use preorder traversal which means root > left > right
        
        #the root part
        root1.val=root1.val+root2.val
        
        
        #in this case I choose the root1 to make my values in 
        #it and I assign root1.right for the right part of 
        #the tree and root1.left for the left part of the tree 
        #by calling the function recursively I made the solution
        
        root1.left=self.mergeTrees(root1.left,root2.left)
        
        
        root1.right=self.mergeTrees(root1.right,root2.right)
        
        return root1