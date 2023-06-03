# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        #dfs
        
        if root is None:
            
            return False
        
        stack=[root]
        val=[root.val]
        
        while stack:
            
            res=stack.pop()
            innerval=val.pop()
            print(innerval)
            
            if not res.left and not res.right:
                if (innerval==targetSum):
                    return True
                
    
            if res.left:
                
                stack.append(res.left)
                val.append(res.left.val+innerval)
                
            if res.right:
                
                stack.append(res.right)
                val.append(res.right.val+innerval)
                
        return False
            
        
        