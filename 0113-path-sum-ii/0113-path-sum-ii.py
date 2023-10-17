# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack=[root]
        path_stack=[(root.val,[root.val])]
        result=[]
        
        while stack:
            
            node= stack.pop()
            curr_sum, path= path_stack.pop()
            
            if not node.left and not node.right:
                
                if curr_sum == targetSum:
                    
                    result.append(path)
                    
            if node.left:
                
                stack.append(node.left)
                left_path = path +[node.left.val]
                left_sum = curr_sum + node.left.val
                path_stack.append((left_sum, left_path))
                
            if node.right:
                
                stack.append(node.right)
                right_path= path + [node.right.val]
                right_sum= curr_sum+ node.right.val
                path_stack.append((right_sum,right_path))
                
        return result
    
    
                