# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
#         if root is None:
#             return 
            
#         if root.left is None and root.right is None:
#             return [str(root.val)]
#         left=self.binaryTreePaths(root.left)
#         right=self.binaryTreePaths(root.left)
#         left_val=[]
#         for i in left:
#             left_val.append(str(root.val))
#             left_val.append('->')
#             left_val.append(str(i.val)
#         for j in right:
#             right_val.append(str(root.val))
#             right_val.append('->')
#             right_val.append('j.val')
#         return left_val+ right_val
        path=[]
        def function(root,pathin):
            if root.left is None and root.right is None:
                path.append('->'.join(pathin))
                return
            if root.left:
                function(root.left,pathin+[str(root.left.val)])
            if root.right:
                function(root.right,pathin+[str(root.right.val)])
                                            
        function(root,[str(root.val)])
        return path