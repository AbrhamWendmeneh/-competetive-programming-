# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def helper(node,first = None, second=None, prev = None):
         
            if not node:
                return first, second, prev
            first, second, prev = helper(node.left, first, second, prev)
            
            if prev and node.val< prev.val:
                if not first:
                    first=prev
                second=node
            prev=node
            return helper(node.right,first, second,prev)
       
        first ,second, res=helper(root)
        first.val,second.val=second.val,first.val
            