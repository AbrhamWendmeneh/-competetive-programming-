# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        
        count=0
        
        def dfs(node):
            
            nonlocal count
            
            if not node:
                
                return 0,0
            
            leftsum, leftcount= dfs(node.left)
            
            rightsum, rightcount=dfs(node.right)
            
            sumval= leftsum+node.val+rightsum
            
            sumcount= leftcount+rightcount+1 
            
            if sumval//sumcount==node.val:
                
                count+=1
                
            return sumval, sumcount
        
        dfs(root)
        
        return count