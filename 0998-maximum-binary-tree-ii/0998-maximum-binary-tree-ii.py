# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            
            return TreeNode(val)
        
        if root.val < val:
            
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
            
        root.right=self.insertIntoMaxTree(root.right,val)
        
        return root
    
'''

The basic thing when I solve this question is that 
if the value root is None, then we make new tree at this point like that of 
example 2
This is my 401 Leetcode question which I have solved

                            (●'◡'●)
                            
                            \U0001f929  \U0001f929

'''
        