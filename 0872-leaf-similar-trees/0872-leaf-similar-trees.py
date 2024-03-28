# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        
        
        if not root1 or not root2:
            
            return
        
        def dfs(root):
            
            result = []
        
            stack = [root]
        
            while stack:

                currentVal = stack.pop()

                if currentVal.right is None and currentVal.left is None:
                    result.append(currentVal.val)

                if currentVal.right:
                    stack.append(currentVal.right)

                if currentVal.left:
                    stack.append(currentVal.left)
                
            return result
        
        tree1 = dfs(root1)
        
        tree2 = dfs(root2)
        
        return tree1 == tree2
        
        
        
        