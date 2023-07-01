# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def helper(node):
            if not node:
                return ""
            result = str(node.val)
            left=helper(node.left)
            right=helper(node.right)
            
            if right or left:
                result+= "(" + left + ")"
            if right:
                result+= "(" + right + ")"
            return result
        return helper(root)
    
    '''
    this implementation uses preorder traversal method and it test if the 
    first value is none or not if not it goes with the node.left value 
    and node.right value after that append the result to the current result       string, and finally return the final result
    '''
    
                