
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        array=[]
        setval=set()
        def small(root):
            if root is None:
                return
            else:
                small(root.left)
                if  root.val not in setval:
                    array.append(root.val)
                    setval.add(root.val)
                small(root.right)
        small(root)        
        if len(list(set(array)))==1:
            return -1
        val=sorted(array)
        return val[1]
            