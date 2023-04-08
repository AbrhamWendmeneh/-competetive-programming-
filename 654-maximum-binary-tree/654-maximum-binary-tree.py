# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return 0
        
        else:
            val=max(nums)
            slicing_val=nums.index(val)
            root=TreeNode(val)
            # vaidate_1=len(nums[:max(nums)+1])
            # validate_2=[max(nums)+1:]
            left_val=len(nums[:slicing_val])
            right_val=len(nums[slicing_val+1:])
            
            if left_val:
                root.left=self.constructMaximumBinaryTree(nums[:slicing_val])
            if right_val :
                root.right=self.constructMaximumBinaryTree(nums[slicing_val+1:])
        return root
            
        '''
        this the modified from the last one only with naming
        for this question I have tried to do in different approaches but It uses similar approache to the question on the leetcode 108. Convert Sorted Array to Binary Search Tree with little difference 
        ->first I evaluate the maximum among the nums and then using the value of the maximum value index I use to evaluate the left and the right elements of the root and the value of the maximum one is stored in the root value of the subsquent roots from the first one to the others
        
        '''