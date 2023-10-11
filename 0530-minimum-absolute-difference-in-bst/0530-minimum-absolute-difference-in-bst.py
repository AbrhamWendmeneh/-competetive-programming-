# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inorder(root):
            nonlocal prev, mindiff
            if not root:
                return 
            inorder(root.left)
            if prev is not None:
                mindiff=min(mindiff,abs(root.val-prev))
            prev=root.val
            inorder(root.right)
        mindiff= float('inf')
        prev= None
        inorder(root)
        return mindiff
            