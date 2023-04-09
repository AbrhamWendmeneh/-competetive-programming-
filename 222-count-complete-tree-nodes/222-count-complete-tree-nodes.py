# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            
            return 0
        
        else:
            
            return 1+self.countNodes(root.left)+self.countNodes(root.right)
        
        
        
'''
To address this issue, I adopt a basic strategy that involves traversing the binary tree using a depth-first search (DFS) technique and tracking the number of nodes visited during the traversal. The case that I added one in the traversal is that to count the value of the root in every level of implementation

'''
        