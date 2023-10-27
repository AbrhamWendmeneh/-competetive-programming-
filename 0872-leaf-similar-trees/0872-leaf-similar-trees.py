# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1:
            return
        result1=[]
        stack=[root1]
        while stack:
            node=stack.pop()
            if node.right is None and node.left is None:
                result1.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
                
    
        result2=[]
        stack2=[root2]
        while stack2:
            node=stack2.pop()
            if node.right is None and node.left is None:
                result2.append(node.val)
            if node.right:
                stack2.append(node.right)
            if node.left:
                stack2.append(node.left)
                
        return result1==result2
        
        
        