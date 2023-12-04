# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result=0
        
        def helper(node):
            nonlocal result
            if not node:
                return
            helper(node.left)
            if low<= node.val <= high:
                result+=node.val
            helper(node.right)
        helper(root)
        return result
        
            