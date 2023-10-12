# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def symmetry(val1,val2):
            
            if val1 is None and val2 is None:
                return True
            
            if val1 is None or val2 is None:
                return False
            
            if val1.val != val2.val:
                return False
            
            return symmetry(val1.left,val2.right) and symmetry(val1.right,val2.left)
        
        return symmetry(root.left,root.right)
       
        
'''
This is recursive type of approach that I followed to solve this question

time complexity: O(n), where "n" is the number of nodes in the tree.
the space complexity: O(h), where "h" is the height of the binary tree. In the worst case, it's O(n), and in the best case, it's O(log n).

'''   