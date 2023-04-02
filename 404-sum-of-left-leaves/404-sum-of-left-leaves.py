# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        val=0
        if root.left and root.left.right is None and root.left.left is None:
            val+=root.left.val
        #this the first problem that I facedup in which it gives me 9 instead of 24
        # root.left
        # root.right
        #and then I make it like this to recursively go a head
        val+=self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
        return val