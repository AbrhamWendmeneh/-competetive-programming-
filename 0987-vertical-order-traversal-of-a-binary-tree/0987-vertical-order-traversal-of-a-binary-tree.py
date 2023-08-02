# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        memo={} # this is used to store values which are in the same column
        stack=[(root,0,0)]
        
        while stack:
            node,col,row= stack.pop()
            if col in memo:
                memo[col].append((node.val,row))
            else:
                memo[col]= [(node.val,row)]
                
            if node.left:
                stack.append((node.left,col-1,row+1))
            if node.right:
                stack.append((node.right,col+1,row+1))
                
        result=[]
        for val in sorted(memo.keys()):

            sorted_nodes = sorted(memo[val], key=lambda x: (x[1], x[0])) 
            # sort by row first, then by value
            
            result.append([node_val for node_val, _ in sorted_nodes])
            
        return result
        
                
            