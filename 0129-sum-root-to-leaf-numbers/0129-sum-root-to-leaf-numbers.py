# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return []
        
        stack=[(root,[root.val])]
        path=[]
        result=0
        
        while stack:
            
            node,curr_path=stack.pop()
            
            if node.right is None and node.left is None:
                path.append(curr_path)
                
            if node.right:
                stack.append((node.right,curr_path+[node.right.val]))
                
            if node.left:
                stack.append((node.left,curr_path+[node.left.val]))
                
        for digits in path:
            
             result+=int(''.join(map(str, digits)))
                
        return result
        