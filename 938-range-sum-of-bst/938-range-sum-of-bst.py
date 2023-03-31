# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result=[]
        
        def val(root):
            
            if root is None:
                
                return
            
            val(root.left)
            
            result.append(root.val)
            
            val(root.right)
            
        sum_val=0
        
        val(root)
        
        for i in result:
            
            if i in range(low,high+1):
                
                sum_val+=i
                
        return sum_val
    
    
'''
the method that I want to solve is appending the values to the empty list called result and then the value are inorder in which they are ordered in accending order and then through iteration I try to find the interval of the position of the values and then if they are in the given interval I add the valus to my sum_val and then returning it after finishing the all the cases
 
'''    
            