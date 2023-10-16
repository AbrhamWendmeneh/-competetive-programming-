# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def helper(node):
            
            if not node:
                return 0
            left=helper(node.left)
            right=helper(node.right)
            return max(left,right)+1
        
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        return max(helper(root.left) + helper(root.right) + 1, max(left_diameter, right_diameter)+1) - 1
