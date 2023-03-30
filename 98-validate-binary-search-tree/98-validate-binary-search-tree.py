# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode],prev=(-2**(31)-1),prev_2=(2**(31))) -> bool:
        if root is None:
            
            return True
        
        # val_left=self.isValidBST(root.left,prev)
        # print(prev,prev_2,root.val)
        
        
        if root.val < prev_2 and root.val>prev:
            
            val_left=self.isValidBST(root.left,prev,root.val)
            
            
            
            val_right=self.isValidBST(root.right,root.val,prev_2)
            
            
            
            return val_left and val_right
        
        return False
    '''
        val_left=self.isValidBST(root.left,prev)   
        val_right=self.isValidBST(root.right) 
        return val_right and val_left'''
    
        
        