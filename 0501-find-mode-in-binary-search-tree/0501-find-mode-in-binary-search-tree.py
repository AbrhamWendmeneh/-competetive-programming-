# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from statistics import mode
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        
        store={}
        stack=[root]
        
        while stack:
            
            node=stack.pop()
            
            if node.val in store:
                
                store[node.val]+=1
                
            else:
                store[node.val]=1
            
            if node.right:
                
                stack.append(node.right)
                
            if node.left:
                
                stack.append(node.left)
                
        max_val= max(store.values())
        
        return [key for key, val in store.items() if val==max_val]
        