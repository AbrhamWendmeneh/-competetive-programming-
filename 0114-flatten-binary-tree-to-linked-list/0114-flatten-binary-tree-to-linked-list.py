# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(root):
            nonlocal prev
            if not root:
                return None
            
            helper(root.right)
            helper(root.left)
            root.right=prev
            root.left=None
            prev=root
            
        prev=None
        helper(root)
        
        
        '''
        This is done by using the concept post-order traversal which means first visit left,and then root but as the question says all of the left node are null we can change it to navigate to right, left and finally root.
        '''
        
        