# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # def countVal(root):
        #     if root:
        #         return 1+countVal(root.left)+countVal(root.right)
        #try it latter
        #using DFS
        '''stack_val=[]
        while root:
            stack_val.append(root) #for the first case root = [3,1,4,null,2]
            
            # stack_val=[3]
            
        
        root=root.left
        # counter=0
        for counter in range(k-1):
            root=stack_val.pop()
            root=root.right
            while root:
                stack_val.append(root)
                root=root.left
            # counter+=1
        #stack_val=[]
        return stack_val[-1].val'''
        res=[]
        def val(root):
            if root is None:
                return 
            val(root.left)
            res.append(root.val)
            val(root.right)
        val(root)
        return res[k-1]
            