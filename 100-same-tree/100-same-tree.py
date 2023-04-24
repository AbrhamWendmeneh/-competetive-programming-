# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def validate(val1,val2):
            if not val1  and not val2 :
                return True
            if not val1  and val2:
                return False
            if val1 and not val2 :
                return False
            if val1.val != val2.val:
                return False
            else:
                return validate(val1.left,val2.left) and validate(val1.right,val2.right)
                                                                  
        return validate(p,q)