# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(root):
            if not root:
                return 0
            right=height(root.right)
            left=height(root.left)
            return max(right,left)+1
        height(root)
        if root is None:
            return True
        else:
            left=height(root.left)

            right=height(root.right)

            if abs(left-right)<=1 and self.isBalanced(root.left) is True and self.isBalanced(root.right) is True:
                return True
            else:
                return False
        
    