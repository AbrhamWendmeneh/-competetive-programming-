# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        #if the root value doesn't have value in it we simply add val to           the empty node and return the value, it is base case for the             following implementation 
        if root is None:
            return TreeNode(val)
        
        # if the first condition is not full filled we evaluate the root            that we want is in the position of the root either right left            or at the root part the conditions below this explains the              cases
        
        elif root.val==val:
            return self.TreeNode(val)
        
        elif root.val>val:
            root.left= self.insertIntoBST(root.left,val)
            
        else:
            root.right= self.insertIntoBST(root.right,val)

        return root
