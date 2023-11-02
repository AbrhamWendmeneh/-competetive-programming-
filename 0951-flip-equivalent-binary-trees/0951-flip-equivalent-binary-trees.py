# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def dfs(node1, node2):
            
            if not node1 and not node2:
                return True
                
            if not node1 or not node2:
                return False
            
            if node1.val!=node2.val:
                return False
            
            left=  dfs(node1.left,node2.left)
            right= dfs(node1.right, node2.right)
            
            lefright= dfs(node1.left, node2.right)
            righleft= dfs(node1.right, node2.left)
            
            
            return (left and right ) or ( lefright and righleft)
        
        return dfs(root1, root2)
    
    
    
    
    
    
    
    
    
    