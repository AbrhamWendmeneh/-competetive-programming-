# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        counter=0
        if root is None:
            return 0
        else:
            a=self.maxDepth(root.left)
            b=self.maxDepth(root.right)
        return max(a,b)+1
        