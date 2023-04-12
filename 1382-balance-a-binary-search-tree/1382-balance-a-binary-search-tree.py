# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nums=[]
        if root:
            nums+=self.inOrderTraversal(root)
        
        def helper(nums):
            if not nums:
                return None
            middle=len(nums)//2
            root=TreeNode(nums[middle])
            root.left=helper(nums[:middle])
            root.right=helper(nums[middle+1:])   
            return root
        return helper(nums)
    def inOrderTraversal(self, root):
        res = []
        if root:
            res += self.inOrderTraversal(root.left)
            res.append(root.val)
            res += self.inOrderTraversal(root.right)
        return res