# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        result=[]
        
        def helper(node):
            
            if not node:
                
                return 
            
            helper(node.left)
            
            result.append(node.val)
            
            helper(node.right)
            
        helper(root)
        
        set_val= set()
        
        for i in result:
            
            if k - i in set_val:
                
                return True
            
            else:
                
                set_val.add(i)
                
        return False