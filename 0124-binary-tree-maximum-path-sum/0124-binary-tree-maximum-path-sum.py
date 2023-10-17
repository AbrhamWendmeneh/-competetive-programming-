# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum=float('-inf')
        visited=set()
        def helper(node):
            nonlocal max_sum
            if not node or node in visited:
                return 0
            visited.add(node)
            left_max_sum= max(0,helper(node.left))
            right_max_sum= max(0,helper(node.right))
            
            local_val= left_max_sum + right_max_sum+node.val
            
            
            max_sum=max(max_sum, local_val)
            
            return node.val+ max(left_max_sum,right_max_sum)
            
        helper(root)
        return max_sum
                